"""Browser tests against an intercepted contract fixture, not a live backend.

No production traffic, account creation, or real comments are used here.
"""
import copy
import json
from pathlib import Path
import unittest
from urllib.parse import parse_qs, urlparse

import test_series_reader as reader_fixture


def metrics(views=0, reads=0, likes=0, comments=0):
    return dict(page_views=views, reads=reads, likes=likes, comments=comments)


class EngagementTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        reader_fixture.ReaderTests.setUpClass.__func__(cls)

    @classmethod
    def tearDownClass(cls):
        reader_fixture.ReaderTests.tearDownClass.__func__(cls)

    def setUp(self):
        reader_fixture.ReaderTests.setUp(self)
        self.api_requests = []
        self.events = {}
        self.votes = set()
        self.pending = {}
        self.items = []
        self.fail_summary = False
        self.bad_policy = False
        self.fail_next_event_response = False
        self.fail_next_comment_response = False
        self.fail_next_like_response = False
        self.summary_data = {
            'schema_version': 1, 'series': 'test-series',
            'since': '2026-10-18T00:00:00Z', 'updated_at': '2026-10-18T01:00:00Z',
            'comments_policy': 'premoderated', 'likes_policy': 'browser-token',
            'direct': metrics(), 'chapters': {'1': metrics(), '2': metrics()},
        }
        self.page.route('**/engagement/config.json', lambda route: route.fulfill(
            content_type='application/json', body=json.dumps({'apiBase': 'https://engagement.test/v1/'})))
        self.page.route('https://engagement.test/v1/**', self.api)

    load = reader_fixture.ReaderTests.load

    def api(self, route):
        request = route.request
        path = urlparse(request.url).path.rsplit('/', 1)[-1]
        query = parse_qs(urlparse(request.url).query)
        body = request.post_data_json if request.post_data else None
        self.api_requests.append((request.method, path, body, request.headers))
        headers = {'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Headers': 'Content-Type', 'Access-Control-Allow-Methods': 'GET,POST,PUT,OPTIONS'}
        def reply(data, status=200):
            route.fulfill(status=status, content_type='application/json', headers=headers, body=json.dumps(data))
        if request.method == 'OPTIONS':
            return reply({})
        if path == 'summary':
            if self.fail_summary:
                return reply({}, 503)
            data = copy.deepcopy(self.summary_data)
            if self.bad_policy:
                data['comments_policy'] = 'unmoderated'
            return reply(data)
        if path == 'events':
            if body['event_id'] not in self.events:
                self.events[body['event_id']] = body
                target = self.summary_data['direct'] if body['chapter'] is None else self.summary_data['chapters'][str(body['chapter'])]
                target['page_views' if body['type'] == 'page_view' else 'reads'] += 1
            if self.fail_next_event_response:
                self.fail_next_event_response = False
                return route.abort()
            return reply({'accepted': True})
        if path == 'likes':
            target = self.summary_data['direct'] if body['chapter'] is None else self.summary_data['chapters'][str(body['chapter'])]
            vote = (body['series'], body['chapter'], body['client_id'])
            if body['liked'] and vote not in self.votes:
                self.votes.add(vote)
                target['likes'] += 1
            if not body['liked'] and vote in self.votes:
                self.votes.remove(vote)
                target['likes'] -= 1
            if self.fail_next_like_response:
                self.fail_next_like_response = False
                return route.abort()
            return reply({'liked': body['liked'], 'metrics': target})
        if path == 'comments' and request.method == 'POST':
            self.pending.setdefault(body['request_id'], body)
            if self.fail_next_comment_response:
                self.fail_next_comment_response = False
                return route.abort()
            return reply({'status': 'pending'}, 202)
        if path == 'comments':
            return reply({'items': self.items, 'next_cursor': None})
        return reply({}, 404)

    def enabled(self):
        self.page.wait_for_function("document.querySelector('.engagement > button')?.disabled === false")

    def no_errors_or_overflow(self):
        self.assertFalse(self.errors)
        self.assertFalse(self.page.evaluate('document.documentElement.scrollWidth > innerWidth'))

    def test_no_backend_does_not_write_or_transmit_engagement_data(self):
        self.page.route('**/engagement/config.json', lambda route: route.fulfill(content_type='application/json', body='{"apiBase":null}'))
        self.load()
        self.page.get_by_text('Shared stats and comments are not connected yet.', exact=False).wait_for()
        self.assertEqual(self.page.locator('.eng-metrics dd').all_text_contents(), ['—'] * 4)
        self.assertTrue(self.page.get_by_role('button', name='Like this chapter', exact=True).is_disabled())
        self.assertTrue(self.page.get_by_role('button', name='Submit for review').is_disabled())
        self.assertEqual(self.api_requests, [])
        self.assertEqual(self.page.evaluate("[...Object.keys(localStorage),...Object.keys(sessionStorage)].filter(k=>k.startsWith('manhwa:engagement:'))"), [])
        self.assertTrue(self.page.locator('#reader').is_visible())
        self.no_errors_or_overflow()

    def test_zero_is_real_when_service_explicitly_returns_zero(self):
        self.load()
        self.enabled()
        self.assertEqual(self.page.locator('.eng-metrics dd').all_text_contents()[1:], ['0', '0', '0'])
        self.assertIn('No approved comments yet', self.page.locator('.engagement').inner_text())
        self.assertIn('Earlier history is unavailable', self.page.locator('.engagement').inner_text())
        self.no_errors_or_overflow()

    def test_reload_and_lost_view_response_reuse_event_id(self):
        self.fail_next_event_response = True
        self.load()
        self.enabled()
        self.page.wait_for_function("Object.keys(sessionStorage).some(k=>k.includes(':event:'))")
        self.page.wait_for_timeout(100)
        self.assertEqual(len(self.events), 1)
        self.load()
        self.enabled()
        self.page.wait_for_function("Object.keys(sessionStorage).filter(k=>k.includes(':event:')).some(k=>JSON.parse(sessionStorage[k]).done)")
        sent = [body for method, path, body, _ in self.api_requests if path == 'events' and body]
        self.assertEqual(len(sent), 2)
        self.assertEqual(sent[0]['event_id'], sent[1]['event_id'])
        self.load()
        self.enabled()
        self.assertEqual(len([body for method, path, body, _ in self.api_requests if path == 'events' and body]), 2)
        self.assertEqual(self.summary_data['chapters']['1']['page_views'], 1)
        self.assertEqual(self.summary_data['chapters']['1']['reads'], 0)
        self.no_errors_or_overflow()

    def test_likes_are_confirmed_by_server_and_scoped_to_target(self):
        self.load()
        self.enabled()
        like = self.page.locator('.engagement > button').first
        like.click()
        self.page.wait_for_function("document.querySelector('.engagement > button').getAttribute('aria-pressed')==='true'")
        self.assertEqual(self.page.locator('.eng-metrics dd').nth(2).inner_text(), '1')
        client_id = next(iter(self.votes))[2]
        self.load()
        self.enabled()
        self.assertEqual(like.get_attribute('aria-pressed'), 'true')
        like.click()
        self.page.wait_for_function("document.querySelector('.engagement > button').getAttribute('aria-pressed')==='false'")
        self.assertEqual(len(self.votes), 0)
        self.load('?series=test-series')
        self.enabled()
        self.page.locator('.engagement > button').first.click()
        self.page.wait_for_function("document.querySelector('.engagement > button').getAttribute('aria-pressed')==='true'")
        self.assertEqual(self.votes, {('test-series', None, client_id)})
        self.assertEqual(self.summary_data['chapters']['1']['likes'], 0)
        self.no_errors_or_overflow()

    def test_comments_plain_text_pending_limits_and_duplicate_retry(self):
        attack = '<img src=x onerror="window.injected=true">'
        self.items = [{'id': 'safe-id', 'name': '<script>bad</script>', 'text': attack, 'created_at': '2026-10-18T00:00:00Z', 'status': 'approved'}]
        self.load()
        self.enabled()
        self.assertEqual(self.page.locator('.eng-comments p').inner_text(), attack)
        self.assertEqual(self.page.locator('.eng-comments img,.eng-comments script').count(), 0)
        self.assertFalse(self.page.evaluate('Boolean(window.injected)'))
        textarea = self.page.locator('.eng-form textarea')
        self.assertEqual(textarea.get_attribute('maxlength'), '1000')
        textarea.fill('https://one.test https://two.test https://three.test')
        self.page.get_by_role('button', name='Submit for review').click()
        self.assertEqual(len(self.pending), 0)
        self.assertIn('at most two links', self.page.locator('.eng-form').inner_text())
        self.fail_next_comment_response = True
        textarea.fill('A test-only comment.')
        self.page.get_by_role('button', name='Submit for review').click()
        self.page.get_by_text('Failed to fetch', exact=False).wait_for()
        self.assertEqual(len(self.pending), 1)
        self.load()
        self.enabled()
        textarea.fill('A test-only comment.')
        self.page.get_by_role('button', name='Submit for review').click()
        self.page.get_by_text('Submitted for owner review.', exact=False).wait_for()
        self.assertEqual(len(self.pending), 1)
        posts = [body for method, path, body, _ in self.api_requests if path == 'comments' and method == 'POST']
        self.assertEqual(posts[0]['request_id'], posts[1]['request_id'])
        self.assertEqual(self.page.locator('.eng-comments li').count(), 1)
        self.assertEqual(self.summary_data['chapters']['1']['comments'], 0)
        textarea.fill('Another test-only comment.')
        self.page.get_by_role('button', name='Submit for review').click()
        self.assertEqual(len(self.pending), 1)
        self.assertIn('wait a minute', self.page.locator('.eng-form').inner_text())
        self.no_errors_or_overflow()

    def test_like_retry_after_lost_response_reuses_token_and_desired_state(self):
        self.load()
        self.enabled()
        self.fail_next_like_response = True
        like = self.page.locator('.engagement > button').first
        like.click()
        self.page.get_by_text('Failed to fetch', exact=False).wait_for()
        self.assertEqual(like.get_attribute('aria-pressed'), 'false')
        self.assertEqual(self.summary_data['chapters']['1']['likes'], 1)
        like.click()
        self.page.wait_for_function("document.querySelector('.engagement > button').getAttribute('aria-pressed')==='true'")
        self.assertEqual(self.summary_data['chapters']['1']['likes'], 1)
        requests = [body for method, path, body, _ in self.api_requests if path == 'likes' and method == 'PUT']
        self.assertEqual(requests[0], requests[1])
        self.no_errors_or_overflow()

    def test_read_retry_retains_original_evidence(self):
        self.load()
        self.enabled()
        self.page.wait_for_function("Object.keys(sessionStorage).filter(k=>k.includes(':event:')).some(k=>JSON.parse(sessionStorage[k]).done)")
        self.fail_next_event_response = True
        script = """async seconds => {
          const {getClient, trackEvent} = await import('/manhwa/engagement/client.js');
          return trackEvent(await getClient(), {series:'test-series',chapter:1}, 'chapter_read',
            {visible_seconds:seconds,coverage:.9,bottom_seen:true});
        }"""
        self.assertFalse(self.page.evaluate(script, 30))
        self.assertTrue(self.page.evaluate(script, 45))
        attempts = [body for method, path, body, _ in self.api_requests if path == 'events' and body and body['type'] == 'chapter_read']
        self.assertEqual(len(attempts), 2)
        self.assertEqual(attempts[0], attempts[1])
        self.assertEqual(self.summary_data['chapters']['1']['reads'], 1)
        self.no_errors_or_overflow()

    def test_backend_failure_and_wrong_moderation_policy_disable_actions(self):
        self.fail_summary = True
        self.load()
        self.page.get_by_text('The shared service is unavailable.', exact=False).wait_for()
        self.assertEqual(self.page.locator('.eng-metrics dd').all_text_contents(), ['—'] * 4)
        self.assertTrue(self.page.get_by_role('button', name='Submit for review').is_disabled())
        self.fail_summary = False
        self.page.get_by_role('button', name='Refresh shared data').click()
        self.enabled()
        self.bad_policy = True
        self.page.get_by_role('button', name='Refresh shared data').click()
        self.page.get_by_text('The shared service returned an unsupported response.').wait_for()
        self.assertTrue(self.page.get_by_role('button', name='Submit for review').is_disabled())
        self.no_errors_or_overflow()

    def test_missing_chapter_counts_are_unavailable_not_zero(self):
        del self.summary_data['chapters']['2']
        self.load('?series=test-series')
        self.page.get_by_text('Some chapter statistics are unavailable.').wait_for()
        self.assertEqual(self.page.locator('.eng-metrics dd').all_text_contents(), ['—'] * 4)
        self.assertEqual(self.page.locator('.eng-row').all_text_contents(), ['Shared stats unavailable'] * 2)
        self.no_errors_or_overflow()

    def test_series_aggregates_are_not_unique_readers(self):
        self.summary_data['direct'] = metrics(views=4, likes=1, comments=2)
        self.summary_data['chapters'] = {'1': metrics(views=3, reads=2, likes=4, comments=1), '2': metrics(views=2, reads=1, likes=2, comments=0)}
        self.load('?series=test-series')
        self.enabled()
        self.page.wait_for_function("Object.keys(sessionStorage).filter(k=>k.includes(':event:')).some(k=>JSON.parse(sessionStorage[k]).done)")
        self.page.get_by_role('button', name='Refresh shared data').click()
        self.enabled()
        self.assertEqual(self.page.locator('.eng-metrics dd').all_text_contents(), ['10', '3', '7', '3'])
        self.assertIn('Like this series · 1', self.page.locator('.engagement').inner_text())
        self.assertIn('3 views · 2 reads · 4 likes · 1 comments', self.page.locator('.eng-row').all_text_contents())
        self.no_errors_or_overflow()

    def test_background_time_and_failed_images_do_not_qualify_reads(self):
        self.page.clock.install()
        self.page.add_init_script("window.qaHidden = true; Object.defineProperty(document,'visibilityState',{get:()=>window.qaHidden?'hidden':'visible',configurable:true})")
        self.load()
        self.enabled()
        self.page.wait_for_function("[...document.querySelectorAll('#strip img')].every(i=>i.complete && i.naturalWidth)")
        self.page.clock.run_for(60000)
        self.assertEqual(self.events, {})
        self.page.evaluate("window.qaHidden=false; document.dispatchEvent(new Event('visibilitychange'))")
        for y in range(0, 1900, 250):
            self.page.evaluate('(y)=>scrollTo(0, document.querySelector("#strip").offsetTop+y)', y)
            self.page.clock.run_for(1000)
        self.assertEqual(self.summary_data['chapters']['1']['reads'], 0)
        # An image that failed to load must prevent qualification even with time.
        self.page.route('**/manhwa/series/test-series/ch/001/001.webp', lambda route: route.fulfill(status=404))
        self.load()
        self.enabled()
        self.page.evaluate("window.qaHidden=false; document.dispatchEvent(new Event('visibilitychange'))")
        for y in range(0, 1900, 250):
            self.page.evaluate('(y)=>scrollTo(0, document.querySelector("#strip").offsetTop+y)', y)
            self.page.clock.run_for(10000)
        self.assertEqual(self.summary_data['chapters']['1']['reads'], 0)
        self.no_errors_or_overflow()

    def test_honeypot_and_unapproved_response_are_rejected(self):
        self.items = [{'id': 'pending-id', 'name': 'Reader', 'text': 'Must not be public', 'created_at': '2026-10-18T00:00:00Z', 'status': 'pending'}]
        self.load()
        self.enabled()
        self.page.get_by_text('Comments could not be loaded safely.').wait_for()
        self.assertEqual(self.page.locator('.eng-comments li').count(), 0)
        self.page.locator('.eng-form textarea').fill('Test-only body')
        self.page.locator('input[name=website]').evaluate('(input)=>input.value="spam"')
        self.page.get_by_role('button', name='Submit for review').click()
        self.assertEqual(self.pending, {})
        self.assertIn('Submission could not be accepted', self.page.locator('.eng-form').inner_text())
        self.no_errors_or_overflow()

    def test_unsafe_api_configuration_is_never_contacted(self):
        self.page.route('**/engagement/config.json', lambda route: route.fulfill(content_type='application/json', body='{"apiBase":"https://secret@engagement.test/v1/"}'))
        self.load()
        self.page.get_by_text('Shared service settings are invalid.').wait_for()
        self.assertEqual(self.api_requests, [])
        self.assertTrue(self.page.get_by_role('button', name='Submit for review').is_disabled())
        self.no_errors_or_overflow()

    def test_owner_aggregates_and_partial_failures_withhold_overall_total(self):
        self.page.route('**/engagement/catalog.json', lambda route: route.fulfill(content_type='application/json', body=json.dumps([
            {'slug': 'test-series', 'title': 'QA fixture', 'manifest': '../series/test-series/series.json', 'url': '../series/?series=test-series'},
            {'slug': 'second-series', 'title': 'Second QA fixture', 'manifest': '../series/second-series/series.json', 'url': '../series/?series=second-series'}
        ])))
        self.page.route('**/series/second-series/series.json', lambda route: route.fulfill(content_type='application/json', body=json.dumps(self.manifest)))
        self.summary_data['direct'] = metrics(views=4, likes=1, comments=2)
        self.summary_data['chapters'] = {'1': metrics(views=3, reads=2, likes=4, comments=1), '2': metrics(views=2, reads=1, likes=2, comments=0)}
        def summary_route(route):
            series = parse_qs(urlparse(route.request.url).query)['series'][0]
            data = copy.deepcopy(self.summary_data)
            data['series'] = series
            route.fulfill(status=503 if series == 'second-series' and self.fail_summary else 200, content_type='application/json', body=json.dumps(data))
        self.page.route('https://engagement.test/v1/summary?*', summary_route)
        self.page.goto(self.origin + '/manhwa/owner.html')
        self.page.get_by_text('Shared data loaded for all published series.').wait_for()
        self.assertEqual(self.page.locator('#overview-totals dd').all_text_contents(), ['18', '6', '14', '6'])
        self.assertEqual(self.page.locator('.eng-series').count(), 2)
        self.assertEqual(self.page.locator('.eng-chapter').count(), 4)
        self.assertFalse(any(path == 'events' for _, path, _, _ in self.api_requests))
        self.fail_summary = True
        self.page.get_by_role('button', name='Refresh shared data').click()
        self.page.get_by_text('Some shared data is unavailable.', exact=False).wait_for()
        self.assertEqual(self.page.locator('#overview-totals dd').all_text_contents(), ['—'] * 4)
        self.assertEqual(self.page.locator('.eng-series').nth(0).locator('td').all_text_contents()[1:], ['9', '3', '7', '3'])
        self.assertEqual(self.page.locator('.eng-series').nth(1).locator('td').all_text_contents()[1:], ['—'] * 4)
        self.no_errors_or_overflow()

    def test_qualified_read_needs_time_coverage_and_visible_end(self):
        self.page.clock.install()
        self.load()
        self.enabled()
        self.page.wait_for_function("[...document.querySelectorAll('#strip img')].every(i=>i.complete && i.naturalWidth)")
        self.page.locator('#endnav').scroll_into_view_if_needed()
        self.page.clock.run_for(31000)
        self.assertEqual(self.summary_data['chapters']['1']['reads'], 0, 'Jumping to end must not count a read')
        # Expose overlapping slices of the actual loaded pages, including their end.
        self.page.evaluate("scrollTo(0, document.querySelector('#strip').offsetTop)")
        self.page.clock.run_for(16000)
        for y in range(0, 1900, 250):
            self.page.evaluate('(y)=>scrollTo(0, document.querySelector("#strip").offsetTop+y)', y)
            self.page.clock.run_for(3000)
        self.page.wait_for_function("Object.keys(sessionStorage).some(k=>k.endsWith(':chapter_read') && JSON.parse(sessionStorage[k]).done)")
        self.assertEqual(self.summary_data['chapters']['1']['reads'], 1)
        self.assertEqual(len([e for e in self.events.values() if e['type'] == 'chapter_read']), 1)
        self.page.clock.run_for(60000)
        self.assertEqual(self.summary_data['chapters']['1']['reads'], 1)
        read = next(e for e in self.events.values() if e['type'] == 'chapter_read')
        self.assertGreaterEqual(read['evidence']['visible_seconds'], 30)
        self.assertGreaterEqual(read['evidence']['coverage'], .8)
        self.assertEqual(set(read) - {'evidence'}, {'event_id', 'session_id', 'series', 'chapter', 'type'})
        self.no_errors_or_overflow()

    def test_blocked_storage_keeps_reader_and_shared_counts_usable(self):
        self.page.add_init_script("Object.defineProperty(window,'localStorage',{get(){throw Error('blocked')}}); Object.defineProperty(window,'sessionStorage',{get(){throw Error('blocked')}})")
        self.load()
        self.enabled()
        self.page.get_by_role('button', name='Like this chapter', exact=False).click()
        self.page.get_by_text('Browser storage is unavailable.', exact=False).wait_for()
        self.assertEqual(self.votes, set())
        self.assertEqual(self.events, {})
        self.assertTrue(self.page.locator('#reader').is_visible())
        self.no_errors_or_overflow()

    def test_legacy_additive_integration_and_typing_does_not_navigate(self):
        root = Path(__file__).resolve().parents[1]
        legacy = json.loads((root / 'manhwa/data/chapters.json').read_text())['chapters']
        self.summary_data['series'] = 'the-lord-who-measured-zero'
        self.summary_data['chapters'] = {str(ch['n']): metrics() for ch in legacy}
        self.page.goto(self.origin + '/manhwa/read.html?ch=1')
        self.enabled()
        self.page.locator('.eng-form textarea').fill('test')
        self.page.keyboard.press('ArrowRight')
        self.page.keyboard.press('ArrowLeft')
        self.assertTrue(self.page.url.endswith('?ch=1'))
        self.assertTrue(self.page.locator('#player').is_visible())
        self.page.goto(self.origin + '/manhwa/')
        self.enabled()
        self.assertEqual(self.page.locator('.eng-row').count(), len(legacy))
        self.assertFalse(self.page.locator('.engagement details').evaluate('(el)=>el.open'))
        self.no_errors_or_overflow()

    def test_owner_lists_only_published_content_and_is_not_tracked(self):
        self.page.route('**/engagement/config.json', lambda route: route.fulfill(content_type='application/json', body='{"apiBase":null}'))
        self.page.goto(self.origin + '/manhwa/owner.html')
        self.page.get_by_text('Shared stats and comments are not connected yet.', exact=False).wait_for()
        self.assertEqual(self.page.locator('.eng-series').count(), 2)
        root = Path(__file__).resolve().parents[1]
        catalog_path = root / 'manhwa/engagement/catalog.json'
        expected = sum(len(json.loads((catalog_path.parent / item['manifest']).read_text())['chapters']) for item in json.loads(catalog_path.read_text()))
        self.assertEqual(self.page.locator('.eng-chapter').count(), expected)
        self.assertEqual(self.page.locator('#overview-totals dd').all_text_contents(), ['—'] * 4)
        self.assertEqual(self.api_requests, [])
        self.assertIn('no administrative access', self.page.locator('main').inner_text())
        self.no_errors_or_overflow()


if __name__ == '__main__':
    unittest.main()
