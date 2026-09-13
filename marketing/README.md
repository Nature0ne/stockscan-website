# StockScan 1.4 marketing materials

## Deliverables

- `../assets/marketing/StockScan-1.4.0-Marketing.zip`: complete downloadable kit with 24 real-app Store compositions (6 per device and language), original release banners, contact sheets and web/social additions.
- `release-banner-{de,en}.png`: 1600 × 900, original app release compositions.
- `social-{de,en}.jpg`: 1200 × 630, link-preview graphics based on the original release composition.
- `square-{de,en}-1080x1080.png`: new square social posts.
- `story-{de,en}-1080x1920.png`: new portrait story/status posts.
- `copy-{de,en}.txt`: short description, launch post, workshop post and Pro post.
- `manifest.json`: file sizes and SHA-256 checksums.
- `source/`: editable HTML sources for the square and story compositions. Recreate with `python3 scripts/marketing.py`, then `node scripts/render-marketing.cjs` from the root while serving the site locally.

All localized app screenshots, the app icon, original release banners and the initial Store kit come from the owner's StockScan app repository, `marketing/1.4.0`, prepared and verified on 12–13 September 2026. iPhone images were captured from the real app on iPhone 17; iPad images from iPad Pro 13-inch (M5). Sample inventory data is fictional. Full-resolution Store assets are preserved inside the ZIP. Website WebP versions are delivery-size conversions of these captures, never generated UI.

The new social layouts are rendered from HTML with macOS Avenir Next and Georgia. They use the same real app captures. Conversion and compression are performed with sharp; no product content is changed. The 24 original screenshot compositions can be rebuilt with the app repository's `marketing/1.4.0/render.py`.

## Workshop image

`../assets/workshop.webp` is an AI-generated supporting editorial image, generated with the built-in imagegen tool on 13 September 2026. It is decorative context, not a photograph of a real customer, endorsement or app screenshot. The website's alt text identifies it as illustrative AI imagery.

Original generation file: `exec-9d34332c-0927-4efd-9317-a828d0ea07a5.png`. The lossless copy is kept locally as ignored `assets/workshop.png`; the WebP copy is committed and fully self-contained.

Exact generation prompt:

> Use case: photorealistic-natural. Asset type: premium editorial landscape photography for the StockScan inventory app website, wide 3:2 composition. Primary request: an authentic small European workshop inventory shelf with carefully arranged dark forest green open-front parts bins containing bolts, washers and fittings, plain kraft boxes with simple small barcode labels without legible brand names, brushed metal shelf, subtle wooden workbench edge. No people, no phones, no screens. Beautiful restrained natural window light, tactile paper and metal details, rich forest green and warm ivory palette, calm organized working environment, high-end architectural/editorial photography, realistic and not glossy CGI. Composition: closer, generous clean cream wall and natural shadow on left third, shelves with parts on the right two-thirds. No overlay text, no logos, no watermark. This is a supporting atmosphere image, the app screenshots will be placed separately as actual HTML images.

## Content boundaries and checks

Use launch wording as explicitly requested by the owner. Do not add fixed pricing, unconditional free-trial promises, performance guarantees, customer counts or invented reviews. Label XLSX, Fast Scan, target/actual comparison, templates, history comparison, difference reports, full Watch lists and private iCloud sync as Pro. Family Sharing shares only Pro entitlement, not inventory data. Core counting works offline; Apple services need a connection. Apple Intelligence and Dynamic Island are availability-dependent.

The technical privacy update reflects the code's private CloudKit opt-in, on-device import assistance, diagnostic sharing and local data. Existing public controller/contact details are retained. Reference sources consulted on 13 September 2026:

- App listing: https://apps.apple.com/app/id6760256901
- § 5 DDG: https://www.gesetze-im-internet.de/ddg/__5.html
- GitHub hosting privacy: https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement

No social post, newsletter or message is sent by these scripts. App Store review/release remains separate from publishing this website.
