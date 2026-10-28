#!/usr/bin/env python3
"""Build a GitHub Pages export without changing local demo URLs."""
from pathlib import Path
import shutil, re

root=Path(__file__).resolve().parent
source=root/"public"
target=root/".publish-gh-pages"
repo="digipixel-budget-previews"
if target.exists():
 for child in target.iterdir():
  if child.name == ".git": continue
  if child.is_dir(): shutil.rmtree(child)
  else: child.unlink()
else:
 target.mkdir()
sites=[
 ("alder","Alder & Stone","Trades & home improvements","Bold industrial typography, dramatic photography and a direct quote journey for trades."),
 ("fieldnote","Fieldnote","Bookkeeping & professional services","Minimal professional editorial design with a visual business dashboard and clear services."),
 ("sunday","Sunday & Sage","Hair and beauty","Expressive salon editorial with layered portrait imagery and a menu-style service guide."),
]
for slug,name,category,description in sites:
 shutil.copytree(source/slug,target/slug)
 for f in (target/slug).rglob("*.html"):
  s=f.read_text()
  s=re.sub(r'(href|src)="/(?!/)',lambda m:m.group(1)+'="/'+repo+'/'+slug+'/',s)
  f.write_text(s)
cards=""
for idx,(slug,name,category,description) in enumerate(sites):
 cards+=f'''<a class="demo" href="/{repo}/{slug}/"><div class="photo"><img loading="lazy" src="{slug}/assets/preview.jpg" alt="{name} design preview"></div><div class="details"><small>{idx+1:02d} / {category}</small><h2>{name} </h2><p>{description}</p><strong>Explore website</strong></div></a>'''
html='''<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex,nofollow,noarchive"><meta name="description" content="Three affordable small-business website design concepts by DigiPixel."><title>Website previews | DigiPixel</title>
<style>
*{box-sizing:border-box}body{margin:0;background:#faf9f5;color:#203c30;font:16px/1.6 -apple-system,BlinkMacSystemFont,Arial,sans-serif}a{color:inherit;text-decoration:none}a:focus-visible{outline:3px solid #2382bd;outline-offset:4px}.wrap{width:min(1220px,calc(100% - 72px));margin:auto}.ribbon{background:#1b4033;color:#e1eee5;font-size:11px;letter-spacing:.18em;padding:9px 0;text-transform:uppercase}header{display:flex;justify-content:space-between;align-items:center;gap:20px;padding:28px 0}header .logo{font-size:28px;font-weight:800;letter-spacing:-.065em}header .logo span{color:#d99776}header .action{font-size:12px;font-weight:750;border:1px solid #9cab9d;padding:12px 17px}main{padding-bottom:90px}.intro{padding:86px 0 75px;display:flex;align-items:end;justify-content:space-between;gap:70px}.eyebrow{color:#72917b;font-size:11px;font-weight:800;letter-spacing:.19em;text-transform:uppercase}h1{font:normal clamp(60px,7vw,106px)/.98 Georgia,serif;letter-spacing:-.065em;margin:21px 0 0}h1 em{font-weight:normal;color:#b68b6a}.intro p{max-width:365px;color:#6e7f74;font-size:17px}.label{display:flex;justify-content:space-between;align-items:center;border-top:1px solid #cbd4ca;padding:25px 0}.label h2{font:normal 32px Georgia,serif;margin:0}.label p{font-size:12px;color:#77877c}.grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px}.demo{background:white;border:1px solid #e3e8e0;transition:transform .16s,box-shadow .16s}.demo:hover{transform:translateY(-5px);box-shadow:0 20px 40px #20352b15}.photo{height:270px;overflow:hidden;background:#e8e8e0}.photo img{width:100%;height:100%;object-fit:cover}.details{padding:28px}.details small{font-size:10px;text-transform:uppercase;letter-spacing:.13em;color:#6b8474;font-weight:800}.details h2{font:normal 34px Georgia,serif;letter-spacing:-.045em;display:flex;align-items:center;justify-content:space-between;margin:11px 0}.details h2 span{font:24px Arial,sans-serif}.details p{font-size:14px;color:#78877d;min-height:73px}.details strong{font-size:13px;border-bottom:1px solid currentColor;padding-bottom:5px}.cta{background:#204336;color:#fff;padding:55px 0}.cta .wrap{display:flex;justify-content:space-between;align-items:center;gap:32px}.cta h2{font:normal clamp(30px,4vw,49px) Georgia,serif;letter-spacing:-.04em;margin:0}.cta p{color:#d7e8df;margin:8px 0 0}.cta a{display:inline-block;white-space:nowrap;background:#e9bd98;padding:17px 21px;color:#283b2d;font-size:13px;font-weight:800}footer{font-size:12px;color:#687b6e;display:flex;justify-content:space-between;gap:20px;padding:24px 0}@media(max-width:950px){.intro{display:block;padding:60px 0}.intro p{margin-top:35px}.grid{grid-template-columns:1fr}.demo{display:grid;grid-template-columns:1fr 1fr}.photo{height:100%;min-height:260px}.details p{min-height:0}}@media(max-width:590px){.wrap{width:calc(100% - 36px)}header{padding:18px 0}header .logo{font-size:24px}header .action{font-size:11px;padding:9px}.intro{padding:50px 0}h1{font-size:clamp(54px,14vw,70px)}.label p{display:none}.grid{gap:15px}.demo{display:block}.photo{height:220px;min-height:0}.details{padding:21px}.details h2{font-size:32px}.cta .wrap{display:block}.cta a{margin-top:22px}footer{display:block}}@media(prefers-reduced-motion:reduce){.demo{transition:none}}
</style></head><body><div class="ribbon"><div class="wrap">DigiPixel / Starter website concepts</div></div><header class="wrap"><a href="https://digipixel.uk/" class="logo" aria-label="DigiPixel">digi<span>pixel</span>.</a><a class="action" href="https://digipixel.uk/">Let's talk websites </a></header><main><section class="intro wrap"><div><span class="eyebrow">THREE DIRECTIONS. THREE DISTINCT DESIGNS.</span><h1>Small business.<br><em>Big first impression.</em></h1></div><p>Three fundamentally different website approaches for independent businesses, not the same layout in three colours. Pick a style and look around.</p></section><section class="wrap"><div class="label"><h2>Explore the previews</h2><p>Three styles. Four pages each. Clear customer journeys.</p></div><div class="grid">'''+cards+'''</div></section></main><section class="cta"><div class="wrap"><div><h2>Ready for a website of your own?</h2><p>Your business, your words, your new website.</p></div><a href="https://digipixel.uk/">Talk to DigiPixel </a></div></section><footer class="wrap"><span>© DigiPixel 2026. Illustrative designs.</span><span>Businesses are fictional. Forms do not transmit enquiries.</span></footer></body></html>'''
(target/"index.html").write_text(html)
(target/".nojekyll").write_text("")
(target/"README.md").write_text("# DigiPixel budget starter previews\n\nThree fictional, non-indexed static website demos for review and portfolio presentation. No customer data is collected.\n")
print("Prepared",target, "with",sum(p.is_file() for p in target.rglob("*")),"files.")
