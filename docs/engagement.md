# Manhwa engagement integration

Backend setup is currently deferred at the owner's request. The prepared
frontend remains disabled. See the [continuation checkpoint](engagement-checkpoint.md)
before resuming this work.

## Current state and release boundary

Inspected 2026-10-18 against remote `main` at
`6f9576ec3a96590c0b9f491622a1c75c2a7d0dc7`.
The repository is a static GitHub Pages site. It has the original reader under
`/manhwa/` and a separate manifest-driven reader under `/manhwa/series/`.
There is no configured analytics script, database, comment provider, authentication
service, or server endpoint in the tracked source. Existing `lwmz-*` and
`manhwa:<slug>:*` localStorage keys hold personal reading progress only.
They provide no shared counts or historical readership data.

The engagement frontend supports both readers, both chapter lists, and
`/manhwa/owner.html`. `engagement/catalog.json` lists only the two already
published series. Chapters are read from their existing public manifests;
no story inputs, planned chapters, or new releases are included.
The original reader's inline script is unchanged, including audio and Follow.
The existing browser test protects that script with its original SHA-256.

`manhwa/engagement/config.json` deliberately contains `{"apiBase": null}`.
With this configuration there are **no engagement service requests, tracking
IDs, local engagement counters, votes, or comment submissions**. Counts display
an em dash and an explanation; actions are disabled. Browser progress still works.
Real zeroes appear only when a configured service explicitly returns zero.
No historical counts can be reconstructed from the repository.

This change prepares a frontend and a service contract. **It does not implement
or provision a backend.** Browser tests use intercepted, test-only responses.
Their passing does not establish working production counters, moderation,
database isolation, or server-side duplicate protection.

See the [concrete Supabase setup proposal](supabase-setup.md) for current official
terms/plan references, exact data fields, owner approvals, and security gaps.
It specifies a required signed-session extension before bounded-retention
activation; the current random-UUID contract alone cannot prevent old replays
after its deduplication rows have been deleted.

## Metric definitions

| Metric | Definition |
| --- | --- |
| Page view | A visible series page or chapter page opening, accepted at most once for that target per tab measurement session, lasting at most 24 hours. Refreshes and response retries in that session reuse the event. This is a deduplicated page-opening measure, not every HTTP request. |
| Chapter read | At least 30 seconds with loaded artwork visible in the foreground, at least 80% of total rendered image height exposed cumulatively, and the bottom of the final image seen. Gaps between images do not contribute. All chapter images must load successfully. Follow scrolling can qualify. |
| Like | An active vote for one series page or one chapter from a random browser token. Repeating `liked: true` cannot add another vote for that token and target. The reader may undo the vote. |
| Comment | A publicly approved comment for that target. Pending, rejected, spam, and deleted comments are excluded. |
| Series aggregate | Direct series-page views/likes/comments plus the corresponding chapter values. Reads are the sum of chapter reads. A reader visiting three chapters can contribute three reads. |
| Owner totals | Sum of series aggregates across every registered published series. Withheld if any series is unavailable. Do not sum both aggregate rows and their chapter rows. |

These measures never claim unique readers or unique people. Session storage can
be cleared, tabs duplicated, and tokens reset; shared browsers and multiple
devices also prevent a person-level interpretation. Browsers or bots can forge
client events. The frontend does not prove attention, identity, or human traffic.
Missing storage disables recording and mutations that need reliable IDs; it
does not replace IDs with fingerprints or invent local analytics.

The read observer excludes the sticky navigation/narration and fixed original
player from the visible area. It counts foreground visibility, not window focus.
It stores the union of exposed vertical intervals only in memory. It does not
send scroll trails, image coordinates, audio history, URLs, referrers, email,
user-agent strings, screen characteristics, or existing reading-progress keys.
The read event contains only coarse qualification evidence (seconds, coverage,
and a boolean). A failed/unacknowledged read may be lost if the page closes;
there is no persistent offline queue or retrospective backfill.

## Frontend REST contract (version 1)

After the parent coordinates service approval, implement and test this contract,
then set `apiBase` to its HTTPS base URL, with no query, fragment, or credentials.
For example, an approved Edge Function might have a base URL ending in
`/functions/v1/manhwa-engagement/`. No third-party JavaScript SDK is required.
All fetches omit cookies and referrers. Do not put service keys, database
passwords, GitHub tokens, or owner credentials in this repository or config.

The server must allow CORS only for the production site origin and explicitly
approved test origins. Support `OPTIONS`, `GET`, `POST`, `PUT`, and
`Content-Type: application/json`. Origin checks are not authentication and do
not prevent non-browser abuse. Use HTTPS, bounded request bodies (e.g. 8 KiB),
appropriate rate limits, and non-sensitive error responses. Return JSON,
`Cache-Control: no-store`, and HTTP 429 with `Retry-After` when throttled.
Do not enable any endpoint before its mandatory server protections are tested.

### GET summary?series=<slug>

Return an explicit object for **every currently published chapter**, using
chapter numbers as keys. Missing keys are unavailable, never implicit zeroes.
Numbers must be nonnegative JavaScript safe integers. `direct.reads` is always
zero. `direct` refers only to the series page; chapter values are not included
in it. Include the actual start of measurement and snapshot time in ISO 8601.
The example below is a new, empty test dataset, not historical site data:

```json
{
  "schema_version": 1,
  "series": "example-published-series",
  "since": "2026-10-18T00:00:00Z",
  "updated_at": "2026-10-18T00:00:00Z",
  "comments_policy": "premoderated",
  "likes_policy": "browser-token",
  "direct": {"page_views": 0, "reads": 0, "likes": 0, "comments": 0},
  "chapters": {
    "1": {"page_views": 0, "reads": 0, "likes": 0, "comments": 0}
  }
}
```

Use a consistent database snapshot. Do not silently omit chapters on partial
failure. Do not return tokens, session IDs, moderation records, or raw events.
The owner overview uses the same public summaries; it is a convenience view,
not a security boundary or an authenticated administration panel. It records
no visits. Private owner moderation stays in the service's authenticated
dashboard. `noindex` is advisory, not access control.

### POST events

```json
{
  "event_id": "<UUID v4>",
  "session_id": "<UUID v4>",
  "series": "<published slug>",
  "chapter": 1,
  "type": "chapter_read",
  "evidence": {"visible_seconds": 30, "coverage": 0.85, "bottom_seen": true}
}
```

For `page_view`, omit `evidence`. `chapter: null` denotes a series-page view.
Reject `chapter_read` with a null chapter or invalid evidence. Server validation
of evidence is a sanity check; it cannot prove a human read the page.
Reject unknown fields and unknown/unpublished targets. Never fetch arbitrary
client-provided paths or URLs. Use the server's receive time, not a client date.

Return `{"accepted": true}` only after durable acceptance (or for a duplicate
already durably accepted). In one transaction, enforce both unique `event_id`
and unique `(session_id, series, target, type)` for a 24-hour server-bounded
session. Reject reuse of an ID with a different payload. Do not increment a
counter on conflict. Use a non-null target key such as `series` or `chapter:1`;
SQL nullable uniqueness must not let series-page duplicates through. Bound a
session's lifetime from its first server acceptance, reject expired IDs, and
retain deduplication keys beyond that period to prevent replay.

The browser stores session/event IDs in sessionStorage only when connected.
An accepted event is not sent on reload. After a lost response, the same event
ID is retried on a subsequent eligible visit. Concurrent calls within a page
are guarded. The server must still enforce uniqueness across tabs, concurrent
requests, retries, and direct clients. No count is increased optimistically in
the frontend; use Refresh shared data to load a newer snapshot.

### PUT likes

Request:

```json
{"series":"<published slug>","chapter":1,"client_id":"<UUID v4>","liked":true}
```

Use null for a series-page vote. Upsert/delete a vote atomically under unique
`(series, target, client_token_hash)`. Return the confirmed state and current
**direct target** metrics:

```json
{"liked":true,"metrics":{"page_views":1,"reads":0,"likes":1,"comments":0}}
```

Use a server-secret HMAC of the random token for storage; do not return it.
The browser generates its token only on an explicit like/post action and keeps
only the token and last confirmed liked state locally. Local state is a UI
hint, not a counter or a server authorization rule. Retrying an ambiguous
successful `liked:true` is idempotent. Clearing browser storage loses the
ability to undo the old vote and permits another vote. This intentionally
offers no one-person-one-vote guarantee. If votes are later reset on the
server, clear/version the corresponding browser-state namespace too.

### GET comments?series=<slug>&chapter=<number|series>[&cursor=<opaque>]

Return newest approved comments first, at most 20 per page:

```json
{
  "items": [{"id":"<opaque>","name":"Reader","text":"Plain text only.","created_at":"2026-10-18T00:00:00Z","status":"approved"}],
  "next_cursor": null
}
```

Opaque cursors are null or 1–200 characters, IDs at most 100 characters. Never
return pending/rejected content or tokens from this endpoint. The frontend
validates each item, deduplicates page IDs, and renders name/body with
`textContent`, preserving line breaks. It never parses Markdown/HTML,
auto-links text, or loads user-controlled avatars/media.

### POST comments

```json
{"series":"<published slug>","chapter":1,"client_id":"<UUID v4>","request_id":"<UUID v4>","name":"","text":"Plain text only.","website":""}
```

Return `{"status":"pending"}` with HTTP 202 only after durable insertion or
idempotent replay. Enforce unique `(client_token_hash, request_id)` with
payload consistency. The client keeps an in-progress ID and a content digest
in sessionStorage so a lost response followed by a reload can retry safely;
it does not store comment text there. A successful submission never appears
in the public list or increases the approved-comment total before moderation.

Mandatory server controls, not just frontend checks:

- Trim and validate a nonempty body of at most 1,000 UTF-16 code units and an
  optional display name of at most 40; reject disallowed control characters.
  Bound raw JSON bytes too. Store/render text, never HTML.
- Reject a nonempty honeypot (`website`) and more than two link-like strings
  (`http://`, `https://`, `www.`). These checks reduce noise; they are not the
  only spam protection.
- Rate limit new comments to at most one per token per minute and e.g. ten per
  day. Allow idempotent retries to return their previous acknowledgement.
  Add bounded per-network abuse limits for token-reset spam, using short-lived
  server-secret HMAC buckets, without retaining raw IPs or fingerprinting.
  Document the retention before activation. Return 429 for rejected new posts.
- Every new post starts pending. Only an authenticated owner may approve,
  reject, mark spam, or delete. Anonymous callers cannot choose status, edit
  timestamps, moderate content, enumerate pending IDs, or edit others' posts.
- Count only approved, nondeleted posts. Status changes and aggregate counts
  must be transactional (or query the authoritative rows directly).

Client cooldown and input limits improve usability, but are bypassable. They
are never described as server-side moderation or abuse protection.

## Recommended minimum backend, pending parent approval

Use **one Supabase project with Postgres and one Edge Function implementing
the contract above**. Keep Pages hosting and all existing assets unchanged.
Supabase is a proposed new integration, not a discovered existing service.
No project, account, token, credential, subscription, or persistent grant has
been created. No visitor data has been sent to it.

Suggested schema and constraints:

| Table | Contents and essential constraints |
| --- | --- |
| `published_targets` | Approved series/target keys imported only from current public manifests. Primary key `(series, target)`; no story-source import. |
| `measurement_sessions` | Random session ID, server first-seen and expiry; 24-hour maximum. |
| `engagement_events` | Event ID primary key, session, target FK, type, server timestamp. Unique `(session_id, series, target, type)`; no nullable target. No scroll trail. |
| `engagement_votes` | Target FK and HMAC browser token, composite unique key. One row means one active vote. |
| `engagement_comments` | Opaque ID, target FK, HMAC token, request ID, plain name/text, pending/approved/rejected/spam/deleted status, timestamps. Unique `(token_hash, request_id)`. Retain a payload digest for replay validation. |
| `engagement_rate_limits` | Atomic token and rotating network-HMAC buckets with bounded expiry; no raw IP storage. |

Keep table access server-side. Enable RLS on exposed tables, revoke all access
from `anon`/ordinary `authenticated` roles unless explicitly justified, and do
not expose private rows through unsafe views. The Edge Function holds the
service credential in server secrets and calls transactional SQL routines.
Public endpoints are deliberately callable without visitor accounts; protect
them with validation, allowlists, rate limits, and DB constraints. Owner
moderation can initially use Supabase's authenticated project dashboard;
never put a service-role key into the static owner page. Use a moderation
audit record/trigger and retain rejected/spam posts only as long as necessary.

Proposed retention for approval: raw event/dedup/session rows for 30 days,
daily target aggregates retained for history, rate-limit buckets at most 24
hours (network buckets rotate every 10 minutes), rejected/spam comments for
30 days, and approved comments/active votes until deletion. Expired session
IDs must be rejected during and after aggregation, so old retries cannot
inflate totals. The current UI shows all-time totals since activation; do not
drop historical aggregate counts when expiring event rows. Configure minimal
provider logging and confirm its retention; don't promise that the provider
never receives a connection IP.

Supabase's official documentation describes the components underlying this
recommendation: [row-level security and grants](https://supabase.com/docs/guides/database/postgres/row-level-security),
[Edge Function authorization](https://supabase.com/docs/guides/functions/auth),
and [rate limiting](https://supabase.com/docs/guides/functions/examples/rate-limiting).
The rate-limiting example uses another service; this proposal keeps rate-limit
buckets in Postgres to avoid adding an extra vendor. Implement and load-test
the atomic routines; do not copy an example and assume it provides this API.
[GitHub Pages serves static files](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages),
so it cannot run these mutation endpoints by itself.

Parent decisions needed before activation:

1. Confirm an approved existing backend project, or authorize creating this
   proposed project, accepting its terms, region, budget, credentials and
   persistent service access. Confirm the owner account for moderation.
2. Approve sending the documented minimal event/token/comment payloads to
   that service and its retention/logging settings. Add a public privacy note
   naming the actual provider before enabling the endpoint.
3. Implement and verify the backend against this contract, including concurrent
   duplicate events/votes/posts, moderation isolation, forged targets, limits,
   safe public reads, expired IDs, and authenticated deletion. Frontend mocks
   cannot validate those guarantees.
4. Coordinate the release with ongoing content work: fetch current main,
   review/rebase the feature commit, then merge only the reviewed changes.
   A feature-branch push is not a Pages deployment. Main pushes/deployment
   require coordination with the parent. Never force-push over content work.

## Verification

Run in the saved cloud environment (Python, Pillow, Playwright, Chromium):

```bash
python3 -m unittest discover -s tools -p 'test_*.py'
git diff --check
```

Tests cover unavailable/real-zero states, response failure/recovery, policy
validation, scoped browser-token votes, no local engagement writes while
disabled, storage denial, text injection, pending comments, client limits,
stable comment retry IDs after reload, view retry/reload deduplication, read
time/coverage qualification, both readers, mobile overflow, owner totals, and
the original audio/Follow/release checks. Service responses and story fixtures
in tests are intercepted locally and never published as chapters.
