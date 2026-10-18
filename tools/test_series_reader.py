"""Headless browser checks. All sample chapters are intercepted test-only data."""
import functools
import hashlib
import http.server
import io
import json
from pathlib import Path
import shutil
import threading
import unittest

from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
LEGACY_READER_SHA256 = "37bcd83de8cd4190fadb19a7456efb3318ad6812f8d674ccbbd3896d0a552376"


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


class ReaderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(QuietHandler, directory=str(ROOT)))
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.origin = f"http://127.0.0.1:{cls.server.server_port}"
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch(headless=True, executable_path=shutil.which("chromium"))
        stream = io.BytesIO()
        Image.new("RGB", (1080, 2400), "#262b34").save(stream, format="WEBP")
        cls.image = stream.getvalue()

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.playwright.stop()
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def setUp(self):
        self.context = self.browser.new_context(viewport={"width": 390, "height": 844}, is_mobile=True, has_touch=True)
        self.addCleanup(self.context.close)
        self.page = self.context.new_page()
        self.errors = []
        self.page.on("pageerror", lambda error: self.errors.append(str(error)))
        self.page.route("https://fonts.googleapis.com/**", lambda route: route.abort())
        self.page.route("https://fonts.gstatic.com/**", lambda route: route.abort())
        self.manifest = {"schema_version": 1, "slug": "test-series", "title": "Reader QA fixture", "synopsis": "Test-only layout, not a chapter release.", "chapters": [
            {"n": 1, "title": "First test", "width": 1080, "segments": [["001.webp", 2400], ["002.webp", 2400]], "thumbnail": "thumb.webp"},
            {"n": 2, "title": "Second test", "width": 1080, "segments": [["001.webp", 2400]]}
        ]}
        self.page.route("**/manhwa/series/test-series/series.json", lambda route: route.fulfill(content_type="application/json", body=json.dumps(self.manifest)))
        self.page.route("**/manhwa/series/test-series/ch/*/*.webp", lambda route: route.fulfill(content_type="image/webp", body=self.image))

    def load(self, suffix="read.html?series=test-series&ch=1"):
        self.page.goto(self.origin + "/manhwa/series/" + suffix)
        self.page.wait_for_function("document.querySelector('#status').hidden || !document.querySelector('#status').textContent.startsWith('Loading')")

    def test_visual_mobile_navigation_and_separate_progress(self):
        self.page.add_init_script("localStorage.setItem('lwmz-pos', JSON.stringify({ch:44}));")
        self.load()
        self.assertTrue(self.page.locator("#reader").is_visible())
        self.assertEqual(self.page.locator("#strip img").count(), 2)
        self.page.wait_for_function("[...document.querySelectorAll('#strip img')].every(image => image.complete && image.naturalWidth === 1080)")
        self.page.evaluate("async () => { await Promise.all([...document.querySelectorAll('#strip img')].map(image => image.decode())); }")
        self.assertFalse(self.page.locator("#narration").is_visible())
        self.assertEqual(self.page.locator("#audio").get_attribute("src"), None)
        self.assertFalse(self.page.evaluate("document.documentElement.scrollWidth > innerWidth"))
        for image in self.page.locator("#strip img").all():
            self.assertEqual(image.bounding_box()["width"], 390)
        self.assertEqual(self.page.evaluate("JSON.parse(localStorage.getItem('lwmz-pos')).ch"), 44)
        self.assertEqual(self.page.evaluate("JSON.parse(localStorage.getItem('manhwa:test-series:position')).ch"), 1)
        self.page.locator("#endnav").scroll_into_view_if_needed()
        self.page.wait_for_function("JSON.parse(localStorage.getItem('manhwa:test-series:read') || '{}')['1'] === 1")
        self.page.locator("#nextbig").click()
        self.page.wait_for_url("**&ch=2")
        self.page.wait_for_function("!document.querySelector('#reader').hidden")
        self.assertEqual(self.page.locator("#next").get_attribute("aria-disabled"), "true")
        self.assertFalse(self.page.locator("#nextbig").is_visible())
        self.page.locator("#all-chapters").click()
        self.page.wait_for_function("!document.querySelector('#series').hidden")
        self.assertEqual(self.page.locator(".chapter-link").count(), 2)
        self.assertFalse(self.page.evaluate("document.documentElement.scrollWidth > innerWidth"))
        self.assertFalse(self.errors)

    def test_missing_chapter_invalid_series_and_no_script_injection(self):
        self.load("read.html?series=test-series&ch=999")
        self.assertIn("not available", self.page.locator("#status").inner_text())
        self.assertEqual(self.page.locator("#strip img").count(), 0)
        self.load("read.html?series=..%2F..%2Fsecret")
        self.assertIn("Choose a series", self.page.locator("#status").inner_text())
        self.manifest["title"] = "<img src=x onerror=alert(1)>"
        self.load("?series=test-series")
        self.assertEqual(self.page.locator("#title img").count(), 0)
        self.assertEqual(self.page.locator("#title").inner_text(), self.manifest["title"])
        self.assertFalse(self.errors)

    def test_optional_narration_and_desktop_width(self):
        self.manifest["chapters"][0]["audio"] = {"file": "audio.mp3"}
        self.load()
        self.assertTrue(self.page.locator("#narration").is_visible())
        self.assertTrue(self.page.locator("#audio").get_attribute("src").endswith("/ch/001/audio.mp3"))
        self.assertTrue(self.page.locator("#audio").evaluate("audio => audio.paused && !audio.autoplay && audio.preload === 'none'"))
        self.page.set_viewport_size({"width": 1440, "height": 900})
        self.assertEqual(self.page.locator("#strip").bounding_box()["width"], 720)
        self.assertFalse(self.page.evaluate("document.documentElement.scrollWidth > innerWidth"))
        self.assertFalse(self.errors)

    def test_failed_page_is_reported_without_breaking_navigation(self):
        self.page.route("**/manhwa/series/test-series/ch/001/001.webp", lambda route: route.fulfill(status=404))
        self.load()
        self.page.locator(".image-error").wait_for()
        self.assertTrue(self.page.locator("#next").is_visible())
        self.assertFalse(self.errors)

    def test_old_reader_bytes_and_follow_behavior(self):
        self.assertEqual(hashlib.sha256((ROOT / "manhwa/read.html").read_bytes()).hexdigest(), LEGACY_READER_SHA256)
        self.page.goto(self.origin + "/manhwa/read.html?ch=1")
        self.page.wait_for_function("document.querySelector('#pick').options.length > 0")
        self.assertIn("on", self.page.locator("#follow").get_attribute("class"))
        self.page.evaluate("dispatchEvent(new Event('wheel'))")
        self.assertIn("on", self.page.locator("#follow").get_attribute("class"))
        self.page.evaluate("Object.defineProperty(document.querySelector('#aud'), 'paused', {value:false, configurable:true}); dispatchEvent(new Event('touchmove'))")
        self.assertNotIn("on", self.page.locator("#follow").get_attribute("class"))
        self.page.locator("#follow").click()
        self.assertIn("on", self.page.locator("#follow").get_attribute("class"))
        self.assertFalse(self.errors)


if __name__ == "__main__":
    unittest.main()
