#!/usr/bin/env python3
"""Export standalone concept demos into a safe GitHub Pages project subpath."""
from pathlib import Path
import shutil
import html
import subprocess
import sys
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/"public"
DST=ROOT/"docs"
BASE="/project-digipixel-starter-previews"
if DST.exists():
 shutil.rmtree(DST)
DST.mkdir()
sites=[
 ("alder","Alder & Stone","Trades & home improvements","Industrial, high contrast, quote led. Strong typography and full width imagery."),
 ("fieldnote","Fieldnote","Professional services","Minimal editorial design with a dashboard instead of a photographic hero."),
 ("sunday","Sunday & Sage","Salon & beauty","Asymmetric editorial salon design with an entirely different layout.")
]
for slug,*_ in sites:
 shutil.copytree(SRC/slug,DST/slug)
 for page in (DST/slug).rglob("*.html"):
  text=page.read_text()
  prefix=BASE+"/"+slug
  text=text.replace('href="/','href="'+prefix+'/').replace('src="/','src="'+prefix+'/')
  page.write_text(text)
 (DST/slug/".nojekyll").write_text("")
# A single branded selector, generated identically for every DigiPixel review.
selector=ROOT.parent/"digipixel-preview-selector"/"render.py"
subprocess.run([
 sys.executable,str(selector),
 "--config",str(ROOT/"preview-selector.json"),
 "--output",str(DST/"index.html")
],check=True)
shutil.copy2(DST/"index.html",DST/"404.html")
(DST/"robots.txt").write_text("User-agent: *\nDisallow: /\n")
(DST/".nojekyll").write_text("")
print("EXPORTED",len(list(DST.rglob("index.html"))),"pages and",len(list(DST.rglob("*.jpg"))),"photos to",DST)
