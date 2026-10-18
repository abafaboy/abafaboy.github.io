// Additive integration: leave the original reader/player/progress script intact.
import {attachEngagement} from './ui.js';
import {node} from './client.js';

const series = 'the-lord-who-measured-zero';
function ready(selector) {
  return new Promise((resolve, reject) => {
    if (document.querySelector(selector)) { resolve(); return; }
    const timer = setTimeout(() => { observer.disconnect(); reject(Error('Chapter information is unavailable.')); }, 10000);
    const observer = new MutationObserver(() => {
      if (document.querySelector(selector)) { clearTimeout(timer); observer.disconnect(); resolve(); }
    });
    observer.observe(document.body, {childList: true, subtree: true});
  });
}
const reader = document.body.classList.contains('reader');
const host = node('div', undefined, reader ? 'eng-reader-host' : 'wrap');
if (reader) document.querySelector('#endnav').after(host);
else document.querySelector('#chapters').before(host);
const owner = node('a', 'Owner overview', 'eng-owner-link'); owner.href = new URL('../owner.html', import.meta.url); host.after(owner);
try {
  const response = await fetch(new URL('../data/chapters.json', import.meta.url), {cache: 'no-cache'});
  if (!response.ok) throw Error('Chapter information is unavailable.');
  const {chapters} = await response.json();
  await ready(reader ? '#pick option' : '#grid .ch');
  const chapter = reader ? Number(document.querySelector('#pick').value) : null;
  if (reader && !chapters.some(item => item.n === chapter)) throw Error('Chapter information is unavailable.');
  const rows = reader ? [] : [...document.querySelectorAll('#grid .ch')].map(link => ({host: link.querySelector('.meta'), n: Number(new URL(link.href).searchParams.get('ch'))}));
  attachEngagement({series, chapters, chapter, host, strip: reader ? document.querySelector('#strip') : null, rows});
} catch {
  host.append(node('p', 'Shared statistics are unavailable. You can keep reading.', 'eng-note'));
}
