# DigiPixel starter website concepts

Three original demonstration websites for the affordable DigiPixel fixed-scope website offering. These are fictional example businesses, not client projects, live customer testimonials or production booking systems.

## Sites

- Alder & Stone: industrial home renovations website. Dark photographic split hero, oversized condensed block typography, bright orange accents, bold service rows and prominent quotation journey.
- Fieldnote: editorial professional-services website. Quiet Swiss-influenced layout, large serif typography, mock graphical dashboard rather than a photographic hero, information-first service listing and unobtrusive enquiries.
- Sunday & Sage: expressive salon editorial. Lavender and coral, mixed type, layered fashion photography, asymmetrical composition, treatment-list presentation and an entirely separate page architecture.

These are three separate CSS and layout systems, not three colour variants of a common template. The only shared JavaScript is accessible mobile-navigation and deliberately non-transmitting demonstration form behaviour. Each website has four responsive pages: Home, Services, Our approach, Contact, plus a designed 404 page. Mobile menus, semantic navigation, focus states, reduced-motion support, sample form validation and an explicit confirmation that no enquiry is sent are included. All assets are locally hosted. No decorative emoji or star/asterisk glyphs appear on the finished pages. No analytics, cookies, customer data capture or live integrations are enabled. The website is marked as a demonstration, with noindex metadata, robots.txt and server headers.

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

The public/<site> directories are release-ready static review assets. To give the user durable public previews while leaving existing customer previews and production infrastructure untouched, the demos were published through a separate GitHub Pages repository (digipixel-uk/digipixel-budget-previews):

- https://digipixel-uk.github.io/digipixel-budget-previews/ — overview
- https://digipixel-uk.github.io/digipixel-budget-previews/alder/
- https://digipixel-uk.github.io/digipixel-budget-previews/fieldnote/
- https://digipixel-uk.github.io/digipixel-budget-previews/sunday/

Publication is separate from production, explicitly noindex, and contains only fictitious demo content. The permanent dedicated preview node (*.preview.digipixel.uk) remains the preferred future branded preview service when available.

To update and republish after editing source: run python3 build.py and python3 prepare_github_pages.py, review the generated .publish-gh-pages diff, then commit and push in .publish-gh-pages. The exporter retains the deployment repository's .git directory. The native WordPress implementation for paying customers is a later step after design approval.

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

## Design source and thumbnails

Build with `python3 build.py`. The fictional businesses and illustrative photo identifiers live in `content_reference.py`; the independently designed templates live in `build.py` and `styles/{alder,fieldnote,sunday}.css`. Screenshot thumbnails used by the public showcase live in each site's `assets/preview.jpg` and should be regenerated from headless desktop screenshots after substantive visual changes. `tests/smoke.cjs` verifies desktop/mobile layouts, navigation and form behaviour.

## Consistent preview selector (29 October 2026)

The hosted gallery root and local public index now use the shared DigiPixel-branded selector. The design system is maintained in the sibling digipixel-preview-selector project. The contents and links in preview-selector.json are project-specific. Rebuilding with python3 build.py or exporting with python3 scripts/export-pages.py regenerates the selector automatically. Individual concept sites remain deliberately unrelated in their visual design.
