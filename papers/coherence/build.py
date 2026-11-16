#!/usr/bin/env python3
"""Build the paper: paper.md -> index.html (MathML, no JS) -> paper.pdf (headless Chromium).

Usage: python3 build.py            (run from the paper directory)
Requires pandoc. The PDF step needs Node with Playwright and is skipped if unavailable.
"""
import pathlib, subprocess, shutil, sys

here = pathlib.Path(__file__).resolve().parent
md, tpl, out = here / "paper.md", here / "template.html", here / "index.html"
subprocess.run([
    "pandoc", str(md), "-o", str(out), "--from", "markdown+tex_math_dollars+implicit_figures+pipe_tables+fenced_divs+smart",
    "--to", "html5", "--standalone", "--template", str(tpl), "--mathml", "--toc", "--toc-depth=1",
    "--number-sections", "--section-divs", "--wrap=none",
], check=True)
# Keep punctuation attached to inline math: browsers may otherwise break the line
# between a MathML element and the comma or full stop that follows it.
import re
html = out.read_text()
_inline = r'<math(?![^>]*display="block")[^>]*>.*?</math>'
_lead, _trail = r'[(\u2018\u201c]+', r'[.,;:!?)\u2019\u201d]+'
html = re.sub(rf'({_lead})?({_inline})({_trail})?',
              lambda m: m.group(0) if not (m.group(1) or m.group(3))
              else f'<span class="nw">{m.group(0)}</span>', html, flags=re.S)
# Lift each table caption out of the table and wrap the table in its own scroll
# container, so a wide table scrolls on narrow screens while its caption wraps
# at the column width.
html = re.sub(r'<table[^>]*>\s*<caption>(.*?)</caption>(.*?)</table>',
              r'<div class="tblock"><p class="tcap">\1</p><div class="tablewrap"><table>\2</table></div></div>',
              html, flags=re.S)
out.write_text(html)
print("wrote", out)

if "--no-pdf" in sys.argv or not shutil.which("node"):
    sys.exit(0)
js = f"""
const {{ chromium }} = require('playwright');
(async () => {{
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://{out}', {{ waitUntil: 'load' }});
  await p.pdf({{ path: '{here / "paper.pdf"}', format: 'A4', printBackground: true,
    margin: {{ top: '20mm', bottom: '20mm', left: '18mm', right: '18mm' }} }});
  await b.close();
}})().catch(e => {{ console.error(e); process.exit(1); }});
"""
r = subprocess.run(["node", "-e", js], cwd="/")
print("wrote paper.pdf" if r.returncode == 0 else "PDF step failed (page is still built)")
