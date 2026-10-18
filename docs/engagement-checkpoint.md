# Engagement continuation checkpoint — 2026-10-18

**Paused at the owner's request.** Backend work is deferred so the current
focus can return to the manhwa. Do not resume backend setup or activate tracking
without a new instruction. This note does not authorize chapter production,
publication, a main merge, or deployment.

## Preserved work

- Feature branch: `feat/manhwa-engagement`.
- Frontend implementation commit: `68313b0299b02261657f2ed09672825b459e2592`.
- Both readers/catalogs have shared-statistics and discussion UI; the public,
  read-only owner overview is `/manhwa/owner.html`.
- `manhwa/engagement/config.json` remains `{"apiBase": null}`. Counters are
  unavailable, likes/posting are disabled, and no engagement data is transmitted.
- All published manifests and source assets remain unchanged. The original
  reader's inline audio/Follow/progress script is byte-for-byte unchanged.
- [Service contract](engagement.md) and [Supabase proposal](supabase-setup.md)
  are saved for later review. The owner confirmed there is no existing backend.

## Verification at pause

`python3 -m unittest discover -s tools -p 'test_*.py'` passed **38 tests** after
the last frontend change. These include 18 engagement browser tests and the
20 existing reader/release checks. Four engagement ES modules parsed, diff
whitespace checks passed, and mobile/desktop layouts were inspected. Tests
use mocked service responses; they do not establish backend security.
The later setup additions change documentation only.

No SQL schema, backend functions, migration, hosted project, account,
credentials, paid subscription, or deployment has been created. A public
`postgres:17-alpine` development image was downloaded before the pause; no
database container or test database was started. There are no backend tests
to claim as passing.

## If explicitly resumed later

1. Reconfirm the provider, owner account, plan/budget and database region.
   Review current official terms and limits again; the proposal's sources were
   checked on 2026-10-18 and are not a promise of future pricing.
2. Obtain the required approvals for new account/project terms, minimal data
   processing, retention/privacy notice, and server credential/signing-key
   handling. Do not create persistent agent access as a routine setup step.
3. Implement the SQL/Edge service and **signed expiring session-ticket
   extension**. The current client-generated UUID alone cannot reject an old
   replay after its deduplication record is deleted; bounded-retention backend
   activation remains blocked on resolving this contract gap.
4. Test real database constraints, concurrent retries, permissions, owner
   moderation, rate limits/trusted proxy headers, expiry after cleanup,
   deletion, logs, backup recovery and load. All remain untested.
5. Coordinate separately with the parent before any hosted staging work,
   config activation, main merge or deployment. Reconcile the latest published
   content without overwriting it. Do not backfill invented historical counts.
