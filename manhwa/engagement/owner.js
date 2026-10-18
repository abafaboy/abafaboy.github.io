import {aggregate, getClient, keys, metricStrip, node, unavailable, validMetrics} from './client.js';

const status = document.querySelector('#overview-status'), rows = document.querySelector('#overview-rows'), totals = document.querySelector('#overview-totals'), refresh = document.querySelector('#overview-refresh');
function row(title, href, value, className) {
  const tr = node('tr', undefined, className), label = node('td'), a = node('a', title); a.href = href; label.append(a); tr.append(label);
  for (const key of keys) tr.append(node('td', value ? value[key].toLocaleString() : '—'));
  return tr;
}
async function load() {
  refresh.disabled = true; rows.replaceChildren(); totals.replaceChildren(metricStrip(null, true));
  status.textContent = 'Loading shared data…';
  try {
    const response = await fetch(new URL('catalog.json', import.meta.url), {cache: 'no-cache'});
    if (!response.ok) throw Error('The published series list is unavailable.');
    const catalog = await response.json(), client = await getClient();
    const outcomes = await Promise.allSettled(catalog.map(async item => {
      const response = await fetch(new URL(item.manifest, import.meta.url), {cache: 'no-cache'});
      if (!response.ok) throw Error('Published chapter information is unavailable.');
      const {chapters} = await response.json();
      let summary = null, error = null;
      if (client) try { summary = await client.summary(item.slug, chapters); } catch (e) { error = e.message; }
      return {item, chapters, summary, error};
    }));
    const total = Object.fromEntries(keys.map(key => [key, 0])); let complete = !!client;
    outcomes.forEach((outcome, index) => {
      if (outcome.status !== 'fulfilled') {
        complete = false;
        const item = catalog[index]; rows.append(row(`${item.title} · chapters unavailable`, new URL(item.url, import.meta.url), null, 'eng-series')); return;
      }
      const {item, chapters, summary, error} = outcome.value;
      let value = null;
      if (summary) value = aggregate(summary, chapters); else complete = false;
      rows.append(row(item.title + (error ? ' · shared service unavailable' : ''), new URL(item.url, import.meta.url), value, 'eng-series'));
      if (value) keys.forEach(key => { total[key] += value[key]; });
      chapters.forEach(chapter => {
        const url = item.slug === 'the-lord-who-measured-zero' ? new URL(`../read.html?ch=${chapter.n}`, import.meta.url) : new URL(`../series/read.html?series=${encodeURIComponent(item.slug)}&ch=${chapter.n}`, import.meta.url);
        rows.append(row(`Chapter ${chapter.n}: ${chapter.title}`, url, summary?.chapters[chapter.n], 'eng-chapter'));
      });
      if (summary) {
        const tr = node('tr'), td = node('td', `Measurement since ${new Date(summary.since).toLocaleDateString()} · updated ${new Date(summary.updated_at).toLocaleString()}`, 'eng-note'); td.colSpan = 5; tr.append(td); rows.append(tr);
      }
    });
    if (complete && !validMetrics(total)) throw Error('Overall statistics are outside the supported range.');
    if (complete) { totals.replaceChildren(metricStrip(total, true)); status.textContent = 'Shared data loaded for all published series.'; }
    else status.textContent = client ? 'Some shared data is unavailable. Overall totals are withheld until every series is available.' : unavailable;
  } catch (error) { status.textContent = error.message; }
  finally { refresh.disabled = false; }
}
refresh.addEventListener('click', load);
void load();
