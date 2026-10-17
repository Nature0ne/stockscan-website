# StockScan website media · German and English

Updated 17 October 2026 from the owner's approved `StockScan/marketing/1.5.1/open-assets` campaign. The campaign identifier describes the source material, not an announcement that a new App Store version has been released. The forest-green and mint artwork uses real native app captures and fictional workshop/service-van sample data.

## Downloads

- `assets/marketing/StockScan-Media-DE-EN-2026-10-17.zip`: curated DE/EN website media kit. Contains 24 full-resolution iPhone/iPad screenshot compositions, four original header/search creatives, eight web/social derivatives, two text files, source provenance and the original Apple frame license. File paths in this document are relative to the website root; the ZIP groups its images under `screenshots/`, `creatives/` and `web-social/`, with copy, license and provenance at the root.
- `01-inventory-{de,en}-1320x2868.png` through `06-lists-{de,en}-1320x2868.png`: six iPhone compositions per language, 1320 × 2868, copied byte-for-byte from the approved exports.
- `ipad-{de,en}-{01-inventory,02-quantity,03-review,04-data,05-export,06-lists}-2064x2752.png`: six iPad compositions per language, 2064 × 2752, copied byte-for-byte.
- `header-{de,en}.png`: original 3840 × 1646 header creatives.
- `search-{de,en}.png`: original 3840 × 2560 search creatives.
- `release-banner-{de,en}.png`: 1600 × 900, complete header artwork contained in a matching green canvas.
- `social-{de,en}.jpg`: 1200 × 630, complete header artwork contained in a matching green canvas.
- `square-{de,en}-1080x1080.png`: complete search artwork contained in a square green canvas.
- `story-{de,en}-1080x1920.png`: complete first iPhone composition contained in a portrait green canvas.
- `copy-{de,en}.txt`: reusable, version-neutral promotional copy.
- `manifest.json`: exact bytes, SHA-256 checksums and image dimensions for every public media file. `provenance.json` records source files, source checksums and transformations, including native-screen mapping.

The website's `assets/screens/*.webp` files use the native captures directly, without marketing headlines or rendered device frames. iPhone images are 660 × 1435; iPad images are 1000 × 1333. Their source captures are respectively 1206 × 2622 and 2064 × 2752. Conversion resizes and compresses the image; it does not retouch UI or invent app state. Keep the website's CSS device frames separate.

For existing website URLs, six stable motif names are retained. `01-inventory` maps to the native item-entry capture; `02-quantity` to the quantity calculator; `03-review` to required-item review; `04-data` to data/import settings; `05-export` to the export-format chooser; and `06-lists` to completion history. The first capture follows manual item-number entry and does not show a live camera scan. The export chooser does not prove completion or display a finished report. History is not a list overview.

## Rebuild and provenance

`python3 scripts/refresh-assets.py --source /path/to/StockScan/marketing/1.5.1` refreshes source copies, WebP delivery files, social derivatives, the curated ZIP and its manifest. Pillow is required. After `scripts/build.py` updates promotional copy, run `python3 scripts/refresh-assets.py --package-only` to rebuild the ZIP and checksums using the committed website media; no app repository is needed for that command.

The original campaign captures were produced with StockScan 1.5.1 build 36, from source commit `cb6905819cf817def6db2790f80ccb494a867605`. Capture provenance records Xcode 27.1 and the iOS Simulator 27.1 SDK. The public website uses these approved captures without making a new-version release claim. Original full-resolution assets remain byte-identical to campaign exports. The kit is a focused website/media selection, not the complete eight-language App Store upload archive.

Product frames in the original campaign come from [Apple Design Resources](https://developer.apple.com/design/resources/), downloaded 16 October 2026: iPhone 17 Black Portrait and iPad Pro (M5) 13-inch Space Black Portrait. Follow Apple's [Marketing Resources and Identity Guidelines](https://developer.apple.com/app-store/marketing/guidelines/). The unmodified original license is included as `apple-frames-license.rtf`. The campaign's `APPLE-FRAMES.md` and `devices.json` retain full frame provenance. Derived social images scale the complete approved composition uniformly and do not crop or alter product imagery.

## Workshop image

`../assets/workshop.webp` is an AI-generated supporting editorial image, generated with the built-in imagegen tool on 13 September 2026. It is decorative context, not a photograph of a real customer, endorsement or app screenshot. The website's alt text identifies it as illustrative AI imagery.

Original generation file: `exec-9d34332c-0927-4efd-9317-a828d0ea07a5.png`. The lossless copy is kept locally as ignored `assets/workshop.png`; the WebP copy is committed and fully self-contained.

Exact generation prompt:

> Use case: photorealistic-natural. Asset type: premium editorial landscape photography for the StockScan inventory app website, wide 3:2 composition. Primary request: an authentic small European workshop inventory shelf with carefully arranged dark forest green open-front parts bins containing bolts, washers and fittings, plain kraft boxes with simple small barcode labels without legible brand names, brushed metal shelf, subtle wooden workbench edge. No people, no phones, no screens. Beautiful restrained natural window light, tactile paper and metal details, rich forest green and warm ivory palette, calm organized working environment, high-end architectural/editorial photography, realistic and not glossy CGI. Composition: closer, generous clean cream wall and natural shadow on left third, shelves with parts on the right two-thirds. No overlay text, no logos, no watermark. This is a supporting atmosphere image, the app screenshots will be placed separately as actual HTML images.

## Content boundaries

Do not add fixed pricing, unconditional free-trial promises, performance guarantees, customer counts or invented reviews. Label XLSX, Fast Scan, target/actual comparison, templates, history comparison, difference reports, full Watch lists and private iCloud sync as Pro. Import and CSV export are available free. Family Sharing shares Pro entitlement, not inventory data. Core counting works offline; Apple services need a connection. Apple Intelligence and Dynamic Island are availability-dependent.

No social post, newsletter or message is sent by these scripts. App Store review/release remains separate from publishing this website.
