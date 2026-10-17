# StockScan website

German and English marketing site, hosted at https://nature0ne.github.io/stockscan-website/.
GitHub Pages serves the committed files from `main` at the repository root.

## Content and build

- `scripts/build.py`: bilingual landing and media pages, shared templates and marketing copy.
- `scripts/documents.py`: support, privacy and legal pages. Preserve legal/contact details when refreshing marketing.
- `assets/site.css` and `assets/site.js`: responsive design and progressive gallery controls.
- `marketing/README.md`: image provenance and delivery formats.

```sh
python3 scripts/build.py
python3 scripts/documents.py
python3 scripts/refresh-assets.py --package-only
python3 scripts/check.py
python3 -m http.server 8765 --bind 127.0.0.1
```

Open http://127.0.0.1:8765/. The site has no framework or runtime dependencies, analytics, remote fonts or browser storage. Navigation, language selection and FAQs work without JavaScript. Keep asset URLs relative because Pages hosts this site under `/stockscan-website/`.

## Marketing assets

The October 2026 refresh uses the approved StockScan 1.5.1 marketing material: genuine localized iPhone/iPad captures, corrected review/export scenes and forest/mint artwork. The iPhone/iPad workflow shown is also available in the published 1.5.0 app. These pages do not announce the draft 1.5.1 as released.

Public media downloads contain the current German/English artwork and copy. `scripts/refresh-assets.py` creates WebP delivery images and the curated media archive; see its help and the provenance notes before regenerating from the app repository. `--package-only` repackages committed assets after copy changes. The original captures are never retouched to change app behavior. The workshop image is an illustrative AI image, identified in its alt text.

## Verification

```sh
python3 scripts/check.py
# Playwright and an installed Google Chrome are required by the existing browser checks:
node scripts/browser-check.cjs
node scripts/workflow-check.cjs
```

Browser checks cover German and English, 320/390/768/1440px layouts, image loads, overflow, language switching, native FAQs, gallery controls, media downloads and no-JavaScript behavior. Workflow checks inspect card text/image overlap at eight widths. Use `SITE_URL` to check the deployed site. Reports and screenshots are ignored under `artifacts/`.

## Product boundaries

Free: one active inventory, 100 distinct items, checklist and master-data import, completion/history, unlimited CSV export and single-item Watch counting. Pro removes Free list/item limits and adds XLSX export, Fast Scan for known items, templates, target/actual comparisons, history/difference reports, Watch queues and optional private iCloud sync between the user's own devices. Family Sharing shares the entitlement, not inventory data. Imported master data stays local. The app supports eight languages; the website supports German and English. Minimum systems: iOS/iPadOS 18 and watchOS 10.

Website publication does not submit or release a version in App Store Connect. App source files and the older local website checkout are outside this change.
