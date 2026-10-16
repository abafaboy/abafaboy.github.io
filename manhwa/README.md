# The Lord Who Measured Zero: reader

A static webtoon reader for an original manhwa, served by GitHub Pages at https://abafaboy.github.io/manhwa/

- `index.html` is the landing page and chapter list.
- `read.html?ch=N` is the vertical reader. Its narration player can scroll the page in time with the voice.
- `data/chapters.json` lists the chapters, their image segments and the scroll keyframes for the narration.
- `ch/NNN/` holds each chapter's WebP page segments, its thumbnail and `audio.mp3`.

New chapters are exported by the production pipeline (build_site.py) and committed here.
