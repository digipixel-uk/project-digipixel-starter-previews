#!/usr/bin/env python3
"""Reference data and illustrative image retrieval for three example websites.
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

