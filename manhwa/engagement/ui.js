import {aggregate, browserID, getClient, likedState, metricStrip, node, observeRead, saveLiked, trackEvent, unavailable, validMetrics} from './client.js';

export function attachEngagement({series, chapters, chapter = null, host, strip = null, rows = []}) {
  const target = {series, chapter}, label = chapter === null ? 'series' : 'chapter';
  const panel = node('section', undefined, 'engagement'); panel.setAttribute('aria-label', `${label} statistics and discussion`);
  panel.append(node('h2', chapter === null ? 'Series activity' : 'Chapter activity'));
  const metrics = node('div'); metrics.append(metricStrip(null, chapter === null));
  const status = node('p', 'Loading shared statistics…', 'eng-note'); status.setAttribute('role', 'status');
  const note = node('p', chapter === null
    ? 'Series totals include this chapter list and all published chapters. Likes and discussion below are for the series itself.'
    : 'Page views count opens once per page in a tab session (up to 24 hours). A chapter read needs 30 visible seconds, 80% of its artwork seen, and the end reached. These counts do not measure unique people.', 'eng-note');
  const like = node('button', `Like this ${label}`, 'eng-button'); like.type = 'button'; like.disabled = true; like.setAttribute('aria-pressed', 'false');
  const likeNote = node('p', 'One like per browser token for each series or chapter. Clearing storage or using another browser allows another vote.', 'eng-note');
  const refresh = node('button', 'Refresh shared data', 'eng-button'); refresh.type = 'button'; refresh.hidden = true;
  const discussion = node('details'); discussion.open = chapter !== null;
  const discussionToggle = node('summary', `${chapter === null ? 'Series' : 'Chapter'} discussion`);
  const commentsStatus = node('p', 'Comments are unavailable until a shared service is connected.', 'eng-note'); commentsStatus.setAttribute('role', 'status');
  const comments = node('ol', undefined, 'eng-comments');
  const more = node('button', 'Load more comments', 'eng-button'); more.type = 'button'; more.hidden = true;
  const form = document.createElement('form'); form.className = 'eng-form';
  const name = document.createElement('input'); name.name = 'name'; name.maxLength = 40; name.autocomplete = 'off';
  const text = document.createElement('textarea'); text.name = 'text'; text.required = true; text.minLength = 1; text.maxLength = 1000; text.rows = 4;
  const nameLabel = node('label', 'Name (optional, up to 40 characters)'); nameLabel.append(name);
  const textLabel = node('label', 'Comment (up to 1,000 characters)'); textLabel.append(text);
  const trapLabel = node('label', 'Leave this field empty', 'eng-trap'); trapLabel.setAttribute('aria-hidden', 'true');
  const trap = document.createElement('input'); trap.name = 'website'; trap.tabIndex = -1; trap.autocomplete = 'off'; trapLabel.append(trap);
  const submit = node('button', 'Submit for review', 'eng-button'); submit.type = 'submit'; submit.disabled = true;
  name.disabled = text.disabled = true;
  const postingStatus = node('p', '', 'eng-note'); postingStatus.setAttribute('role', 'status');
  form.append(nameLabel, textLabel, trapLabel, node('p', 'Comments appear after owner approval. No email or account is requested. Please avoid personal information. Up to two links per comment.', 'eng-note'), submit, postingStatus);
  // The original reader uses document-level arrow navigation. Typing in this
  // isolated form must not turn the chapter; its reader code stays unchanged.
  panel.addEventListener('keydown', event => { if (event.target.closest('input,textarea') && ['ArrowLeft', 'ArrowRight'].includes(event.key)) event.stopPropagation(); });
  discussion.append(discussionToggle, commentsStatus, comments, more, form);
  panel.append(metrics, status, note, like, likeNote, refresh, discussion);
  host.append(panel);
  const rowMetrics = rows.map(({host, n}) => { const el = node('small', 'Shared stats unavailable', 'eng-row'); host.append(el); return {el, n}; });
  let client, summary, liked = likedState(target), busyLike = false, busyPost = false, cursor = null, postAttempt = null;
  let recordView = null;
  const commentIDs = new Set();
  function startRecording(service) {
    if (!recordView) {
      let recorded = false;
      recordView = async () => {
        if (document.visibilityState !== 'visible' || recorded) return;
        recorded = await trackEvent(service, target, 'page_view');
      };
      document.addEventListener('visibilitychange', recordView);
      if (strip && chapter !== null) observeRead(strip, evidence => trackEvent(service, target, 'chapter_read', evidence));
    }
    void recordView();
  }
  function draw() {
    metrics.replaceChildren(metricStrip(chapter === null ? aggregate(summary, chapters) : summary.chapters[chapter], chapter === null));
    rowMetrics.forEach(({el, n}) => {
      const item = summary.chapters[n];
      el.textContent = item ? `${item.page_views.toLocaleString()} views · ${item.reads.toLocaleString()} reads · ${item.likes.toLocaleString()} likes · ${item.comments.toLocaleString()} comments` : 'Shared stats unavailable';
    });
    const direct = chapter === null ? summary.direct : summary.chapters[chapter];
    discussionToggle.textContent = `${chapter === null ? 'Series' : 'Chapter'} discussion · ${direct.comments.toLocaleString()} approved comments`;
    like.textContent = `${liked ? 'Unlike' : 'Like'} this ${label} · ${direct.likes.toLocaleString()}`;
    like.setAttribute('aria-pressed', String(liked));
    status.textContent = `Shared counts since ${new Date(summary.since).toLocaleDateString()}. Updated ${new Date(summary.updated_at).toLocaleString()}. Earlier history is unavailable.`;
  }
  async function loadComments(reset = true) {
    more.disabled = true;
    if (reset) { cursor = null; commentIDs.clear(); comments.replaceChildren(); commentsStatus.textContent = 'Loading approved comments…'; }
    try {
      const query = new URLSearchParams({series, chapter: chapter ?? 'series'});
      if (cursor) query.set('cursor', cursor);
      const data = await client.request(`comments?${query}`);
      if (!Array.isArray(data?.items) || data.items.length > 20 || (data.next_cursor !== null && (typeof data.next_cursor !== 'string' || !data.next_cursor.length || data.next_cursor.length > 200)) || data.items.some(item => typeof item.id !== 'string' || item.id.length > 100 || item.status !== 'approved' || typeof item.name !== 'string' || item.name.length > 40 || typeof item.text !== 'string' || !item.text.trim() || item.text.length > 1000 || !Number.isFinite(Date.parse(item.created_at)))) throw Error('Comments could not be loaded safely.');
      for (const item of data.items) {
        if (commentIDs.has(item.id)) continue;
        const li = node('li'), date = node('time', new Date(item.created_at).toLocaleDateString()); date.dateTime = item.created_at;
        li.append(node('strong', item.name || 'Reader'), date, node('p', item.text)); comments.append(li); commentIDs.add(item.id);
      }
      cursor = data.next_cursor;
      commentsStatus.textContent = commentIDs.size ? 'Approved comments, newest first.' : 'No approved comments yet. Be the first to leave one for review.';
      more.hidden = !cursor;
    } catch (error) { commentsStatus.textContent = error.message; more.hidden = true; }
    finally { more.disabled = false; }
  }
  async function load() {
    refresh.disabled = true;
    like.disabled = name.disabled = text.disabled = submit.disabled = true;
    try {
      client = await getClient();
      if (!client) { status.textContent = unavailable; return; }
      // View recording does not depend on summary availability.
      startRecording(client);
      summary = await client.summary(series, chapters); draw();
      like.disabled = name.disabled = text.disabled = submit.disabled = false;
      refresh.hidden = false;
      await loadComments();
    } catch (error) {
      status.textContent = error.message;
      metrics.replaceChildren(metricStrip(null, chapter === null));
      rowMetrics.forEach(({el}) => { el.textContent = 'Shared stats unavailable'; });
      summary = null;
      like.textContent = `${liked ? 'Unlike' : 'Like'} this ${label}`;
      discussionToggle.textContent = `${chapter === null ? 'Series' : 'Chapter'} discussion`;
      comments.replaceChildren(); more.hidden = true;
      commentsStatus.textContent = 'Comments are unavailable. Refresh when the shared service returns.';
      like.disabled = name.disabled = text.disabled = submit.disabled = true;
      refresh.hidden = false;
    } finally { refresh.disabled = false; }
  }
  like.addEventListener('click', async () => {
    if (busyLike || !summary || !client) return;
    busyLike = true; like.disabled = refresh.disabled = true;
    const desired = !liked;
    try {
      const data = await client.request('likes', {...target, client_id: browserID(), liked: desired}, 'PUT');
      if (data?.liked !== desired || !validMetrics(data.metrics) || (chapter === null && data.metrics.reads !== 0)) throw Error('The like was not confirmed. Refresh and try again.');
      if (chapter === null) summary.direct = data.metrics; else summary.chapters[chapter] = data.metrics;
      liked = desired; saveLiked(target, liked); draw();
    } catch (error) { status.textContent = error.message; }
    finally { busyLike = false; like.disabled = refresh.disabled = false; }
  });
  form.addEventListener('submit', async event => {
    event.preventDefault();
    if (busyPost || !client || !summary) return;
    const body = text.value.trim(), author = name.value.trim();
    if (trap.value) { postingStatus.textContent = 'Submission could not be accepted.'; return; }
    if (!body || body.length > 1000 || author.length > 40 || /[\u0000-\u0008\u000B\u000C\u000E-\u001F\u007F]/.test(body + author) || (body.match(/https?:\/\/|www\./gi) || []).length > 2) { postingStatus.textContent = 'Use 1–1,000 characters, a name up to 40 characters, and at most two links.'; return; }
    try {
      const cooldown = Number(sessionStorage.getItem('manhwa:engagement:last-comment') || 0);
      if (Date.now() - cooldown < 60000) { postingStatus.textContent = 'Please wait a minute before submitting another comment.'; return; }
    } catch { /* The server still enforces rate limits. */ }
    busyPost = true; submit.disabled = refresh.disabled = true;
    try {
      const clientID = browserID();
      const digest = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(JSON.stringify([author, body])));
      const signature = [...new Uint8Array(digest)].map(byte => byte.toString(16).padStart(2, '0')).join('');
      const attemptKey = `manhwa:engagement:comment:${series}:${chapter ?? 'series'}`;
      try { postAttempt = JSON.parse(sessionStorage.getItem(attemptKey)); } catch {}
      if (!postAttempt || postAttempt.signature !== signature || !/^[0-9a-f-]{36}$/i.test(postAttempt.id)) postAttempt = {signature, id: crypto.randomUUID()};
      try { sessionStorage.setItem(attemptKey, JSON.stringify(postAttempt)); } catch {}
      const data = await client.request('comments', {...target, client_id: clientID, request_id: postAttempt.id, name: author, text: body, website: ''});
      if (data?.status !== 'pending') throw Error('Submission was not confirmed. Try again with the same text.');
      postingStatus.textContent = 'Submitted for owner review. Your comment is not public yet.';
      text.value = ''; postAttempt = null;
      try { sessionStorage.removeItem(attemptKey); } catch {}
      try { sessionStorage.setItem('manhwa:engagement:last-comment', String(Date.now())); } catch {}
    } catch (error) { postingStatus.textContent = error.message; }
    finally { busyPost = false; submit.disabled = refresh.disabled = false; }
  });
  refresh.addEventListener('click', load); more.addEventListener('click', () => loadComments(false));
  void load();
  return panel;
}
