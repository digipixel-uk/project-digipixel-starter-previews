# DigiPixel starter website concepts

Three original demonstration websites for the affordable DigiPixel fixed-scope website offering. These are fictional example businesses, not client projects, live customer testimonials or production booking systems.

## Sites

- Alder & Stone: home renovation / trades. Warm editorial palette, clear service range and quote journey.
- Fieldnote: bookkeeping / professional service. Accessible, calm layout, straightforward explanation of services and lead journey.
- Sunday & Sage: salon / lifestyle. Image-led personality, appointment-led structure and service menu.

Each website has four responsive pages: Home, Services, Our approach, Contact, plus a designed 404 page. Mobile menus, semantic navigation, focus states, reduced-motion support, sample form validation and an explicit confirmation that no enquiry is sent are included. All assets are locally hosted. No analytics, cookies, customer data capture or live integrations are enabled. The website is marked as a demonstration, with noindex metadata, robots.txt and server headers.

## Build / run on Mac

    cd ~/Sites/digipixel-starter-previews
    python3 build.py
    docker compose -f compose.local.yml up -d
    curl -I http://localhost:8771

Local demo URLs:

- http://localhost:8771 — Alder & Stone
- http://localhost:8772 — Fieldnote
- http://localhost:8773 — Sunday & Sage

Caddy on the shared local dev network also maps alder.demo.digipixel.test, fieldnote.demo.digipixel.test, and sunday.demo.digipixel.test (local DNS needed to use hostnames).

## Preview publishing

The public/<site> directories are release-ready static review assets. Any permanent public preview deployment should use the existing dedicated preview node and domain namespace under *.preview.digipixel.uk, with valid TLS, noindex and optional access controls. Do not silently route this through production or replace existing customer previews. The static review assets are distinct from the planned native WordPress implementation for paying DigiPixel clients.

## Images / licence

Images are downloaded at build time from Unsplash and stored locally. The photo IDs, image endpoints and descriptive alt text are in build.py. Unsplash permits commercial use under its licence; these images are illustrative and do not depict actual work by the fictional businesses. Confirm final image suitability and licensing before any customer launch.

## Delivery boundary

These designs are preview concepts. The proposed DigiPixel delivery stack for customer websites is native WordPress with a custom theme, editable content, backups, SEO and a real contact endpoint. Conversion of the approved concepts into WordPress production packages should not be confused with these static demonstrations. No production domains or servers are touched by the local run command.

## Hosted sales previews (28 October 2026)

Live gallery: https://digipixel-uk.github.io/project-digipixel-starter-previews/

- https://digipixel-uk.github.io/project-digipixel-starter-previews/alder/
- https://digipixel-uk.github.io/project-digipixel-starter-previews/fieldnote/
- https://digipixel-uk.github.io/project-digipixel-starter-previews/sunday/

GitHub Pages is configured to publish the main branch's /docs folder. Rebuild it with python3 scripts/export-pages.py after changing design content, commit and push. The hosted gallery, all demo pages, assets, mobile menus and non-sending forms have been verified through HTTPS and a headless mobile Chromium test.

GitHub Pages is an interim, non-production review host only. The normal controlled preview.digipixel.uk environment was not changed because the known SSH host identity of its apparent wildcard target differed from the stored identity. Resolve that out-of-band against the infrastructure provider before provisioning there; do not disable SSH host key checking.
