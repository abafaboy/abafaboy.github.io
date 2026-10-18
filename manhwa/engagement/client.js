// Public REST adapter. No credentials, local counters, or third-party SDKs.
const slugPattern = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;
const uuidPattern = /^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i;
const DAY = 86400000;
const inflight = new Set();
export const keys = ['page_views', 'reads', 'likes', 'comments'];
export const unavailable = 'Shared stats and comments are not connected yet. Historical counts are unavailable.';
export function node(tag, text, className) {
  const el = document.createElement(tag);
  if (text !== undefined) el.textContent = text;
  if (className) el.className = className;
  return el;
}
function stored(storage, key) {
  try { return JSON.parse(storage.getItem(key)); } catch { return null; }
}
function save(storage, key, value) {
  try { storage.setItem(key, JSON.stringify(value)); return storage.getItem(key) === JSON.stringify(value); } catch { return false; }
}
function storage(kind) { try { return window[kind]; } catch { return null; } }
export function browserID() {
  const store = storage('localStorage'), key = 'manhwa:engagement:browser';
  const existing = stored(store, key);
  if (uuidPattern.test(existing)) return existing;
  const id = crypto.randomUUID();
  if (!save(store, key, id)) throw Error('Browser storage is unavailable. Likes and posting need storage to prevent accidental duplicates.');
  return id;
}
export function likedState(target) {
  return stored(storage('localStorage'), `manhwa:engagement:liked:${target.series}:${target.chapter ?? 'series'}`) === true;
}
export function saveLiked(target, liked) {
  save(storage('localStorage'), `manhwa:engagement:liked:${target.series}:${target.chapter ?? 'series'}`, liked);
}
export function validMetrics(value) {
  return value && keys.every(key => Number.isSafeInteger(value[key]) && value[key] >= 0);
}
export function validateSummary(data, slug, chapters) {
  if (data?.schema_version !== 1 || data.series !== slug || !validMetrics(data.direct) || data.direct.reads !== 0 || !data.chapters || Array.isArray(data.chapters) || !Number.isFinite(Date.parse(data.since)) || !Number.isFinite(Date.parse(data.updated_at)) || data.comments_policy !== 'premoderated' || data.likes_policy !== 'browser-token') throw Error('The shared service returned an unsupported response.');
  // Every published chapter must be explicit. Missing data never becomes zero.
  for (const chapter of chapters) if (!Object.hasOwn(data.chapters, chapter.n) || !validMetrics(data.chapters[chapter.n])) throw Error('Some chapter statistics are unavailable.');
  return data;
}
export function aggregate(summary, chapters) {
  const result = {...summary.direct};
  for (const chapter of chapters) for (const key of keys) result[key] += summary.chapters[chapter.n][key];
  if (!validMetrics(result)) throw Error('Statistics are outside the supported range.');
  return result;
}
export function metricStrip(value, aggregateSeries = false) {
  const el = node('dl', undefined, 'eng-metrics');
  const labels = aggregateSeries ? ['All page views', 'Chapter reads', 'All likes', 'Approved comments'] : ['Page views', 'Chapter reads', 'Likes', 'Approved comments'];
  keys.forEach((key, i) => {
    const pair = node('div'); pair.append(node('dt', labels[i]), node('dd', value ? value[key].toLocaleString() : '—')); el.append(pair);
  });
  return el;
}
let clientPromise;
export function getClient() {
  clientPromise ??= (async () => {
    const response = await fetch(new URL('config.json', import.meta.url), {cache: 'no-store', credentials: 'omit', signal: AbortSignal.timeout(10000)});
    if (!response.ok) throw Error('Shared service settings are unavailable.');
    const config = await response.json();
    if (config.apiBase === null) return null;
    if (typeof config.apiBase !== 'string') throw Error('Shared service settings are invalid.');
    const base = new URL(config.apiBase);
    if (base.protocol !== 'https:' || base.username || base.password || base.search || base.hash) throw Error('Shared service settings are invalid.');
    base.pathname = base.pathname.replace(/\/?$/, '/');
    return {
      async request(path, body, method = 'POST') {
        const response = await fetch(new URL(path, base), {
          method: body === undefined ? 'GET' : method, credentials: 'omit', referrerPolicy: 'no-referrer', cache: 'no-store',
          headers: body === undefined ? {} : {'Content-Type': 'application/json'},
          ...(body === undefined ? {} : {body: JSON.stringify(body)}), signal: AbortSignal.timeout(10000)
        });
        if (response.status === 429) throw Error('Too many requests. Please wait a minute before trying again.');
        if (!response.ok) throw Error('The shared service is unavailable. Please try again later.');
        return response.json();
      },
      summary(series, chapters) {
        if (!slugPattern.test(series)) throw Error('Invalid series.');
        return this.request(`summary?series=${encodeURIComponent(series)}`).then(data => validateSummary(data, series, chapters));
      }
    };
  })().catch(error => { clientPromise = null; throw error; });
  return clientPromise;
}

// Stable event IDs survive reloads and lost responses. The server must also
// enforce atomic uniqueness; this client guard is not an anti-bot boundary.
export async function trackEvent(client, target, type, evidence) {
  const store = storage('sessionStorage'), sessionKey = 'manhwa:engagement:session';
  let session = stored(store, sessionKey);
  if (!session || !uuidPattern.test(session.id) || !Number.isFinite(session.at) || Date.now() - session.at >= DAY || session.at > Date.now()) {
    session = {id: crypto.randomUUID(), at: Date.now()};
    if (!save(store, sessionKey, session)) return false;
  }
  const key = `manhwa:engagement:event:${session.id}:${target.series}:${target.chapter ?? 'series'}:${type}`;
  let event = stored(store, key);
  if (event?.done) return true;
  if (inflight.has(key)) return false;
  if (!event || !uuidPattern.test(event.id)) {
    event = {id: crypto.randomUUID(), done: false};
  }
  // Retain the original coarse evidence as well as the ID. Requalification
  // after a lost response must not change the payload for that same event.
  event.payload ??= {event_id: event.id, session_id: session.id, ...target, type, ...(evidence ? {evidence} : {})};
  if (!save(store, key, event)) return false;
  inflight.add(key);
  try {
    const data = await client.request('events', event.payload);
    if (data?.accepted !== true) return false;
    save(store, key, {...event, done: true});
    return true;
  } catch { return false; }
  finally { inflight.delete(key); }
}

// A read means >=30 visible seconds over the pages, >=80% of image height
// actually exposed, and the final image's bottom seen. It is not a unique person.
export function observeRead(strip, onRead) {
  const seen = new Map();
  let active = 0, last = performance.now(), bottomSeen = false, finished = false;
  function sample() {
    if (finished) return;
    const now = performance.now(), delta = Math.min(1000, now - last); last = now;
    if (document.visibilityState !== 'visible') return;
    let top = 0, bottom = innerHeight;
    for (const el of document.querySelectorAll('.reader-bar,.rbar,#narration:not([hidden])')) {
      const rect = el.getBoundingClientRect();
      if (rect.top <= top + 1 && rect.bottom > top) top = rect.bottom;
    }
    const player = document.querySelector('#player');
    if (player && getComputedStyle(player).position === 'fixed') { const rect = player.getBoundingClientRect(); if (rect.top < bottom) bottom = rect.top; }
    const images = [...strip.querySelectorAll('img')];
    let visible = false, total = 0, covered = 0, loaded = images.length > 0;
    images.forEach((image, index) => {
      const rect = image.getBoundingClientRect(); total += rect.height;
      if (!image.complete || !image.naturalWidth || rect.height <= 0) { loaded = false; return; }
      const start = Math.max(0, top - rect.top), end = Math.min(rect.height, bottom - rect.top);
      let ranges = seen.get(image) || [];
      if (end > start) {
        visible = true;
        ranges = [...ranges, [start / rect.height, end / rect.height]].sort((a, b) => a[0] - b[0]);
        const merged = [];
        for (const range of ranges) {
          const previous = merged.at(-1);
          if (previous && range[0] <= previous[1]) previous[1] = Math.max(previous[1], range[1]);
          else merged.push([...range]);
        }
        ranges = merged; seen.set(image, ranges);
        if (index === images.length - 1 && rect.bottom <= bottom && rect.bottom > top) bottomSeen = true;
      }
      covered += ranges.reduce((sum, [a, b]) => sum + (b - a) * rect.height, 0);
    });
    if (visible) active += delta;
    if (loaded && active >= 30000 && total > 0 && covered / total >= .8 && bottomSeen) {
      finished = true; cleanup();
      onRead({visible_seconds: Math.floor(active / 1000), coverage: Math.min(1, covered / total), bottom_seen: true});
    }
  }
  const timer = setInterval(sample, 1000);
  function resetClock() { last = performance.now(); }
  function cleanup() {
    clearInterval(timer); removeEventListener('scroll', sample); removeEventListener('resize', sample);
    document.removeEventListener('visibilitychange', resetClock);
  }
  addEventListener('scroll', sample, {passive: true}); addEventListener('resize', sample, {passive: true});
  document.addEventListener('visibilitychange', resetClock);
  addEventListener('pagehide', cleanup, {once: true});
  sample();
  return cleanup;
}
