#!/usr/bin/env python3
"""Export standalone concept demos into a safe GitHub Pages project subpath."""
from pathlib import Path
import shutil
import html
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/"public"
DST=ROOT/"docs"
BASE="/project-digipixel-starter-previews"
if DST.exists():
 shutil.rmtree(DST)
DST.mkdir()
sites=[
 ("alder","Alder & Stone","Trades & home improvements","Considered spaces. Straightforward service and quote journeys."),
 ("fieldnote","Fieldnote","Professional services","Quiet confidence, easy-to-understand services and an inviting enquiry experience."),
 ("sunday","Sunday & Sage","Salon & beauty","An image-led service menu with a welcoming appointment journey.")
]
for slug,*_ in sites:
 shutil.copytree(SRC/slug,DST/slug)
 for page in (DST/slug).rglob("*.html"):
  text=page.read_text()
  prefix=BASE+"/"+slug
  text=text.replace('href="/','href="'+prefix+'/').replace('src="/','src="'+prefix+'/')
  page.write_text(text)
 (DST/slug/".nojekyll").write_text("")
cards=""
for index,(slug,name,sector,description) in enumerate(sites,1):
 cards+=f'''<a class="card" href="./{slug}/" aria-label="Open {html.escape(name)} concept website"><div class="photo"><img src="./{slug}/assets/hero.jpg" alt="Example {html.escape(sector.lower())} website design" loading="eager"></div><div class="card-content"><span class="label">CONCEPT 0{index} · {html.escape(sector)}</span><h2>{html.escape(name)} <span aria-hidden="true">↗</span></h2><p>{html.escape(description)}</p><span class="cta">Explore the website <span aria-hidden="true">→</span></span></div></a>'''
page='''<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow,noarchive"><meta name="theme-color" content="#172e2b"><title>DigiPixel | Three affordable website concepts</title><meta name="description" content="Three mobile-ready small-business website concepts showing the kind of design DigiPixel could create. Fictional sample businesses."><style>
*{box-sizing:border-box}body{margin:0;color:#1f3732;background:#f8f8f4;font:16px/1.6 -apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif}a{color:inherit;text-decoration:none}.wrap{width:min(1190px,calc(100% - 48px));margin:auto}.top{background:#172e2b;color:#f2f5ef;padding:24px 0}.top .wrap{display:flex;justify-content:space-between;align-items:center;gap:20px}.logo{font:bold 27px Georgia,serif}.logo span{color:#dbb980}.top a:last-child{font-size:12px;text-decoration:underline;text-underline-offset:4px}main{padding:80px 0 105px}.kicker{font-size:11px;letter-spacing:.2em;font-weight:800;text-transform:uppercase;color:#8b8069}h1{font:normal clamp(48px,6vw,85px)/1.03 Georgia,serif;letter-spacing:-.047em;max-width:900px;margin:19px 0 23px}main>.wrap>p{font-size:17px;color:#607069;max-width:640px;line-height:1.8;margin-bottom:55px}.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:19px}.card{background:#fff;display:flex;flex-direction:column;border:1px solid #183b2c14;transition:transform .2s,box-shadow .2s}.card:hover{transform:translateY(-5px);box-shadow:0 20px 38px #203d2b18}.photo{height:260px;overflow:hidden}.photo img{width:100%;height:100%;object-fit:cover;transition:transform .3s}.card:hover .photo img{transform:scale(1.03)}.card-content{padding:27px 25px 30px;display:flex;flex-direction:column;flex:1}.label{font-size:10px;letter-spacing:.13em;color:#668076;text-transform:uppercase;font-weight:800}.card h2{font:normal 35px Georgia,serif;letter-spacing:-.035em;line-height:1.12;margin:17px 0}.card h2>span{float:right;font:20px Arial,sans-serif}.card p{color:#64746d;font-size:13px;line-height:1.8;margin:0 0 30px}.cta{font-weight:750;font-size:12px;margin-top:auto;border-top:1px solid #e6e9e4;padding-top:18px}.cta>span{margin-left:8px}footer{border-top:1px solid #dfe3dd;padding:30px 0;font-size:12px;color:#66766d}footer .wrap{display:flex;justify-content:space-between;gap:30px}footer a{text-decoration:underline}@media(max-width:850px){.grid{grid-template-columns:1fr 1fr}.photo{height:225px}main{padding:60px 0}}@media(max-width:600px){.wrap{width:calc(100% - 34px)}.grid{grid-template-columns:1fr}h1{font-size:52px}.photo{height:240px}footer .wrap{flex-direction:column;gap:6px}.top .wrap{align-items:center}.top a:last-child{text-align:right}}
</style></head><body><header class="top"><div class="wrap"><a href="./" class="logo">DigiPixel<span>.</span></a><a href="https://digipixel.uk/" rel="noopener" target="_blank">Our website ↗</a></div></header><main><div class="wrap"><div class="kicker">Practical websites, big personality</div><h1>Three different businesses.<br>Three ways to stand out.</h1><p>A small collection of original DigiPixel website concepts, designed around what local and independent businesses actually need: to look great, explain what they do and make it easy for customers to get in touch.</p><div class="grid">''' + cards + '''</div></div></main><footer><div class="wrap"><span>Concepts only. These are fictional example businesses, not customer case studies.</span><span><a href="https://digipixel.uk/" rel="noopener" target="_blank">Built by DigiPixel ↗</a></span></div></footer></body></html>'''
(DST/"index.html").write_text(page)
(DST/"404.html").write_text(page.replace("<title>DigiPixel | Three affordable website concepts</title>","<title>Page not found | DigiPixel concepts</title>"))
(DST/"robots.txt").write_text("User-agent: *\nDisallow: /\n")
(DST/".nojekyll").write_text("")
print("EXPORTED",len(list(DST.rglob("index.html"))),"pages and",len(list(DST.rglob("*.jpg"))),"photos to",DST)
