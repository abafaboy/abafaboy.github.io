import {validNarration, setupNarration} from './narration.js';

const $ = id => document.getElementById(id);
const query = new URLSearchParams(location.search);
const slug = query.get('series') || '';
const imageName = /^[a-zA-Z0-9][a-zA-Z0-9_.-]*\.(?:webp|png|jpe?g)$/i;
const positive = n => Number.isSafeInteger(n) && n > 0;
const chapterURL = n => `read.html?series=${encodeURIComponent(slug)}&ch=${n}`;
const homeURL = `./?series=${encodeURIComponent(slug)}`;
let storageKey = `manhwa:${slug}`;
const getStored = (key, fallback) => {
  try { const value = JSON.parse(localStorage.getItem(`${storageKey}:${key}`)); return value && typeof value === 'object' && !Array.isArray(value) ? value : fallback; }
  catch { return fallback; }
};
const setStored = (key, value) => { try { localStorage.setItem(`${storageKey}:${key}`, JSON.stringify(value)); } catch {} };
let read = {};

function validate(manifest) {
  if (manifest?.schema_version !== 1 || manifest.slug !== slug || typeof manifest.title !== 'string' || !manifest.title.trim() || !Array.isArray(manifest.chapters)) throw Error('This series is unavailable.');
  if (manifest.cover && !imageName.test(manifest.cover)) throw Error('This series is unavailable.');
  if (manifest.edition !== undefined && (!positive(manifest.edition) || manifest.edition > 9999)) throw Error('This series is unavailable.');
  let previous = 0;
  for (const chapter of manifest.chapters) {
    if (!positive(chapter.n) || chapter.n <= previous || typeof chapter.title !== 'string' || !chapter.title.trim() || !positive(chapter.width) || !Array.isArray(chapter.segments) || !chapter.segments.length) throw Error('This series is unavailable.');
    for (const segment of chapter.segments) {
      if (!Array.isArray(segment) || segment.length !== 2 || !imageName.test(segment[0]) || !positive(segment[1])) throw Error('This series is unavailable.');
    }
    if (chapter.gutters !== undefined && (!chapter.gutters || typeof chapter.gutters !== 'object' || Array.isArray(chapter.gutters) || Object.entries(chapter.gutters).some(([file, gap]) => !chapter.segments.some(segment => segment[0] === file) || !Number.isSafeInteger(gap) || gap < 0 || gap > 1000))) throw Error('This series is unavailable.');
    if (chapter.framing_height !== undefined && (!positive(chapter.framing_height) || chapter.framing_height > 10000)) throw Error('This series is unavailable.');
    if (chapter.top_masks !== undefined && (!chapter.top_masks || typeof chapter.top_masks !== 'object' || Array.isArray(chapter.top_masks) || Object.entries(chapter.top_masks).some(([file, top]) => !chapter.segments.some(segment => segment[0] === file && Number.isSafeInteger(top) && top >= 0 && top < segment[1])))) throw Error('This series is unavailable.');
    if (chapter.pdf !== undefined && (typeof chapter.pdf !== 'string' || !/^[a-zA-Z0-9][a-zA-Z0-9_.-]*\.pdf$/i.test(chapter.pdf))) throw Error('This series is unavailable.');
    if (chapter.thumbnail && !imageName.test(chapter.thumbnail)) throw Error('This series is unavailable.');
    if (chapter.audio && !validNarration(chapter.audio, chapter.segments)) throw Error('This series is unavailable.');
    previous = chapter.n;
  }
  return manifest;
}

function element(tag, text, className) {
  const node = document.createElement(tag);
  if (text !== undefined) node.textContent = text;
  if (className) node.className = className;
  return node;
}

function renderCatalog(manifest, base) {
  document.title = `${manifest.title} · Chapters`;
  $('title').textContent = manifest.title;
  $('synopsis').textContent = manifest.synopsis || '';
  if (manifest.cover) { $('cover').src = new URL(manifest.cover, base); $('cover').hidden = false; }
  const chapters = manifest.chapters;
  $('count').textContent = `${chapters.length} ${chapters.length === 1 ? 'chapter' : 'chapters'}`;
  if (!chapters.length) {
    $('start').hidden = $('latest').hidden = true;
    $('chapters').append(element('p', 'No chapters have been released yet.'));
  } else {
    $('start').href = chapterURL(chapters[0].n);
    $('latest').href = chapterURL(chapters.at(-1).n);
    chapters.slice().reverse().forEach(chapter => {
      const link = element('a', undefined, 'chapter-link'); link.href = chapterURL(chapter.n);
      if (chapter.thumbnail) {
        const image = new Image(); image.alt = ''; image.loading = 'lazy'; image.src = new URL(`ch/${String(chapter.n).padStart(3, '0')}/${chapter.thumbnail}`, base); link.append(image);
      }
      const meta = element('div'); meta.append(element('small', `Chapter ${chapter.n}`), element('strong', chapter.title)); link.append(meta);
      if (read[chapter.n]) link.append(element('span', 'Read', 'read-marker'));
      $('chapters').append(link);
    });
    const position = getStored('position', {});
    if (chapters.some(chapter => chapter.n === position.ch)) {
      const link = element('a', `Continue chapter ${position.ch}`); link.href = chapterURL(position.ch);
      $('resume').append(link); $('resume').hidden = false;
    }
  }
  $('series').hidden = false;
}

function renderReader(manifest, base) {
  const chapters = manifest.chapters;
  const requested = query.get('ch');
  const chapter = requested === null ? chapters[0] : chapters.find(ch => String(ch.n) === requested);
  $('back').href = $('all-chapters').href = homeURL;
  const pick = $('pick'); pick.replaceChildren();
  if (!chapter) {
    const option = element('option', 'Choose a chapter'); option.value = ''; option.disabled = option.selected = true; pick.append(option);
  }
  chapters.forEach(ch => { const option = element('option', `Chapter ${ch.n}: ${ch.title}`); option.value = ch.n; option.selected = ch.n === chapter?.n; pick.append(option); });
  pick.disabled = !chapters.length;
  pick.addEventListener('change', () => { if (pick.value) location.href = chapterURL(pick.value); });
  if (!chapter) {
    document.title = `Chapter unavailable · ${manifest.title}`;
    throw Error('This chapter is unavailable in the current edition.');
  }
  const index = chapters.indexOf(chapter), previous = chapters[index - 1], next = chapters[index + 1];
  const chapterBase = new URL(`ch/${String(chapter.n).padStart(3, '0')}/`, base);
  document.title = `Chapter ${chapter.n}: ${chapter.title} · ${manifest.title}`;
  $('series-name').textContent = manifest.title;
  $('chapter-title').textContent = `Chapter ${chapter.n}: ${chapter.title}`;
  for (const [id, target] of [['prev', previous], ['next', next]]) {
    if (target) { $(id).href = chapterURL(target.n); $(id).removeAttribute('aria-disabled'); }
  }
  $('end-title').textContent = `End of Chapter ${chapter.n}`;
  if (next) {
    $('nextbig').href = chapterURL(next.n); $('nextbig').textContent = `Chapter ${next.n} →`; $('nextbig').hidden = false;
  } else $('endnav').insertBefore(element('p', "You're up to date."), $('all-chapters'));
  const images = new Map();
  chapter.segments.forEach(([file, height], index) => {
    const image = new Image(); image.width = chapter.width; image.height = height;
    image.id = `panel-${String(index + 1).padStart(2, '0')}`;
    image.alt = `Chapter ${chapter.n}, page ${index + 1}`; image.decoding = 'async';
    if (chapter.gutters?.[file]) image.style.marginBottom = `${100 * chapter.gutters[file] / chapter.width}%`;
    image.loading = index < 2 ? 'eager' : 'lazy';
    if (index === 0) image.fetchPriority = 'high';
    if (chapter.top_masks?.[file]) image.style.clipPath = `inset(${100 * chapter.top_masks[file] / height}% 0 0)`;
    image.addEventListener('error', () => {
      $('strip').insertBefore(element('p', 'A page could not load. Please refresh to try again.', 'image-error'), image);
    }, {once: true});
    image.src = new URL(file, chapterBase);
    $('strip').append(image); images.set(file, image);
  });
  if (chapter.pdf) { $('download-pdf').href = new URL(chapter.pdf, chapterBase); $('download-pdf').download = `${slug}-chapter-${chapter.n}.pdf`; $('download-pdf').hidden = false; }
  if (chapter.audio) setupNarration(chapter, chapterBase, images);
  setStored('position', {ch: chapter.n});
  const observer = new IntersectionObserver(entries => {
    if (entries.some(entry => entry.isIntersecting)) { read[chapter.n] = 1; setStored('read', read); observer.disconnect(); }
  });
  observer.observe($('endnav'));
  addEventListener('keydown', event => {
    if (event.defaultPrevented || event.altKey || event.ctrlKey || event.metaKey || event.shiftKey || event.target.closest('input, textarea, select, button, audio, [contenteditable]')) return;
    const target = event.key === 'ArrowRight' ? next : event.key === 'ArrowLeft' ? previous : null;
    if (target) location.href = chapterURL(target.n);
  });
  $('reader').hidden = false;
}

try {
  if (!/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(slug) || slug.length > 80) throw Error('Choose a series from its reading link.');
  const base = new URL(`./${slug}/`, location.href);
  const response = await fetch(new URL('series.json', base), {cache: 'no-cache'});
  if (!response.ok) throw Error('This series is unavailable.');
  const manifest = validate(await response.json());
  // Edition one keeps its original keys; later editions never inherit old read markers.
  if ((manifest.edition || 1) > 1) storageKey += `:edition:${manifest.edition}`;
  read = getStored('read', {});
  if (document.body.dataset.view === 'reader') renderReader(manifest, base);
  else renderCatalog(manifest, base);
  $('status').hidden = true;
} catch (error) {
  $('status').textContent = error.message.startsWith('This ') || error.message.startsWith('Choose ') ? error.message : 'This series could not load. Please try again.';
  if (document.body.dataset.view === 'reader') {
    if ($('pick').disabled) $('pick').replaceChildren(element('option', 'Chapters unavailable'));
    const back = element('a', 'Return to chapters', 'button');
    back.href = /^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(slug) && slug.length <= 80 ? homeURL : '../';
    $('back').href = back.href;
    $('status').append(element('br'), back);
  }
}
