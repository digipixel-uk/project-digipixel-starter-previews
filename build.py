#!/usr/bin/env python3
"""Three genuinely separate, responsive DigiPixel starter design systems.

These sites demonstrate different visual design directions, not different skins.
They intentionally do not collect visitor data. Each demonstration business is fictional.
"""
from pathlib import Path
from html import escape as esc
from content_reference import DATA, photo_download
import shutil

ROOT=Path(__file__).resolve().parent
PUBLIC=ROOT/"public"
PAGES=["home","services","about","contact"]
NAV_LABELS={"home":"Home","services":"Services","about":"About","contact":"Contact"}

def link(page):
 return "/" if page=="home" else "/"+page+"/"

def pic(file, alt, extra=""):
 return '<img src="/assets/'+file+'" alt="'+esc(alt)+'" loading="lazy" '+extra+'>'

def action(text, href="/contact/", cls="btn"):
 return '<a class="'+cls+'" href="'+href+'">'+esc(text)+'</a>'

def menu(slug, page):
 labels={
  "alder":{"home":"Home","services":"What we do","about":"Our approach","contact":"Get a quote"},
  "fieldnote":{"home":"Home","services":"How we help","about":"The studio","contact":"Let's talk"},
  "sunday":{"home":"Home","services":"The menu","about":"Our world","contact":"Get in touch"}
 }[slug]
 return "".join('<a class="nav-link'+(" is-current" if p==page else "")+'" href="'+link(p)+'"'+(' aria-current="page"' if p==page else "")+'>'+labels[p]+'</a>' for p in PAGES)

def nav(slug, page):
 links=menu(slug,page)
 if slug=="alder":
  return """
 <div class="site-strip"><span>Independent home renovations in Wiltshire</span><span>DigiPixel website design demonstration</span></div>
 <header class="trade-header"><div class="frame trade-nav">
   <a class="trade-logo" href="/" aria-label="Alder and Stone home">ALDER <span>&</span> STONE<span class="logo-line">HOME RENOVATIONS</span></a>
   <button class="menu-toggle" aria-expanded="false" aria-controls="main-navigation" type="button"><span class="menu-toggle-lines"><i></i><i></i><i></i></span>Menu</button>
   <nav class="nav" id="main-navigation" aria-label="Main navigation">"""+links+"""<a class="nav-button" href="/contact/">REQUEST A QUOTE</a></nav>
 </div></header>"""
 if slug=="fieldnote":
  return """
 <header class="field-header"><div class="field-wrap field-nav">
  <a class="field-logo" href="/" aria-label="Fieldnote home">fieldnote<span class="field-dot">.</span><small>THE BOOKKEEPING STUDIO</small></a>
  <button class="menu-toggle" type="button" aria-controls="main-navigation" aria-expanded="false">Menu <span class="menu-toggle-lines"><i></i><i></i><i></i></span></button>
  <nav class="nav" id="main-navigation" aria-label="Main navigation">"""+links+"""<a class="nav-button" href="/contact/">Start a conversation</a></nav>
 </div></header>"""
 return """
 <div class="salon-note"><span>Sunday & Sage / Independent hair studio</span><span>A DigiPixel design demonstration</span></div>
 <header class="salon-header"><div class="salon-wrap salon-nav">
  <a class="salon-logo" href="/" aria-label="Sunday and Sage home">sunday <em>&</em> sage</a>
  <button class="menu-toggle" aria-expanded="false" aria-controls="main-navigation" type="button">Menu <span class="menu-toggle-lines"><i></i><i></i><i></i></span></button>
  <nav class="nav" id="main-navigation" aria-label="Main navigation">"""+links+"""<a class="nav-button" href="/contact/">Ask about a visit</a></nav>
 </div></header>"""

def footer(slug):
 if slug=="alder":
  return """<footer class="trade-footer">
  <div class="frame trade-footer-grid"><div><a href="/" class="footer-brand">ALDER & STONE</a><p>Better spaces. Straight answers.<br>Wiltshire home renovation concept.</p></div>
   <div><strong>Explore</strong><a href="/services/">Services</a><a href="/about/">About</a><a href="/contact/">Get a quote</a></div>
   <div><strong>Next step</strong><p>Got a project in mind?</p><a href="/contact/" class="footer-contact">START YOUR ENQUIRY</a></div></div>
  <div class="frame footer-legal">Fictional business. Photos are illustrative, not evidence of completed projects. No enquiries are collected. <a href="https://digipixel.uk/">A DigiPixel website demonstration.</a></div></footer>"""
 if slug=="fieldnote":
  return """<footer class="field-footer"><div class="field-wrap"><div class="field-footer-top">
   <a href="/" class="field-footer-word">fieldnote.</a><div class="field-footer-links"><a href="/services/">Services</a><a href="/about/">Our story</a><a href="/contact/">Get in touch</a></div></div>
  <div class="field-footer-low"><p>A little less admin. A lot more clarity.</p><p>Fictional business; design preview only. No information is sent. Website by <a href="https://digipixel.uk/">DigiPixel</a>.</p></div></div></footer>"""
 return """<footer class="salon-footer"><div class="salon-wrap">
  <div class="salon-footer-top"><div class="salon-footer-brand">sunday <em>&</em> sage</div><div><p>A little time for yourself.</p><a href="/contact/">Get in touch</a></div></div>
  <nav class="salon-footer-nav" aria-label="Footer navigation"><a href="/">Home</a><a href="/services/">The menu</a><a href="/about/">Our world</a><a href="/contact/">Contact</a></nav>
  <div class="salon-footer-legal">Imaginary salon and imagery for a DigiPixel design demonstration. No appointments or enquiries are collected. <a href="https://digipixel.uk/">Made for DigiPixel</a>.</div>
 </div></footer>"""

def document(slug, page, body):
 d=DATA[slug]
 titles={"home":d["name"]+" | "+d["strap"],"services":"Services | "+d["name"],"about":"About | "+d["name"],"contact":"Contact | "+d["name"]}
 descriptions={"home":d["intro"],"services":d["section_intro"],"about":d["promise"],"contact":d["cta_body"]}
 palette={"alder":"#191e1c","fieldnote":"#f8f9f5","sunday":"#f7e5ed"}
 return """<!doctype html><html lang="en-GB"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow,noarchive">
<meta name="theme-color" content='"""+palette[slug]+"""'>
<meta name="description" content='"""+esc(descriptions[page],quote=True)+"""'>
<meta property="og:title" content='"""+esc(titles[page],quote=True)+"""'>
<title>"""+esc(titles[page])+"""</title>
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/site.css"><script src="/assets/site.js" defer></script></head>
<body class='concept concept-"""+slug+" page-"+page+"""'>
<a class="skip-link" href="#main">Skip to content</a>
"""+nav(slug,page)+"""
<main id="main">"""+body+"</main>"+footer(slug)+"""</body></html>"""

def banner_trade(kicker, headline, sub):
 return '<section class="trade-page-title"><div class="frame"><span class="trade-eyebrow">'+kicker+'</span><h1>'+headline+'</h1><p>'+esc(sub)+'</p></div></section>'

def home_trade():
 return """
<section class="trade-hero">
 <div class="trade-hero-picture">"""+pic("hero.jpg","Contemporary home with architectural timber and warm evening lighting", 'fetchpriority="high"')+"""</div>
 <div class="trade-hero-screen"></div>
 <div class="frame trade-hero-content"><div class="trade-hero-text"><span class="trade-eyebrow">WILTSHIRE HOME IMPROVEMENTS</span>
  <h1>GOOD WORK.<br><span>NO DRAMA.</span></h1>
  <p>Properly planned kitchens, bathrooms and home improvements. Clear conversations, considered finishes, and a home that works harder for you.</p>
  <div class="trade-actions">"""+action("TELL US YOUR PLANS")+action("SEE WHAT WE DO","/services/","text-action")+"""</div>
 </div><div class="trade-hero-index"><span>INDEPENDENT THINKING</span><strong>BUILT AROUND YOU</strong></div></div>
</section>
<div class="trade-tape"><div class="frame"><span>CONSIDERED DESIGN</span><span>STRAIGHTFORWARD PROCESS</span><span>EVERYDAY PRACTICALITY</span></div></div>
<section class="trade-what section-space"><div class="frame trade-what-grid">
 <div><span class="trade-eyebrow orange">01 / OUR WORK</span><h2>YOUR SPACE.<br>DONE RIGHT.</h2><p>Whether you're rethinking an entire room or finishing a long-overdue job, we'd start with a proper conversation.</p>"""+action("ALL SERVICES","/services/","text-action dark")+"""</div>
 <div class="trade-service-list">
  <a href="/services/"><span class="service-number">01</span><strong>KITCHENS</strong><span>Fitting & finishing</span></a>
  <a href="/services/"><span class="service-number">02</span><strong>BATHROOMS</strong><span>Refits & wet rooms</span></a>
  <a href="/services/"><span class="service-number">03</span><strong>IMPROVEMENTS</strong><span>Joinery & decorating</span></a>
 </div>
</div></section>
<section class="trade-photos"><div class="frame"><div class="trade-photos-title"><span class="trade-eyebrow">DESIGN INSPIRATION</span><p>Example imagery to show how a trades business could present its work. Not photographs of real Alder & Stone projects.</p></div>
 <div class="trade-photo-grid"><figure>"""+pic("photo-1.jpg","Warm open-plan home interior")+"""<figcaption>BETTER SPACES</figcaption></figure><figure>"""+pic("photo-3.jpg","Modern kitchen design and interior details")+"""<figcaption>THE FINISHING TOUCHES</figcaption></figure></div></div>
</section>
<section class="trade-process section-space"><div class="frame"><div class="trade-process-intro"><span class="trade-eyebrow orange">02 / HOW WE WORK</span><h2>THREE SIMPLE STEPS.</h2></div>
 <ol class="trade-steps"><li><b>01</b><strong>HAVE A CHAT.</strong><p>Tell us what you're planning and what matters most.</p></li><li><b>02</b><strong>GET A PLAN.</strong><p>A clear understanding of the scope and next steps.</p></li><li><b>03</b><strong>MAKE IT HAPPEN.</strong><p>Careful work with attention to the detail.</p></li></ol></div>
</section>"""+trade_cta()

def trade_cta():
 return """<section class="trade-cta"><div class="frame trade-cta-grid"><div><span class="trade-eyebrow">YOUR PROJECT STARTS HERE</span><h2>LET'S GET<br>TO WORK.</h2></div><div><p>Tell us what you're imagining. A good conversation comes first.</p>"""+action("REQUEST A QUOTE")+"</div></div></section>"

def services_trade():
 d=DATA["alder"]
 x=banner_trade("WHAT WE DO","BUILT FOR<br>REAL LIFE.","A clear, practical range of home improvement services.")
 for idx,(title,desc,detail) in enumerate(d["services"],1):
  image="photo-"+str(idx)+".jpg"
  x+='<section class="trade-service-feature"><div class="frame trade-feature-grid"><div class="feature-image">'+pic(image,"Example image of "+title.lower())+'</div><div class="feature-body"><span class="trade-eyebrow orange">SERVICE '+str(idx).zfill(2)+'</span><h2>'+esc(title.upper())+'</h2><p>'+esc(desc)+'</p><div class="feature-detail">'+esc(detail)+'</div>'+action("ASK ABOUT THIS SERVICE")+'</div></div></section>'
 return x+trade_cta()

def about_trade():
 return banner_trade("OUR APPROACH","THE DETAILS<br>MATTER.","A simple, careful approach for your home.")+"""
 <section class="trade-about section-space"><div class="frame trade-about-grid"><div><span class="trade-eyebrow orange">MORE THAN A QUICK FIX</span><h2>GOOD PEOPLE.<br>GOOD PROCESS.<br>GOOD FINISH.</h2><p>On a real trades website, this is the place for the owner's story, their approach to projects and genuine photographs of the team at work.</p><p>This example explains how DigiPixel can show a local builder's expertise without overcomplicating the website.</p>"""+action("TALK ABOUT YOUR PROJECT")+"""</div><div class="trade-about-picture">"""+pic("photo-2.jpg","Contemporary home interior showing detailed finishes")+"""</div></div></section>
 <section class="trade-principle"><div class="frame"><h2>LESS SALES TALK.<br>MORE STRAIGHT ANSWERS.</h2><p>Practical advice, straightforward expectations and work you'd be pleased to come home to.</p></div></section>"""+trade_cta()

def form_markup(slug):
 d=DATA[slug]
 options=''.join('<option value="'+esc(x,quote=True)+'">'+esc(x)+'</option>' for x in d["form_options"])
 return """
<form class="form" data-demo-form novalidate>
 <div class="form-fields">
  <label for="full-name">Your name<input type="text" name="name" id="full-name" autocomplete="name" placeholder="Your name" maxlength="100" required></label>
  <label for="email-address">Email address<input type="email" name="email" id="email-address" autocomplete="email" placeholder="you@example.com" maxlength="254" required></label>
  <label for="type-of-enquiry">"""+esc(d["form_subject"])+"""<select id="type-of-enquiry" name="service" required><option value="">Choose an option</option>"""+options+"""</select></label>
  <label for="message">Your message<textarea name="message" id="message" rows="5" maxlength="2000" required placeholder="Tell us a little more..."></textarea></label>
 </div>
 <button type="submit">Preview the enquiry journey</button>
 <p class="form-disclaimer">Demonstration only. No information is transmitted or stored.</p>
 <p class="form-status" role="status" aria-live="polite" hidden></p>
</form>"""

def contact_trade():
 return banner_trade("START YOUR PROJECT","TELL US<br>YOUR PLANS.","A simple, straightforward route from an idea to the first conversation.")+"""
 <section class="trade-contact section-space"><div class="frame trade-contact-grid">
 <div class="trade-contact-intro"><span class="trade-eyebrow orange">REQUEST AN ENQUIRY</span><h2>NO OBLIGATION.<br>NO COMPLICATIONS.</h2><p>Show customers that you're ready to listen. A genuine client site would send this to the business's approved enquiry system.</p><div class="contact-note"><b>DESIGN PREVIEW</b><p>Alder & Stone is fictional. This form demonstrates a customer enquiry and does not send messages.</p></div></div>
 <div class="trade-form-panel">"""+form_markup("alder")+"""</div></div></section>"""

def home_field():
 return """
<section class="field-hero"><div class="field-wrap field-hero-grid">
 <div class="field-hero-copy"><span class="field-index">01 / MADE FOR SMALL BUSINESS</span>
  <h1>Good books.<br><em>Clear head.</em></h1>
  <p>Bookkeeping that makes the day-to-day easier to understand. Less time untangling the details. More time moving your business forward.</p>
  <div class="field-actions">"""+action("Let's have a conversation")+action("Explore our services","/services/","field-link")+"""</div>
  <div class="field-hero-small">BOOKKEEPING FOR PEOPLE, NOT SPREADSHEETS.</div>
 </div>
 <div class="field-board"><div class="field-board-top"><span>YOUR BUSINESS, AT A GLANCE</span><span class="board-code">EXAMPLE VIEW</span></div>
  <div class="board-content"><span class="board-meta">EVERYTHING IN ITS PLACE</span><h2>Make sense of<br>the month.</h2>
  <div class="board-visual" aria-hidden="true"><div class="bar bar1"></div><div class="bar bar2"></div><div class="bar bar3"></div><div class="bar bar4"></div><div class="bar bar5"></div><div class="bar bar6"></div></div>
  <div class="board-list"><div><span>Records</span><strong>Organised</strong></div><div><span>Invoices</span><strong>Under control</strong></div><div><span>Reports</span><strong>Easy to follow</strong></div></div></div>
 </div>
</div></section>
<section class="field-intro"><div class="field-wrap field-intro-grid"><span class="field-index">LESS ADMIN. MORE HEADSPACE.</span><h2>Running a business is enough work already.</h2><p>Keeping your records in order shouldn't take your evenings. We make the numbers easier to work with, in plain English and at your pace.</p></div></section>
<section class="field-services"><div class="field-wrap"><div class="field-section-head"><span class="field-index">02 / THE PRACTICAL STUFF</span><h2>The support you <em>actually</em> need.</h2></div>
 <div class="field-lines"><a href="/services/"><span>01</span><strong>Day-to-day bookkeeping</strong><p>Transactions, records and the pieces that keep business running.</p></a>
 <a href="/services/"><span>02</span><strong>Invoices and expenses</strong><p>Smaller headaches and better processes for everyday admin.</p></a>
 <a href="/services/"><span>03</span><strong>Useful reporting</strong><p>Clarity on where things stand and what deserves attention.</p></a></div>
 <div class="field-services-link">"""+action("Learn about the services","/services/","field-link")+"</div></div></section>"+"""
<section class="field-feature"><div class="field-wrap field-feature-grid">
 <div class="field-feature-image">"""+pic("photo-1.jpg","Small business owners working collaboratively in an office")+"""</div>
 <div class="field-feature-copy"><span class="field-index">03 / GOOD COMPANY</span><h2>Questions are<br>always welcome.</h2><p>We're people first and bookkeepers second. Clear answers, a bit of patience and a practical approach can make a world of difference.</p>"""+action("Meet Fieldnote","/about/","field-link")+"""</div>
</div></section>"""+field_cta()

def field_cta():
 return """<section class="field-cta"><div class="field-wrap field-cta-grid"><span>LET'S MAKE IT SIMPLER.</span><div><h2>More time for the good stuff.</h2><p>Tell us about your business, and we'll start with a conversation.</p></div>"""+action("Start here")+"</div></section>"

def field_title(index,title,caption):
 return '<section class="field-page-intro"><div class="field-wrap"><span class="field-index">'+index+'</span><h1>'+title+'</h1><p>'+esc(caption)+'</p></div></section>'

def services_field():
 d=DATA["fieldnote"]
 items=""
 for idx,(t,desc,detail) in enumerate(d["services"],1):
  items+='<article class="field-service-entry"><span class="field-entry-index">'+str(idx).zfill(2)+'</span><div><h2>'+esc(t)+'</h2><p>'+esc(desc)+'</p><small>'+esc(detail)+'</small></div></article>'
 return field_title("HOW WE CAN HELP","Everything in<br><em>good order.</em>","Friendly, structured bookkeeping for small businesses.")+"""
 <section class="field-service-page"><div class="field-wrap field-service-grid"><div class="field-service-side"><span class="field-index">A SIMPLER WAY TO WORK</span><p>Careful records, useful information and a dependable point of contact. No unnecessary complications.</p>"""+pic("photo-4.jpg","Notes and paperwork used for business planning")+"""</div><div class="field-service-entries">"""+items+"""</div></div></section>"""+field_cta()

def about_field():
 return field_title("THE APPROACH","A calmer way<br><em>to work.</em>","Helpful, considered support that makes business feel manageable.")+"""
 <section class="field-about"><div class="field-wrap field-about-grid">
 <div><span class="field-index">WHY WE DO IT</span><h2>Being organised shouldn't feel complicated.</h2><p>Fieldnote is a fictitious practice created as a demonstration of how a small independent accountant or bookkeeper could introduce themselves online.</p><p>On a real business website this area would feature the team's authentic background, qualifications and approach. No testimonials or figures are invented here.</p></div>
 <div class="field-about-visual">"""+pic("photo-2.jpg","Open-plan workspace with light interiors")+"""<span>GOOD WORK STARTS WITH CLEAR THINKING.</span></div></div></section>
 <section class="field-values"><div class="field-wrap"><h2>Plain English is a good place to start.</h2><div class="field-values-grid">
  <div><b>01</b><h3>Less jargon</h3><p>Explanations that make sense without a glossary.</p></div>
  <div><b>02</b><h3>More confidence</h3><p>Understand what's happening, instead of guessing.</p></div>
  <div><b>03</b><h3>Better headspace</h3><p>Make room for the work that brought you here.</p></div></div></div></section>"""+field_cta()

def contact_field():
 return field_title("SAY HELLO","Let's make<br><em>this easier.</em>","It all starts with a simple conversation.")+"""
<section class="field-contact"><div class="field-wrap field-contact-grid"><div class="field-contact-aside"><span class="field-index">A FRESH START</span><h2>A note from<br>you is enough.</h2><p>In a real website, an enquiry would go directly to the business. This example has no receiving mailbox and stores no information.</p><div class="field-callout"><strong>THIS IS A DESIGN DEMONSTRATION</strong><span>Fieldnote isn't a real bookkeeping provider.</span></div></div>
<div class="field-form-panel">"""+form_markup("fieldnote")+"""</div></div></section>"""

def home_salon():
 return """
<section class="salon-hero"><div class="salon-wrap salon-hero-grid">
 <div class="salon-hero-copy"><span class="salon-label">GOOD HAIR, YOUR WAY</span><h1>Your hair.<br><em>Your kind</em><br>of day.</h1><p>Great cuts, lovely colour and a little time to yourself. Welcome to your new happy place.</p>"""+action("SEE THE MENU","/services/","salon-pill")+"""</div>
 <div class="salon-hero-images">
  <div class="salon-portrait">"""+pic("photo-3.jpg","Beauty editorial portrait with styled hair", 'fetchpriority="high"')+"""</div>
  <div class="salon-image-slab">"""+pic("photo-1.jpg","Bright modern hair studio")+"""</div>
  <div class="salon-image-caption">THE PERFECT KIND OF RESET</div>
 </div></div>
 <div class="salon-hero-caption"><div class="salon-wrap">INDEPENDENT HAIR STUDIO <span>TAKE SOME TIME FOR YOURSELF</span></div></div>
</section>
<section class="salon-services"><div class="salon-wrap">
 <div class="salon-section-header"><span class="salon-label">THE LITTLE LUXURIES</span><h2>Come for the hair.<br><em>Stay for the feeling.</em></h2></div>
 <div class="salon-menu">
  <a href="/services/"><span class="salon-menu-no">01</span><strong>CUT & FINISH</strong><span>Find your shape</span><b>EXPLORE</b></a>
  <a href="/services/"><span class="salon-menu-no">02</span><strong>COLOUR & CARE</strong><span>Something fresh</span><b>EXPLORE</b></a>
  <a href="/services/"><span class="salon-menu-no">03</span><strong>THE FINISHING TOUCH</strong><span>A little extra</span><b>EXPLORE</b></a>
 </div></div></section>
<section class="salon-interlude"><div class="salon-wrap salon-interlude-grid">
 <div class="salon-image-large">"""+pic("photo-2.jpg","Hair stylist working with a client")+"""</div>
 <div class="salon-interlude-copy"><span class="salon-label">SOMETHING ABOUT US</span><h2>Come as<br>you <em>are.</em></h2><p>A hair appointment should feel like your time. No rush, no pressure. Just good hair and good company.</p>"""+action("OUR WORLD","/about/","salon-pill light")+"</div></div></section>"+"""
<section class="salon-gallery"><div class="salon-wrap"><span class="salon-label">IN THE STUDIO</span><h2>A look around.</h2><div class="salon-gallery-grid"><div>"""+pic("hero.jpg","Bright hair salon with styling stations")+"""</div><div>"""+pic("photo-4.jpg","Modern professional hair salon interior")+"""</div></div><p>Example imagery selected to illustrate the design. Sunday & Sage is not a real operating salon.</p></div></section>"""+salon_cta()

def salon_cta():
 return """<section class="salon-cta"><div class="salon-wrap salon-cta-grid"><div><span class="salon-label">YOUR NEXT GOOD HAIR DAY</span><h2>Make a little<br><em>space for you.</em></h2></div>"""+action("SAY HELLO","/contact/","salon-pill")+"</div></section>"

def salon_title(kicker, h, p):
 return '<section class="salon-page-intro"><div class="salon-wrap"><span class="salon-label">'+kicker+'</span><h1>'+h+'</h1><p>'+esc(p)+'</p></div></section>'

def services_salon():
 d=DATA["sunday"]
 x=salon_title("THE TREATMENT MENU","The good <em>stuff.</em>","A few moments worth making time for.")
 for idx,(t,desc,detail) in enumerate(d["services"],1):
  file="photo-"+str(idx)+".jpg"
  x+='<section class="salon-service-item"><div class="salon-wrap salon-service-grid"><div class="salon-service-photo">'+pic(file,"Illustrative salon service: "+t)+'</div><div class="salon-service-copy"><span class="salon-label">TREATMENT 0'+str(idx)+'</span><h2>'+esc(t)+'</h2><p>'+esc(desc)+'</p><small>'+esc(detail)+'</small>'+action("ASK ABOUT THIS","/contact/","salon-pill")+'</div></div></section>'
 return x+salon_cta()

def about_salon():
 return salon_title("OUR WORLD","Nice to <em>meet you.</em>","Your time, your style, your kind of place.")+"""
<section class="salon-about"><div class="salon-wrap salon-about-grid"><div class="salon-about-main">"""+pic("photo-1.jpg","Bright salon styling chairs")+"""</div>
<div class="salon-about-copy"><span class="salon-label">A LITTLE ABOUT US</span><h2>Good hair is<br>personal.</h2><p>We love the small things: a good chat, a thoughtful consultation and that feeling when you walk out with a little more confidence.</p><p>Sunday & Sage is a fictitious studio. This demonstration shows how a small salon might tell its story, rather than claiming real stylists or customer reviews.</p>"""+action("EXPLORE THE MENU","/services/","salon-pill light")+"</div></div></section>"+salon_cta()

def contact_salon():
 return salon_title("LET'S TALK HAIR","Hello, <em>lovely.</em>","Tell us what you have in mind.")+"""
<section class="salon-contact"><div class="salon-wrap salon-contact-grid"><div class="salon-contact-picture">"""+pic("photo-3.jpg","Editorial portrait with styled hair")+"""<p>GOOD HAIR, GOOD COMPANY.</p></div>
<div class="salon-contact-form"><span class="salon-label">GET IN TOUCH</span><h2>Your next good hair day starts here.</h2><p>This is a fictional salon website. The following form demonstrates a contact journey and doesn't send or store any information.</p>"""+form_markup("sunday")+"""</div></div></section>"""

HOMES={"alder":home_trade,"fieldnote":home_field,"sunday":home_salon}
SERVICES={"alder":services_trade,"fieldnote":services_field,"sunday":services_salon}
ABOUT={"alder":about_trade,"fieldnote":about_field,"sunday":about_salon}
CONTACT={"alder":contact_trade,"fieldnote":contact_field,"sunday":contact_salon}

def build_all():
 for slug in DATA:
  dst=PUBLIC/slug
  assets=dst/"assets"
  assets.mkdir(parents=True,exist_ok=True)
  for i,photo in enumerate([DATA[slug]["hero"]]+DATA[slug]["images"]):
   photo_download(slug,i,photo)
  shutil.copyfile(ROOT/"styles"/(slug+".css"),assets/"site.css")
  shutil.copyfile(ROOT/"shared"/"site.js",assets/"site.js")
  body={page:builder() for page,builder in [
   ("home",HOMES[slug]),("services",SERVICES[slug]),("about",ABOUT[slug]),("contact",CONTACT[slug])]}
  for page in PAGES:
   dest=dst if page=="home" else dst/page
   dest.mkdir(parents=True,exist_ok=True)
   (dest/"index.html").write_text(document(slug,page,body[page]))
  if slug=="alder": notfound=banner_trade("NOT FOUND","WRONG<br>TURN.","That page isn't available.")+trade_cta()
  elif slug=="fieldnote": notfound=field_title("NOT FOUND","A little off<br><em>track.</em>","That page doesn't exist.")+field_cta()
  else: notfound=salon_title("NOT FOUND","Wrong <em>turn.</em>","Let's find your way back.")+salon_cta()
  (dst/"404.html").write_text(document(slug,"home",notfound).replace("<title>"+esc(DATA[slug]["name"]+" | "+DATA[slug]["strap"])+"</title>","<title>Page not found | "+esc(DATA[slug]["name"])+"</title>"))
  (dst/"robots.txt").write_text("User-agent: *\nDisallow: /\n")
  print("Built",slug,"with independently structured layouts and",len(body),"pages")
 # Keep a simple local index, with no false claims about brands.
 (PUBLIC/"index.html").write_text('<!doctype html><html lang="en"><head><meta name="robots" content="noindex"><meta name="viewport" content="width=device-width,initial-scale=1"><title>DigiPixel design previews</title></head><body><main><h1>DigiPixel budget design previews</h1><ul><li><a href="/alder/">Alder & Stone</a></li><li><a href="/fieldnote/">Fieldnote</a></li><li><a href="/sunday/">Sunday & Sage</a></li></ul></main></body></html>')

if __name__=="__main__":
 build_all()
