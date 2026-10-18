# Supabase setup proposal for owner approval

**Deferred at the owner's request.** This proposal is retained for a future
explicit resumption; it does not authorize setup or activation. See the
[continuation checkpoint](engagement-checkpoint.md).

Prepared 2026-10-18. This is a proposed service, not an existing configured
backend. Nothing here creates an account, accepts terms, installs secrets,
invites a collaborator, provisions a project, or deploys a function. The site
still has `apiBase: null`. Main is not changed by this preparation.
The existing [frontend contract](engagement.md) remains a prototype; the
session-ticket extension below is required before activating it with bounded
retention. No database migration or hosted backend has been tested or applied.

## Decisions the owner would approve

| Decision | Proposed minimum |
| --- | --- |
| Account and project | Use an owner-controlled Supabase account and one dedicated project. First confirm whether an approved existing backend is available instead. No shared password or new agent/service-user account is needed. |
| Plan | Free for an initial pilot only if its limits and inactivity pausing are acceptable; otherwise explicitly approve a paid plan and budget. No automatic upgrade, add-on, or paid spend is authorized. |
| Region | Owner chooses a listed database region appropriate to the audience and data requirements. Do not infer this from the user's timezone. |
| Moderation | Owner signs in to the Supabase project dashboard with MFA and reviews pending text before publishing. No reader accounts, email collection, social login, or public moderation endpoint in the minimum version. |
| Public data | Publish target totals and approved comment name/text/time only. The site's owner overview remains a public, read-only convenience page. |
| Processing | Send minimal event/session IDs and read evidence; send browser tokens only for explicit likes/comments. Owner approves Supabase as the new destination, the privacy notice, and the retention below. |
| Credentials | Approve project creation and server-side handling of its privileged function credential, database administration credential, and signing/HMAC secrets. Actual values stay in an owner vault and server secret store, never chat or the static repository. |
| Release | Backend implementation and security verification first. Parent coordinates any subsequent activation and main merge with current content work. This approval proposal is not deployment authorization. |

## Verified official terms and plan limits

Checked public official pages on 2026-10-18; recheck before signup or purchase.
The account owner must review and accept the applicable agreement themselves.
Supabase's current [Terms of Service](https://supabase.com/terms) describe
acceptance by using the service, customer responsibility for security/backups
and rights to submitted data, and arbitration/class-action provisions. The
[Data Processing Addendum](https://supabase.com/legal/customer-resources/data-processing-addendum)
sets out customer/controller and Supabase/processor duties, including notices,
applicable consents and handling deletion requests. No terms have been accepted
on the user's behalf. Also review the [Privacy Policy](https://supabase.com/privacy)
and select an [available region](https://supabase.com/docs/guides/platform/regions).
A database region does not justify promising that all provider operations,
support, telemetry, or subprocessors stay exclusively in that location.

| Relevant item | Current official listing |
| --- | --- |
| Free | $0/month; two active projects; 500 MB database per project; 5 GB egress; 500,000 Edge Function invocations; pauses after one week of inactivity. |
| Free operational limits | Automatic backups and uptime SLA are not included; API/database log retention is listed as one day. |
| Pro | Starts at $25/month; includes 2 million function invocations, then listed function overage is $2/million. Compute, other usage, and optional add-ons can affect the bill. |

Sources: [pricing](https://supabase.com/pricing) and
[billing quotas](https://supabase.com/docs/guides/platform/billing-on-supabase).
Free is quota-limited, not unlimited-capacity hosting. Page opens cause several
function calls (summary, comments, a view, and sometimes a read); invocations
are not reader counts. Traffic and row sizes are unknown, so adequacy of Free
has not been established. Existing audio/images remain on Pages and are not
copied into Supabase Storage.

Pro's [spend cap](https://supabase.com/docs/guides/platform/cost-control) covers
only specified usage items; it excludes compute and several explicitly selected
add-ons and is not a configurable total-dollar budget. Keep it on if Pro is
approved, monitor the usage dashboard, and require separate approval for any
upgrade or add-on. Select a backup/export and recovery arrangement before
activation; do not imply that the Free plan includes managed recoverable backups.
[Backup documentation](https://supabase.com/docs/guides/platform/backups)

The documented [Edge Function limits](https://supabase.com/docs/guides/functions/limits)
include 256 MB memory, 2 seconds CPU per request, and a 150-second Free worker
wall-clock limit. Design short transactional requests rather than doing cleanup
or bulk scans in a visitor request. These are platform limits, not performance
guarantees for this unimplemented service.

## Concrete data model

Use server timestamps in UTC. `target` is a non-null string: `series` or
`chapter:<positive integer>`. API `chapter: null` maps to `series` at the edge;
do not rely on nullable SQL unique constraints. Every target must reference the
published allowlist. No unpublished titles, outlines, or source story files
are inputs to this database.

| Table | Proposed fields and constraints |
| --- | --- |
| `published_series` | `slug text PK`, `measurement_started_at timestamptz`, `enabled boolean`. Validate slug format and maximum 80 characters. Set the real activation time, never a fictional historical start. |
| `published_targets` | `series text FK`, `target text`, `chapter_number integer nullable`, `enabled boolean`; PK `(series,target)`. Series row has null chapter; chapter rows require a positive chapter and a matching target string. |
| `measurement_sessions` | `session_id uuid PK`, `issued_at timestamptz`, `expires_at timestamptz`; server-created ID and maximum 24-hour lifetime. Store no browser vote token, IP, user agent, or referrer. |
| `engagement_events` | `event_id uuid PK`, `session_id uuid FK`, target FK, `kind text` checked to `page_view`/`chapter_read`, `accepted_at timestamptz`, `payload_digest bytea`, optional `visible_seconds integer`, `coverage real`, `bottom_seen boolean`. Unique `(session_id,series,target,kind)`; reads require a chapter and valid evidence. |
| `target_daily_totals` | Target FK, `day date`, `page_views bigint`, `reads bigint`; PK `(series,target,day)` and nonnegative counts. Increment in the same transaction as first acceptance of an event. No session/token identifiers. Sum these durable rows for lifetime views/reads after raw events expire. |
| `engagement_votes` | Target FK, `token_hash bytea`, `created_at timestamptz`; PK `(series,target,token_hash)`. A row is an active vote. Count these rows rather than accepting a caller-supplied total. |
| `engagement_comments` | `id uuid PK`, target FK, `token_hash bytea`, `request_id uuid`, `request_expires_at timestamptz`, `payload_digest bytea`, `display_name text`, `body text`, `status text` checked to `pending/approved/rejected/spam/deleted`, `created_at/updated_at/moderated_at timestamptz`. Unique `(token_hash,request_id)`; pending is the database default. |
| `moderation_audit` | `id uuid PK`, `comment_id uuid`, `previous_status/new_status text`, `actor text`, `changed_at timestamptz`. Record the actual authorized actor where available, never label a generic database role as a verified individual. Keep comment bodies out of audit rows. |
| `engagement_rate_limits` | `purpose text`, `bucket_hash bytea`, `window_start/expires_at timestamptz`, `attempts integer`; composite PK for an atomic bucket. Separate token, session, and network namespaces. No raw IP. |

Store HMAC digests of browser tokens, using different domain prefixes for votes,
comments, and abuse buckets. Treat hashes as pseudonymous data, not anonymous
people. Function responses must not disclose hashes, raw tokens, session rows,
payload digests, rate-limit keys, or unapproved comments. The service inevitably
receives network metadata; the privacy notice must distinguish application
retention from provider logging.

## Public versus owner-only access

Public visitors use only the validated Edge Function routes in the contract.
The extra session route below issues a short-lived ticket; it grants no
administrative access. Public GETs expose totals and at most 20 approved
comments per page. Public writes can submit events, set their browser-token
vote state, or create a pending comment. They cannot select status, edit another
comment, enumerate pending posts, supply counts, or administer anything.

Keep raw tables inaccessible through the browser Data API. Enable RLS and
revoke grants from `PUBLIC`, `anon`, and ordinary `authenticated` as applicable.
Revoke default `PUBLIC` execution on mutation RPCs too; grant the server role
only the routines required. Use `SECURITY INVOKER` where possible, explicit
schemas/search paths, parameterized queries, and no dynamic SQL from payloads.
The privileged server key bypasses RLS: the handler and SQL routines must
validate independently of RLS. A leaked project key therefore has broad impact;
an isolated project reduces the blast radius. [RLS and grants](https://supabase.com/docs/guides/database/postgres/row-level-security)

The initial owner moderates through Supabase's authenticated dashboard, with
MFA on the owner's platform account. Pending comments, spam, audit rows, and
deletion operations remain there. Use a controlled moderation routine or a
trigger so dashboard changes update status/counts consistently and create an
audit entry. Dashboard administrative access is broader than comment moderation;
do not invite additional moderators or agent accounts as an incidental step.
Supabase documents that project-scoped dashboard roles are limited to Team and
Enterprise plans. [Access control](https://supabase.com/docs/guides/platform/access-control)

If narrower delegated moderation is later needed, design a separate authenticated
application route with a server-maintained allowlist of immutable Auth user IDs,
verified user JWTs, MFA enforcement and an audit trail. Reader Auth signups,
OAuth providers and SMTP are unnecessary for the proposed minimum version.
The static owner page must never be treated as authentication; `noindex` and
knowledge of its URL provide no access control.

## Server enforcement and abuse limits

Use one Edge Function router, with public routes deliberately configured for
unauthenticated access and no privileged route mixed into that public router.
Select the platform's documented public-function auth mode explicitly; a
publishable key is not proof of a reader identity. Never disable verification
on a future owner-only endpoint without implementing its own verified owner
authorization. [Function authorization](https://supabase.com/docs/guides/functions/auth)

Enforce an 8 KiB body limit while reading the stream, exact JSON types and
allowed fields, UUID/slug/target validity, server time, and the published target
FK. Reject oversized integers and sums before JSON serialization. Reject bad
methods, invalid pagination cursors and unknown paths. CORS allows only
`https://abafaboy.github.io` plus separately approved staging origins; it is
not an anti-bot control. Omit cookies, credentials and request bodies from logs.

Event acceptance, conflict checking and daily-total increments must be one
transaction. If an event ID already exists, compare its canonical payload digest;
different payloads conflict, identical retries acknowledge without incrementing.
The session/target/kind unique key prevents a different event ID from counting
the same event again. Votes use an idempotent upsert/delete under their composite
key. Comment request IDs must return the previous result on an identical retry,
before charging the new-comment cooldown. No endpoint accepts a numeric delta.

Proposed starting limits, to tune for shared networks during staging:

| Route | Limits checked atomically on the server |
| --- | --- |
| New comment | One/token/minute and ten/token/day; twenty/network/ten minutes. Reject a nonempty honeypot and more than two link-like strings. |
| Like | Thirty/token/minute; two hundred/network/ten minutes. Retrying the same desired state adds no vote. |
| Event | One/target/kind/session by DB constraint; 120/session/minute and 1,000/network/ten minutes as abuse ceilings. |
| Session issuance | Sixty/network/ten minutes. Tickets are random and expiring, not device fingerprints. |
| Public GET | Six hundred/network/ten minutes with bounded pages and indexed queries. |

Network buckets use a server-secret HMAC over a verified connection IP and
ten-minute window, expiring within twenty minutes; never accept an arbitrary
client-supplied forwarded-IP header as trustworthy. The actual trusted header
chain in hosted Supabase remains to be verified. Do not activate network limits
on an unverified header, or claim that token-reset spam is solved by token limits.
These are rate controls, not a guarantee of human traffic or one-person voting.
All new comments remain pending regardless of spam score. No CAPTCHA provider
or new data destination is included; an additional provider needs separate approval.

Apply name/body limits server-side too (40/1,000 UTF-16 code units), normalize
surrounding whitespace and reject disallowed controls. Escape nothing into SQL;
use parameters. Return only plain text fields and retain frontend `textContent`
rendering. Owner approval must never cause HTML interpretation.

## Retention and required replay protection

| Data | Proposed retention |
| --- | --- |
| Sessions, raw events and event dedup rows | Thirty days; session validity at most 24 hours. |
| Daily target totals | Retain without session/browser identifiers for historical totals until owner resets/deletes the series. |
| Active votes | Until undone or owner removal; explain token clearing/multiple-browser limitations. |
| Pending comments | Auto-expire after thirty days if not reviewed. |
| Approved comments | Until deletion; body/name never copied to application logs. |
| Rejected/spam/deleted comment bodies and names | Remove on rejection/deletion or expiry; retain only minimal request/digest tombstones up to thirty days for retry protection, subject to the chosen deletion policy. |
| Moderation audit | Ninety days, without copied body text. |
| Rate-limit buckets | Token daily buckets at most 48 hours, minute buckets within ten minutes, network buckets within twenty minutes. |
| Provider logs and backups | Confirm actual plan/project policy separately; application cleanup does not immediately erase provider logs or existing backups. |

Mandatory contract extension: **`POST sessions` returns a signed session ticket**
containing a server-issued UUID, issued-at, expiry (maximum 24 hours), and key ID.
`POST events` and `POST comments` must carry this ticket. Verify its signature,
audience, issuance bounds and expiry before touching counters or returning a
retry result; retain the original ticket with a pending client attempt. The
ticket must contain no IP, browser token, user agent or fingerprint. Reject
expired tickets, including after raw/dedup rows have been purged. Use a maintained
signing library and separate signing and token-HMAC secrets; retain verification
keys through all outstanding ticket lifetimes when rotating.

The current frontend generates a random session UUID locally and does **not**
implement this ticket exchange. A backend that merely deletes old UUID records
cannot distinguish an old replay from a new UUID after deletion. A finite
retention claim therefore requires this extension (or another reviewed expiring
credential design), not just a unique index. Do not activate the current
prototype with a claim of permanent replay protection after cleanup.

Comment idempotency is bounded by the original ticket's lifetime. After expiry,
the client must report an expired attempt and require an explicit new submission;
it must not silently attach a new ticket and re-post an ambiguous old request.
Do not retain deleted comment bodies indefinitely to solve idempotency. Purge
jobs must be transactional, indexed, and rerunnable; event totals have already
been incremented once and must not be dropped or incremented again by cleanup.

## Credential and activation sequence, after approval only

1. Owner confirms account, organization, plan, region, terms/privacy/DPA review,
   data processing and retention. Owner creates or selects the project and
   keeps database/admin credentials in their own vault. No GitHub app connection
   or OAuth grant is required for this architecture.
2. Implement the migration/routines, session extension and function in a local
   test environment, with ephemeral test values. Seed only the public target
   allowlist. Run the tests below before installing anything hosted.
3. Owner approves a bounded deployment session. Prefer an owner-run Dashboard
   deployment initially. CLI automation would require a personal access token;
   do not create, retain or grant that persistent access incidentally.
4. Approve access to the function's server-side project credential. Current
   [function secrets documentation](https://supabase.com/docs/guides/functions/secrets)
   describes `SUPABASE_SECRET_KEYS` and legacy `SUPABASE_SERVICE_ROLE_KEY`;
   both privileged forms bypass RLS. Use the supported server-side mechanism
   for the selected project and never copy a key into the site, chat, logs or
   a committed `.env`. Review [API key guidance](https://supabase.com/docs/guides/getting-started/api-keys).
5. Approve generation/storage of separate signing and token-HMAC secrets and
   a rotation/revocation procedure. Custom secret names use an application
   prefix, not the reserved `SUPABASE_` prefix. Never rotate a token-HMAC key
   casually: changing it can lose vote deduplication unless migration is planned.
6. With parent authorization, apply the reviewed migration and function to the
   selected staging/project environment, verify permission denials and actual
   headers/log redaction, and establish backup/export and cleanup jobs. This
   hosted step is not authorized by the current preparation request.
7. Add the approved public privacy/provider note. Separately coordinate a release
   that sets only the public function base URL in config and merges against the
   latest main. Verify real counts and moderation with clearly identified test
   records, then remove test content without fabricating historical analytics.

## Security evidence still required

The existing 38 tests validate frontend behavior with mocked responses and
existing readers/releases. No hosted service, SQL permissions, transactional
routine, trusted network header, deletion job, provider log settings or backup
restore has been tested. This follow-up adds requirements only, not a backend.

Before activation, require real Postgres and Edge Function tests for concurrent
identical/conflicting event IDs, different IDs for the same session/target,
series null-target normalization, simultaneous vote upserts/deletes, comment
retry/cooldown races, direct-table/RPC denials for public and ordinary signed-in
users, status forgery, no pending leakage, actual owner authorization/audit,
input/body/cursor limits, atomic abuse buckets and trusted-proxy behavior.
Also test expired/forged tickets after all dedup rows are deleted, signing-key
rotation, purge restart/crash safety, totals surviving retention, deletion
requests and backup recovery. Verify costs and throttling under realistic load.
None of those server guarantees can be inferred from the passing browser mocks.
