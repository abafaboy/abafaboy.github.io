// Cue coordinates belong to the finished, lettered chapter images.
export function validNarration(audio, segments) {
  if (!audio || typeof audio !== 'object' || Array.isArray(audio) || !/^[a-zA-Z0-9][a-zA-Z0-9_.-]*\.(?:mp3|m4a|ogg|wav)$/i.test(audio.file)) return false;
  if (audio.duration !== undefined && (!Number.isFinite(audio.duration) || audio.duration <= 0)) return false;
  if (audio.cues === undefined) return true;
  if (!Array.isArray(audio.cues) || !audio.cues.length) return false;
  const positions = new Map();
  let total = 0;
  for (const [file, height] of segments) { positions.set(file, {top: total, height}); total += height; }
  let previousTime = -1, previousY = -1;
  for (const cue of audio.cues) {
    if (!cue || typeof cue !== 'object' || Array.isArray(cue) || Object.keys(cue).some(key => !['t', 'segment', 'y', 'panel', 'line'].includes(key))) return false;
    const segment = positions.get(cue.segment);
    if (!Number.isFinite(cue.t) || cue.t < 0 || cue.t <= previousTime || !segment || !Number.isFinite(cue.y) || cue.y < 0 || cue.y > segment.height) return false;
    if (audio.duration !== undefined && cue.t > audio.duration) return false;
    if (segment.top + cue.y < previousY) return false;
    for (const key of ['panel', 'line']) if (cue[key] !== undefined && (!Number.isSafeInteger(cue[key]) || cue[key] <= 0 || cue[key] > 9999)) return false;
    previousTime = cue.t; previousY = segment.top + cue.y;
  }
  return audio.cues[0].t === 0;
}

export function setupNarration(chapter, chapterBase, images) {
  const audio = document.getElementById('audio');
  const controls = document.getElementById('narration');
  const follow = document.getElementById('follow');
  const header = document.querySelector('.reader-bar');
  audio.src = new URL(chapter.audio.file, chapterBase);
  controls.hidden = false;
  let frame = null, following = true, lastSet = null;
  const stop = () => { if (frame !== null) cancelAnimationFrame(frame); frame = null; };
  audio.addEventListener('error', () => {
    stop(); audio.hidden = follow.hidden = true;
    document.getElementById('audio-error').hidden = false;
  });
  if (!chapter.audio.cues) return;
  follow.hidden = false;
  const cues = chapter.audio.cues;
  const fitReadingWidth = () => {
    const visible = innerHeight - header.offsetHeight - controls.offsetHeight - 36;
    controls.closest('main').style.setProperty('--reading-width', `${Math.min(720, Math.max(390, visible * chapter.width / (chapter.framing_height || chapter.width * 1.2)))}px`);
  };
  requestAnimationFrame(fitReadingWidth);
  const anchor = (cue, visible) => {
    const image = images.get(cue.segment);
    const point = cue.y * image.clientWidth / chapter.width;
    const offset = Math.min(Math.max(0, point - visible), Math.max(0, image.clientHeight - visible));
    return image.getBoundingClientRect().top + scrollY + offset;
  };
  const destination = () => {
    const time = audio.currentTime;
    let index = 0;
    while (index + 1 < cues.length && cues[index + 1].t <= time) index++;
    const cue = cues[index], next = cues[index + 1];
    const inset = header.offsetHeight + controls.offsetHeight;
    const lead = 24;
    const visible = Math.max(1, innerHeight - inset - lead - 12);
    let y = anchor(cue, visible);
    if (next) y += (anchor(next, visible) - y) * Math.max(0, Math.min(1, (time - cue.t) / (next.t - cue.t)));
    return Math.max(0, Math.min(document.documentElement.scrollHeight - innerHeight, y - inset - lead));
  };
  const align = (immediate = false) => {
    if (!following || audio.seeking && !immediate) return;
    const target = destination();
    const top = immediate || Math.abs(target - scrollY) < 2 ? target : scrollY + (target - scrollY) * .35;
    scrollTo({top, behavior: 'instant'});
    lastSet = scrollY;
  };
  const tick = () => {
    frame = null;
    if (!following || audio.paused || audio.ended || audio.seeking) return;
    align(); frame = requestAnimationFrame(tick);
  };
  const start = () => { stop(); if (following && !audio.paused && !audio.ended) frame = requestAnimationFrame(tick); };
  const setFollow = value => {
    following = value;
    follow.setAttribute('aria-pressed', String(value));
    follow.textContent = value ? 'Follow on' : 'Follow off';
    if (value) { align(true); start(); } else stop();
  };
  follow.addEventListener('click', () => setFollow(!following));
  audio.addEventListener('playing', start);
  for (const event of ['pause', 'ended', 'waiting', 'seeking']) audio.addEventListener(event, stop);
  audio.addEventListener('ended', () => {
    if (!following) return;
    const end = document.getElementById('endnav');
    const inset = header.offsetHeight + controls.offsetHeight + 24;
    scrollTo({top: Math.max(0, Math.min(document.documentElement.scrollHeight - innerHeight, end.getBoundingClientRect().top + scrollY - inset)), behavior: 'instant'});
    lastSet = scrollY;
  });
  audio.addEventListener('seeking', () => align(true));
  audio.addEventListener('seeked', () => { align(true); start(); });
  const manual = event => {
    if (event?.target instanceof Element && event.target.closest('#narration, .reader-bar')) return;
    if (following) setFollow(false);
  };
  addEventListener('wheel', manual, {passive: true});
  addEventListener('touchmove', manual, {passive: true});
  addEventListener('keydown', event => {
    if (event.defaultPrevented || event.altKey || event.ctrlKey || event.metaKey || event.target.closest('input, textarea, select, button, audio, [contenteditable]')) return;
    if ([' ', 'ArrowUp', 'ArrowDown', 'PageUp', 'PageDown', 'Home', 'End'].includes(event.key)) manual(event);
  });
  // Also recognize dragging the scrollbar or other direct user scrolling.
  addEventListener('scroll', () => {
    if (following && (lastSet === null || Math.abs(scrollY - lastSet) > 4)) setFollow(false);
  }, {passive: true});
  addEventListener('resize', () => { fitReadingWidth(); if (following) align(true); });
  addEventListener('pagehide', () => { stop(); audio.pause(); });
}
