"""Headless browser checks. All sample chapters are intercepted test-only data."""
import functools
import hashlib
import http.server
import io
import json
import math
import re
from pathlib import Path
import shutil
import struct
import threading
import unittest
import wave

from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
LEGACY_SCRIPT_SHA256 = "120fb47b529d6e00c3e75d16b48fd61963a8781321cc3fbb43903aa7131ec310"


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    pdf_bytes = b''

    def do_GET(self):
        if self.path == '/manhwa/series/test-series/ch/001/reading.pdf':
            self.send_response(200)
            self.send_header('Content-Type', 'application/pdf')
            self.send_header('Content-Length', str(len(self.pdf_bytes)))
            self.end_headers()
            self.wfile.write(self.pdf_bytes)
        else:
            super().do_GET()

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
        stream = io.BytesIO()
        Image.new('RGB', (10, 10), 'white').save(stream, format='PDF')
        cls.test_pdf = QuietHandler.pdf_bytes = stream.getvalue()
        # An audible test tone exercises the native media clock; never a release asset.
        stream = io.BytesIO()
        with wave.open(stream, 'wb') as audio:
            audio.setnchannels(1); audio.setsampwidth(2); audio.setframerate(8000)
            audio.writeframes(b''.join(struct.pack('<h', int(4000 * math.sin(2 * math.pi * 220 * i / 8000))) for i in range(160000)))
        cls.test_audio = stream.getvalue()

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.playwright.stop()
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def setUp(self):
        self.context = self.browser.new_context(viewport={"width": 390, "height": 844}, is_mobile=True, has_touch=True, accept_downloads=True)
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
        def audio_route(route):
            requested = route.request.headers.get('range', '')
            if requested.startswith('bytes='):
                start, end = requested[6:].split('-', 1)
                start = int(start or 0); end = min(int(end) if end else len(self.test_audio) - 1, len(self.test_audio) - 1)
                route.fulfill(status=206, content_type='audio/wav', headers={'Accept-Ranges': 'bytes', 'Content-Range': f'bytes {start}-{end}/{len(self.test_audio)}'}, body=self.test_audio[start:end + 1])
            else:
                route.fulfill(content_type='audio/wav', headers={'Accept-Ranges': 'bytes'}, body=self.test_audio)
        self.page.route("**/manhwa/series/test-series/ch/*/test-tone.wav", audio_route)

    def load(self, suffix="read.html?series=test-series&ch=1"):
        self.page.goto(self.origin + "/manhwa/series/" + suffix)
        self.page.wait_for_function("document.querySelector('#status').hidden || !document.querySelector('#status').textContent.startsWith('Loading')")

    def test_visual_mobile_navigation_and_separate_progress(self):
        self.page.add_init_script("localStorage.setItem('lwmz-pos', JSON.stringify({ch:44}));")
        self.load()
        self.assertTrue(self.page.locator("#reader").is_visible())
        self.assertEqual(self.page.locator("#strip img").count(), 2)
        self.assertEqual(self.page.locator("#strip img").evaluate_all("images => images.map(image => image.id)"), ["panel-01", "panel-02"])
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

    def test_reading_pdf_download_and_unsafe_filename_rejection(self):
        self.manifest['chapters'][0]['pdf'] = 'reading.pdf'
        pdf_bytes = self.test_pdf
        self.load()
        link = self.page.locator('#download-pdf')
        self.assertTrue(link.is_visible())
        self.assertTrue(link.get_attribute('href').endswith('/ch/001/reading.pdf'))
        self.assertEqual(link.get_attribute('download'), 'test-series-chapter-1.pdf')
        with self.page.expect_download() as event:
            link.click()
        self.assertEqual(Path(event.value.path()).read_bytes(), pdf_bytes)
        self.manifest['chapters'][0]['pdf'] = '../private.pdf'
        self.load()
        self.assertIn('unavailable', self.page.locator('#status').inner_text())
        self.assertEqual(self.page.locator('#strip img').count(), 0)
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
        self.assertFalse(self.page.locator("#follow").is_visible())
        self.page.set_viewport_size({"width": 1440, "height": 900})
        self.assertEqual(self.page.locator("#strip").bounding_box()["width"], 720)
        self.assertFalse(self.page.evaluate("document.documentElement.scrollWidth > innerWidth"))
        self.assertFalse(self.errors)

    def narration_fixture(self):
        self.manifest['chapters'][0]['audio'] = {
            'file': 'test-tone.wav', 'duration': 20, 'cues': [
                {'t': 0, 'segment': '001.webp', 'y': 0},
                {'t': 4, 'segment': '001.webp', 'y': 1200, 'panel': 1, 'line': 1},
                {'t': 10, 'segment': '002.webp', 'y': 0, 'panel': 2},
                {'t': 16, 'segment': '002.webp', 'y': 1200, 'panel': 2, 'line': 2},
            ]}
        self.load()
        self.page.evaluate("async () => { await Promise.all([...document.querySelectorAll('#strip img')].map(image => image.decode())); }")

    def seek(self, time):
        self.page.locator('#audio').evaluate('(audio, time) => { audio.currentTime = time; }', time)
        self.page.wait_for_function('(time) => !document.querySelector("#audio").seeking && Math.abs(document.querySelector("#audio").currentTime - time) < .03', arg=time)

    def test_follow_uses_media_clock_and_stops_when_paused(self):
        self.narration_fixture()
        self.assertEqual(self.page.locator('#follow').get_attribute('aria-pressed'), 'true')
        self.assertTrue(self.page.locator('#audio').evaluate('audio => audio.paused'))
        self.page.locator('#audio').evaluate('audio => audio.play()')
        self.page.wait_for_function('document.querySelector("#audio").currentTime > .08')
        self.page.locator('#audio').evaluate('audio => audio.pause()')
        self.seek(10)
        self.assertEqual(self.page.locator('#follow').get_attribute('aria-pressed'), 'true')
        image_top = self.page.locator('#strip img').nth(1).bounding_box()['y']
        controls = self.page.locator('#narration').bounding_box()
        self.assertGreaterEqual(image_top, controls['y'] + controls['height'] + 20)
        self.assertLess(image_top, controls['y'] + controls['height'] + 80)
        forward_y = self.page.evaluate('scrollY')
        self.page.wait_for_timeout(180)
        self.assertEqual(self.page.evaluate('scrollY'), forward_y)
        self.seek(1)
        self.assertLess(self.page.evaluate('scrollY'), forward_y - 200)
        self.assertTrue(self.page.locator('#audio').evaluate('audio => audio.paused'))
        self.assertFalse(self.errors)

    def test_manual_scroll_disables_follow_and_seek_respects_it(self):
        self.narration_fixture()
        self.page.locator('#audio').evaluate('audio => audio.play()')
        self.page.wait_for_function('document.querySelector("#audio").currentTime > .08')
        self.page.mouse.wheel(0, 220)
        self.page.wait_for_function('document.querySelector("#follow").getAttribute("aria-pressed") === "false"')
        self.assertFalse(self.page.locator('#audio').evaluate('audio => audio.paused'))
        self.page.locator('#audio').evaluate('audio => audio.pause()')
        self.page.wait_for_timeout(150)
        manual_y = self.page.evaluate('scrollY')
        self.seek(16)
        self.page.wait_for_timeout(100)
        self.assertEqual(self.page.evaluate('scrollY'), manual_y)
        self.page.locator('#follow').click()
        self.assertEqual(self.page.locator('#follow').get_attribute('aria-pressed'), 'true')
        self.assertGreater(self.page.evaluate('scrollY'), manual_y + 300)
        self.page.locator('#follow').evaluate('button => button.blur()')
        self.page.keyboard.press('PageUp')
        self.assertEqual(self.page.locator('#follow').get_attribute('aria-pressed'), 'false')
        self.assertFalse(self.errors)

    def test_follow_touch_override_resize_and_audio_failure(self):
        self.narration_fixture()
        self.page.locator('#audio').evaluate('audio => audio.play()')
        self.page.wait_for_function('document.querySelector("#audio").currentTime > .08')
        self.page.set_viewport_size({'width': 360, 'height': 780})
        self.assertFalse(self.page.evaluate('document.documentElement.scrollWidth > innerWidth'))
        self.page.evaluate("document.querySelector('#strip').dispatchEvent(new Event('touchmove', {bubbles:true}))")
        self.assertEqual(self.page.locator('#follow').get_attribute('aria-pressed'), 'false')
        self.page.route('**/test-tone.wav', lambda route: route.fulfill(status=404))
        self.load()
        self.page.locator('#audio').evaluate('audio => { audio.play().catch(() => {}); }')
        self.page.locator('#audio-error').wait_for()
        self.assertTrue(self.page.locator('#reader').is_visible())
        self.assertFalse(self.page.locator('#follow').is_visible())
        self.assertFalse(self.errors)

    def test_invalid_narration_cues_are_rejected(self):
        self.manifest['chapters'][0]['audio'] = {'file': 'test-tone.wav', 'duration': 20}
        for cue in [
            {'t': -1, 'segment': '001.webp', 'y': 0},
            {'t': 0, 'segment': 'missing.webp', 'y': 0},
            {'t': 0, 'segment': '001.webp', 'y': 2401},
            {'t': 0, 'segment': '001.webp', 'y': 0, 'line': 0},
        ]:
            with self.subTest(cue=cue):
                self.manifest['chapters'][0]['audio']['cues'] = [cue]
                self.load()
                self.assertIn('unavailable', self.page.locator('#status').inner_text())
                self.assertEqual(self.page.locator('#strip img').count(), 0)
        self.assertFalse(self.errors)

    def test_late_focus_is_revealed_with_minimal_scroll_and_scaled_gutters(self):
        self.manifest['chapters'][0]['gutters'] = {'001.webp': 216}
        self.manifest['chapters'][0]['framing_height'] = 2880
        self.narration_fixture()
        first, second = self.page.locator('#strip img').all()
        self.assertAlmostEqual(second.bounding_box()['y'] - first.bounding_box()['y'] - first.bounding_box()['height'], 78, delta=1)
        self.manifest['chapters'][0]['audio']['cues'][2]['y'] = 2300
        self.manifest['chapters'][0]['audio']['cues'][3]['y'] = 2400
        self.load()
        self.page.locator('#audio').evaluate('audio => audio.play()')
        self.page.wait_for_function('document.querySelector("#audio").currentTime > .08')
        self.page.locator('#audio').evaluate('audio => audio.pause()')
        self.seek(10)
        box = self.page.locator('#strip img').nth(1).bounding_box()
        self.assertGreater(box['y'], -100)
        self.assertLess(box['y'] + 2300 * 390 / 1080, 844)
        self.page.set_viewport_size({'width':1440,'height':900})
        self.assertEqual(self.page.locator('#strip').bounding_box()['width'], 390)
        self.assertFalse(self.errors)

    def test_failed_page_is_reported_without_breaking_navigation(self):
        self.page.route("**/manhwa/series/test-series/ch/001/001.webp", lambda route: route.fulfill(status=404))
        self.load()
        self.page.locator(".image-error").wait_for()
        self.assertTrue(self.page.locator("#next").is_visible())
        self.assertFalse(self.errors)

    def test_old_reader_bytes_and_follow_behavior(self):
        # Engagement adds external CSS/JS; the original player/Follow/progress
        # script must still be byte-for-byte identical to the released version.
        script = re.search(r'<script>(.*?)</script>', (ROOT / 'manhwa/read.html').read_text(), re.S).group(1)
        self.assertEqual(hashlib.sha256(script.encode()).hexdigest(), LEGACY_SCRIPT_SHA256)
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
