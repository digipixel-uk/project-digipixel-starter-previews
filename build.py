#!/usr/bin/env python3
"""Build three isolated DigiPixel budget website concept previews.
Illustrative businesses only; no lead collection or false reviews.
"""
from pathlib import Path
from html import escape as e
from urllib.request import urlopen, Request
import json
import os

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "public"
PHOTO_BASE = "https://images.unsplash.com/"
DATA = {
 "alder": {
  "name":"Alder & Stone", "strap":"Home renovations", "sector":"Trades & home improvements",
  "place":"Wiltshire", "kicker":"Thoughtful renovation. Beautifully finished.",
  "headline":"A better home starts with good people.",
  "intro":"Kitchens, bathrooms and the finishing touches that turn everyday spaces into somewhere you love to be.",
  "micro":"Made for real homes", "proof":["Kitchens designed around you","Bathrooms built to last","A straightforward process"],
  "hero":"photo-1600585154340-be6161a56a0c",
  "images":["photo-1600566753086-00f18fb6b3ea","photo-1600607687920-4e2a09cf159d","photo-1600566752355-35792bedcfea","photo-1600585152915-d208bec867a1"],
  "section_kicker":"What we can do", "section_head":"The details make the difference.",
  "section_intro":"Big renovation or small upgrade, every job starts with listening and ends with the finishing touches.",
  "services":[
   ("Kitchen renovations","A kitchen that works beautifully from the first coffee to the last plate away.","Layout planning, fitting and finishing"),
   ("Bathrooms & wet rooms","Calm, practical spaces with thoughtful storage and timeless finishes.","Refits, tiling and fixtures"),
   ("Home improvements","Refresh a room, rethink a layout or finish those jobs you've been putting off.","Joinery, flooring and decorating")
  ],
  "promise":"Good workmanship. Clear conversations. No unnecessary fuss.",
  "about":"Alder & Stone is a fictional example of a local home improvement business. This concept demonstrates how DigiPixel could give an independent tradesperson a professional online presence without the complexity or cost of a bespoke software project.",
  "values":[("Talk it through","Tell us the result you're looking for and we'll explore the options."),("Plan the work","We'll explain the scope, practicalities and next steps in plain English."),("Make it happen","Care and attention at every stage, from preparation to the final detail.")],
  "faq":[("Can you help with a smaller project?","Absolutely. This demonstration shows how a trades website can welcome both small improvements and full room renovations."),("Where do you work?","The example business is presented as serving Wiltshire and nearby areas. Exact coverage would be set by the real customer."),("How do I get a quote?","This is a design preview. The enquiry form demonstrates the journey but does not submit any details.")],
  "cta":"Let's talk about your space.", "cta_body":"Tell us a little about your plans and see how simple the next step could be.",
  "form_subject":"What are you planning?", "form_options":["Kitchen renovation","Bathroom renovation","Home improvement","Something else"],
  "hero_note":"Beautifully considered spaces, built around everyday life.",
 },
 "fieldnote": {
  "name":"Fieldnote", "strap":"Bookkeeping studio", "sector":"Accountancy & professional services",
  "place":"Small businesses, everywhere", "kicker":"Less paperwork. More headspace.",
  "headline":"Your numbers, finally making sense.",
  "intro":"Clear, considered bookkeeping support for people who would rather be running their business than sorting receipts.",
  "micro":"Bookkeeping, minus the overwhelm", "proof":["Stay on top of the day to day","Make confident decisions","Keep things moving"],
  "hero":"photo-1497366754035-f200968a6e72",
  "images":["photo-1556761175-b413da4baf72","photo-1497366811353-6870744d04b2","photo-1551836022-d5d88e9218df","photo-1554224155-6726b3ff858f"],
  "section_kicker":"What we take care of", "section_head":"The right support changes everything.",
  "section_intro":"Not another spreadsheet to worry about. Just the right information, organised and explained.",
  "services":[
   ("Everyday bookkeeping","Keep income, expenses and records neat, up to date and ready when you need them.","Transaction recording and reconciliation"),
   ("Invoices & expenses","Make it easier to stay organised with clearer processes and fewer loose ends.","Invoice and expense workflows"),
   ("Reports that help","Understand what's happening in your business without having to decode a pile of numbers.","Useful monthly management insights")
  ],
  "promise":"Clear records. Friendly support. More time for what matters.",
  "about":"Fieldnote is an illustrative bookkeeping brand, created to demonstrate an affordable, conversion-focused DigiPixel website for a small professional practice. Its services, imagery and copy are examples, not claims about a trading firm or regulated provider.",
  "values":[("Say hello","Start with a friendly conversation about your business and what's taking your time."),("Find your rhythm","Choose a way of working that suits your business rather than the other way around."),("See things clearly","Keep everything organised and know what needs your attention next.")],
  "faq":[("Is this a real bookkeeping firm?","No. Fieldnote is a DigiPixel website design demonstration."),("Would this design work for an accountant?","Yes. It shows a suitable starting point for accountants, bookkeepers, consultants and other professional services."),("Can I book a call here?","The sample enquiry form demonstrates how a lead journey would work. No information is transmitted.")],
  "cta":"Business feels better with clarity.", "cta_body":"A welcoming first conversation is all it takes to get started.",
  "form_subject":"What do you need a hand with?", "form_options":["Monthly bookkeeping","Invoices and expenses","Management reports","Not sure yet"],
  "hero_note":"Finally, a little room to focus on your business.",
 },
 "sunday": {
  "name":"Sunday & Sage", "strap":"Hair studio", "sector":"Beauty, wellness & appointments",
  "place":"Your neighbourhood studio", "kicker":"A little time, just for you.",
  "headline":"Good hair. Better feeling.",
  "intro":"Considered cuts, effortless colour and the kind of appointment you look forward to all week.",
  "micro":"Your hair, your way", "proof":["Cuts with personality","Colour with care","Time to unwind"],
  "hero":"photo-1560066984-138dadb4c035",
  "images":["photo-1521590832167-7bcbfaa6381f","photo-1605497788044-5a32c7078486","photo-1487412947147-5cebf100ffc2","photo-1633681926035-ec1ac984418a"],
  "section_kicker":"The treatment menu", "section_head":"Come as you are. Leave feeling lovely.",
  "section_intro":"No complicated menus. Just great hair, good conversations and a little room to breathe.",
  "services":[
   ("Cut & finish","Shape, movement and style that feels completely like you.","Consultation, cut and styled finish"),
   ("Colour & care","From soft, lived-in tones to something completely new.","Colour planning and finish"),
   ("A fresh start","A little reset before something special, or simply because you deserve it.","Treatments and occasion styling")
  ],
  "promise":"A considered moment, in the middle of a busy week.",
  "about":"Sunday & Sage is a fictitious beauty studio designed as a DigiPixel preview. It demonstrates the warm visual language, service menus and appointment-led journey that an independent salon can have with a straightforward, affordable website.",
  "values":[("Find your thing","Explore the menu and choose the service that feels right."),("Make time","Pick a time to pause and get a little attention for yourself."),("Leave glowing","An experience with care in every detail, from hello to goodbye.")],
  "faq":[("Can I book an appointment?","Not through this demonstration. The booking experience is illustrative and no appointment is created."),("Are the service prices real?","No. This site uses sample copy and does not present real prices or offers."),("Can a salon connect an existing booking app?","Yes. A finished DigiPixel site can point to an approved booking provider without building a custom booking system.")],
  "cta":"Your next good hair day starts here.", "cta_body":"A calm, simple booking journey is one of the best things a salon website can offer.",
  "form_subject":"What can we help with?", "form_options":["Cut and finish","Colour consultation","Special occasion","Something else"],
  "hero_note":"A little room to breathe. A lovely way to feel.",
 },
}

def image_url(photo, w=1150):
 return f"{PHOTO_BASE}{photo}?w={w}&q=78&fit=crop&auto=format"

def photo_download(slug, i, photo):
 folder = OUT / slug / "assets"
 folder.mkdir(parents=True, exist_ok=True)
 dest = folder / ("hero.jpg" if i == 0 else f"photo-{i}.jpg")
 if dest.exists() and dest.stat().st_size > 15000: return
 request = Request(image_url(photo, 1600 if i == 0 else 1000), headers={"User-Agent":"Mozilla/5.0"})
 try:
  with urlopen(request, timeout=30) as res:
   body = res.read()
   content_type = res.headers.get("Content-Type","")
  if not content_type.startswith("image/") or len(body) < 15000:
   raise RuntimeError(f"unexpected image payload {content_type} {len(body)}")
  dest.write_bytes(body)
  print("photo:", slug, dest.name, len(body))
 except Exception as exc:
  print("PHOTO FAILED", slug, photo, exc)
  if not dest.exists(): raise

def url(page):
 return "/" if page=="home" else f"/{page}/"

def nav(d, slug, page):
 links = [("home","Home"),("services","Services"),("about","Our approach"),("contact","Contact")]
 items = "".join(f'<a href="{url(p)}" class="nav-link{" active" if p == page else ""}" {"aria-current=page" if p==page else ""}>{label}</a>' for p,label in links)
 return f"""
 <div class="demo-bar"><span><strong>DEMO WEBSITE</strong> / DigiPixel design concept for {e(d['sector'])}</span>
   <a href="https://digipixel.uk/" target="_blank" rel="noopener noreferrer">Need a website like this? <span aria-hidden="true">↗</span></a></div>
 <header class="header" id="top"><div class="nav-shell">
   <a class="wordmark" href="/" aria-label="{e(d['name'])} home">
     <span class="mark" aria-hidden="true">{'a' if slug=='alder' else 'f' if slug=='fieldnote' else 's'}</span>
     <span class="logo-copy"><span class="brand">{e(d['name'])}</span><span class="descriptor">{e(d['strap'])}</span></span>
   </a>
   <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-navigation">
     <span class="menu-icon" aria-hidden="true"><span></span><span></span><span></span></span><span>Menu</span>
   </button>
   <nav class="nav" id="site-navigation" aria-label="Primary navigation">{items}
     <a class="nav-cta" href="/contact/">{'Book a visit' if slug=='alder' else 'Start a conversation' if slug=='fieldnote' else 'Get in touch'} <span aria-hidden="true">↗</span></a></nav>
 </div></header>"""

def footer(d):
 return f"""
 <footer class="footer">
  <div class="footer-grid container">
   <div><div class="footer-logo">{e(d['name'])}<span>.</span></div><p>{e(d['hero_note'])}</p></div>
   <div><p class="footer-heading">Explore</p><a href="/">Home</a><a href="/services/">Services</a><a href="/about/">Our approach</a><a href="/contact/">Contact</a></div>
   <div><p class="footer-heading">Say hello</p><p>{e(d['place'])}</p><a href="/contact/">Contact the studio <span aria-hidden="true">↗</span></a></div>
  </div>
  <div class="footer-bottom container"><span>Illustrative brand and content. No real business or booking service.</span><span>A <a href="https://digipixel.uk/" target="_blank" rel="noopener">DigiPixel</a> website concept</span></div>
 </footer>"""

def shell(d, slug, page, main):
 seo={"home":d["headline"],"services":"Services","about":"Our approach","contact":"Get in touch"}
 title=f"{seo[page]} | {d['name']}"
 desc=(d["intro"] if page=="home" else f"Discover the {d['name']} website concept for {d['sector']}.")[:158]
 return f"""<!doctype html>
<html lang="en-GB"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow,noarchive">
<meta name="theme-color" content="{'#202f28' if slug=='alder' else '#183d42' if slug=='fieldnote' else '#492d3c'}">
<meta name="description" content="{e(desc)}"><title>{e(title)}</title>
<meta property="og:type" content="website"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/site.css">
<script defer src="/assets/site.js"></script></head>
<body class="site site--{slug} page--{page}">
<a class="skip-link" href="#main">Skip to main content</a>
{nav(d,slug,page)}
<main id="main">{main}</main>{footer(d)}
</body></html>"""

def btn(label, href="/contact/", cls="button button-primary"):
 return f'<a class="{cls}" href="{href}">{e(label)} <span aria-hidden="true">↗</span></a>'

def eyebrow(txt):
 return f'<span class="eyebrow"><span class="eyebrow-dot"></span>{e(txt)}</span>'

def hero(d,slug):
 if slug=="alder":
  return f"""<section class="hero hero-alder">
  <div class="container hero-alder-grid">
    <div class="hero-copy">{eyebrow(d['kicker'])}
      <h1>A better home starts with <em>good people.</em></h1>
      <p class="lead">{e(d['intro'])}</p>
      <div class="action-row">{btn("Talk about your project")}{btn("Explore our work","/services/","button button-outline")}</div>
      <div class="hero-trust"><span class="sun-icon" aria-hidden="true">✳</span> A simpler way to improve your home</div>
    </div>
    <div class="hero-visual"><img src="/assets/hero.jpg" alt="Modern characterful home exterior with considered architectural finishes" fetchpriority="high">
     <div class="visual-card"><span class="visual-num">01 / 03</span><strong>Space to feel at home.</strong><p>Made for the way you really live.</p></div></div>
  </div></section>"""
 if slug=="fieldnote":
  return f"""<section class="hero hero-fieldnote">
  <div class="container fieldnote-grid">
   <div class="hero-copy">{eyebrow(d["kicker"])}
     <h1>Your numbers,<br><span class="highlight-swoop">finally</span> making sense<span class="period">.</span></h1>
     <p class="lead">{e(d['intro'])}</p>
     <div class="action-row">{btn("Let's get clear")}{btn("See how we help","/services/","button button-outline")}</div>
     <div class="quiet-note"><span aria-hidden="true">✳</span> Friendly support for the way you work.</div>
   </div>
   <div class="fieldnote-photo"><img src="/assets/hero.jpg" alt="Bright welcoming work space with desks and natural light" fetchpriority="high">
    <div class="fieldnote-sticker"><span aria-hidden="true">✦</span><strong>Make space<br>for better.</strong></div></div>
  </div></section>"""
 return f"""<section class="hero hero-sunday">
  <div class="sunday-photo"><img src="/assets/hero.jpg" alt="Bright salon interior with chairs and styling stations" fetchpriority="high"></div>
  <div class="sunday-scrim"></div><div class="container sunday-inner">
   <div class="hero-copy">{eyebrow(d["kicker"])}<h1>Good hair.<br><em>Better feeling.</em></h1>
    <p class="lead">{e(d["intro"])}</p>
    <div class="action-row">{btn("Explore the menu","/services/")}{btn("Come say hello","/contact/","button button-light")}</div>
   </div>
   <span class="sunday-vertical">A place to be yourself · Your neighbourhood studio</span>
  </div>
 </section>"""

def intro_strip(d, slug):
 return '<div class="intro-strip"><div class="container strip-items">'+''.join(
  f'<div><span class="strip-icon" aria-hidden="true">{["✳","◌","↗"][i]}</span><span>{e(text)}</span></div>' for i,text in enumerate(d["proof"])
 )+'</div></div>'

def section_services(d,slug):
 cards=''.join(f"""<article class="service-card">
    <div class="card-index">0{i+1} <span aria-hidden="true">↗</span></div>
    <h3>{e(title)}</h3><p>{e(desc)}</p><span class="service-detail">{e(detail)}</span>
    </article>""" for i,(title,desc,detail) in enumerate(d["services"]))
 return f"""<section class="section services-section" id="services"><div class="container">
  <div class="section-head"><div>{eyebrow(d["section_kicker"])}<h2>{e(d["section_head"])}</h2></div><div><p>{e(d["section_intro"])}</p><a class="text-link" href="/services/">Explore our services <span aria-hidden="true">↗</span></a></div></div>
  <div class="services-grid">{cards}</div>
 </div></section>"""

def editorial(d, slug):
 if slug=="alder":
  head="Your home deserves more than a quick fix."
  body="Good design should work in everyday life, not just look good in photographs. We bring care, practical thinking and attention to the jobs that matter."
  img1="Carefully designed warm-toned home interior"
 elif slug=="fieldnote":
  head="A bit more clarity. A lot less noise."
  body="We're here for the behind-the-scenes work that keeps things running. Thoughtful processes, approachable people and the feeling that someone's got it covered."
  img1="People collaborating around a table at work"
 else:
  head="You look after everyone. Now it's your turn."
  body="More than a trim, it's your chance to unwind. This is a space made for good conversation, thoughtful care and feeling like yourself again."
  img1="Hair styling in progress in a bright studio"
 return f"""<section class="section editorial-section">
  <div class="container editorial-grid">
   <div class="editorial-images"><img src="/assets/photo-1.jpg" loading="lazy" alt="{e(img1)}"><div class="editorial-small"><img src="/assets/photo-2.jpg" loading="lazy" alt="Additional example of this industry and working environment"></div></div>
   <div class="editorial-copy">{eyebrow("A little about us")}<h2>{e(head)}</h2><p>{e(body)}</p>
    <div class="editorial-note"><span aria-hidden="true">✳</span><span>{e(d["promise"])}</span></div>
    {btn("Get to know us","/about/","button button-outline")}</div>
  </div></section>"""

def steps(d):
 blocks=''.join(f"""<div class="step"><span class="step-num">0{i+1}</span><h3>{e(title)}</h3><p>{e(copy)}</p></div>""" for i,(title,copy) in enumerate(d["values"]))
 return f"""<section class="section steps-section"><div class="container">
   <div class="section-head"><div>{eyebrow("The simple process")}<h2>Easy from the first hello.</h2></div><p>No mystery. No long forms to navigate. Just a clear path from here to there.</p></div>
   <div class="step-grid">{blocks}</div></div></section>"""

def cta(d):
 return f"""<section class="cta-section"><div class="container cta-grid"><div>{eyebrow("Let's begin")}<h2>{e(d["cta"])}</h2><p>{e(d["cta_body"])}</p></div>{btn("Get in touch","/contact/","button button-light")}</div></section>"""

def home(d,slug):
 return hero(d,slug)+intro_strip(d,slug)+section_services(d,slug)+editorial(d,slug)+steps(d)+cta(d)

def page_banner(d,title,lead,kicker):
 return f"""<section class="page-banner"><div class="container">{eyebrow(kicker)}<h1>{e(title)}</h1><p>{e(lead)}</p></div></section>"""

def services(d,slug):
 main=page_banner(d,"What we do.",d["section_intro"],d["section_kicker"])
 for i,(title,desc,detail) in enumerate(d["services"]):
  main+=f"""<section class="service-feature {'reverse' if i%2 else ''}"><div class="container feature-grid">
   <div class="feature-photo"><img src="/assets/photo-{i+1}.jpg" alt="Illustrative {e(title.lower())} service photography" loading="lazy"></div>
   <div class="feature-copy">{eyebrow(f"Service 0{i+1}")}<h2>{e(title)}</h2><p>{e(desc)}</p>
    <div class="feature-detail"><span aria-hidden="true">✳</span> {e(detail)}</div>{btn("Ask about this service")}</div></div></section>"""
 return main+cta(d)

def about(d,slug):
 return (page_banner(d,"Good work starts here.",d["promise"],"Our approach")+
  f"""<section class="section about-story"><div class="container story-grid">
    <div class="story-copy">{eyebrow("A thoughtful approach")}<h2>Simple, human and built around you.</h2><p>{e(d['about'])}</p>
     <p>On a real customer website, this is where an authentic business story, team photographs and values would go. The layout is ready to make those things feel personal.</p></div>
    <div class="story-photo"><img src="/assets/photo-4.jpg" alt="Illustrative business lifestyle photograph" loading="lazy"></div>
   </div></section>"""+steps(d)+cta(d))

def contact(d,slug):
 opts=''.join(f'<option value="{e(x)}">{e(x)}</option>' for x in d["form_options"])
 qas=''.join(f'<details><summary>{e(q)} <span aria-hidden="true">+</span></summary><p>{e(a)}</p></details>' for q,a in d['faq'])
 return (page_banner(d,"Come say hello.",d["cta_body"],"Get in touch")+
  f"""<section class="section contact-section"><div class="container contact-grid">
   <div class="contact-left">{eyebrow("A friendly conversation")}<h2>Tell us what you have in mind.</h2>
    <p>This is a sample enquiry page showing how prospective customers can get in touch quickly and easily.</p>
    <div class="sample-disclaimer"><strong>Design preview only</strong><span>This is a fictional business. The form is not connected to email or a CRM, and no details are sent or stored.</span></div>
    <div class="contact-small"><span class="small-symbol" aria-hidden="true">✳</span><span>To get a real website like this, visit <a href="https://digipixel.uk/" target="_blank" rel="noopener">DigiPixel ↗</a></span></div>
   </div>
   <form data-demo-form class="contact-form" novalidate><p class="form-title">What can we help with?</p>
    <div class="form-row"><label>Your name <input type="text" name="name" autocomplete="name" placeholder="e.g. Alex Taylor" required maxlength="100"></label>
    <label>Email address <input type="email" name="email" autocomplete="email" placeholder="alex@example.com" required maxlength="254"></label></div>
    <label>{e(d["form_subject"])} <select name="service" required><option value="">Please select</option>{opts}</select></label>
    <label>A little about your enquiry <textarea name="message" placeholder="Tell us a little about what you're looking for…" required maxlength="2000" rows="5"></textarea></label>
    <button class="button button-primary submit" type="submit">See how an enquiry works <span aria-hidden="true">↗</span></button>
    <p class="form-help">Preview interaction only. Nothing is submitted.</p><p class="form-status" role="status" aria-live="polite" hidden></p>
   </form>
  </div></section>"""+
  f"""<section class="section faq-section"><div class="container"><div class="faq-left">{eyebrow("Good to know")}<h2>A few quick answers.</h2></div><div class="faq-items">{qas}</div></div></section>""")

def favicon(slug):
 colors={"alder":("#273f31","#ede3c7"),"fieldnote":("#1c4a49","#e1eecf"),"sunday":("#573647","#ffcbb4")}
 a,b=colors[slug]
 letter={"alder":"a","fieldnote":"f","sunday":"s"}[slug]
 return f'<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64"><rect width="64" height="64" rx="16" fill="{a}"/><text x="32" y="45" font-family="Georgia,serif" font-size="49" text-anchor="middle" fill="{b}">{letter}</text></svg>'

def build():
 style=(ROOT/"shared"/"site.css").read_text()
 script=(ROOT/"shared"/"site.js").read_text()
 for slug,d in DATA.items():
  path=OUT/slug
  (path/"assets").mkdir(parents=True,exist_ok=True)
  (path/"assets"/"site.css").write_text(style)
  (path/"assets"/"site.js").write_text(script)
  (path/"favicon.svg").write_text(favicon(slug))
  (path/"robots.txt").write_text("User-agent: *\nDisallow: /\n")
  for i,photo in enumerate([d["hero"]]+d["images"]): photo_download(slug,i,photo)
  for page,content in [("home",home(d,slug)),("services",services(d,slug)),("about",about(d,slug)),("contact",contact(d,slug))]:
   target=path if page=="home" else path/page
   target.mkdir(exist_ok=True,parents=True)
   (target/"index.html").write_text(shell(d,slug,page,content))
  (path/"404.html").write_text(shell(d,slug,"home",f'<div class="container notfound"><p>404 · Page not found</p><h1>This page took a different path.</h1>{btn("Back to home","/")}</div>'))
  print("BUILT:",slug, "5 HTML pages", "images:",len(list((path/"assets").glob("*.jpg"))))
 (OUT/"index.html").write_text('<!doctype html><html lang="en"><head><meta name="robots" content="noindex"></head><body><h1>DigiPixel design concepts</h1><ul><li><a href="/alder/">Alder & Stone</a></li><li><a href="/fieldnote/">Fieldnote</a></li><li><a href="/sunday/">Sunday & Sage</a></li></ul></body></html>')
 (ROOT/"manifest.json").write_text(json.dumps({"brand":"DigiPixel","type":"fictional budget WordPress-ready demo design concepts","sites":{k:{"name":v["name"],"sector":v["sector"]} for k,v in DATA.items()}},indent=2))
if __name__=="__main__":build()
