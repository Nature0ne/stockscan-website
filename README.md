# StockScan website

Static German and English marketing site for StockScan 1.4, hosted on GitHub Pages at https://nature0ne.github.io/stockscan-website/.

## Edit and build

The deployed HTML is committed. GitHub Pages serves `main` at the repository root. No frontend framework, runtime dependency, analytics, third-party font or cookie consent banner is needed. Keep relative asset paths: this site is hosted under `/stockscan-website/`, not the domain root.

- `scripts/build.py`: bilingual landing page, media page, shared templates and marketing copy.
- `scripts/documents.py`: bilingual support, privacy and legal pages.
- `assets/site.css`: responsive design and reduced-motion styling.
- `assets/site.js`: progressive gallery controls; all content, navigation and FAQs work without JavaScript.
- `en/`: English pages with their own metadata, canonical and hreflang links.
- `marketing/README.md`: asset provenance, formats and release context.

```sh
python3 scripts/build.py
python3 scripts/documents.py
python3 scripts/check.py
python3 -m http.server 8765 --bind 127.0.0.1
```

Open http://127.0.0.1:8765/. For browser verification, install Playwright in your tooling environment and use an installed Google Chrome:

```sh
node scripts/browser-check.cjs
```

The script checks German and English at 320, 390, 768 and 1440 CSS pixels, images, overflow, language switching, native FAQs, gallery navigation, media downloads and no-JavaScript behavior. Screenshots and results are written to ignored `artifacts/`. Set `SITE_URL` to validate another serving base URL.

## Marketing

The public `media.html` and `en/media.html` offer the complete ZIP, landscape release banners, link-preview images, square posts, stories and ready-to-use copy. The ZIP includes all 24 official iPhone/iPad screenshot compositions. Nothing here automatically posts to social channels.

```sh
python3 scripts/marketing.py
# While the local HTTP server is running; Playwright + Google Chrome required:
node scripts/render-marketing.cjs
python3 scripts/package.py
```

Rendering uses macOS Avenir Next and Georgia. The original app screenshots are never replaced with generated UI. The workshop photograph is an illustrative AI-generated image; its prompt and provenance are in `marketing/README.md`.

`node scripts/optimize-assets.cjs` needs `sharp` and original source PNGs from the app repository to regenerate WebP delivery images. Source PNGs remain ignored; optimized files and completed marketing deliverables are committed.

## Release facts

Content is aligned to the StockScan 1.4 code, localized release metadata and `FeatureAccessPolicy.swift`. Free: one active inventory and 100 different items, unlimited CSV, completion/history and Watch single-item counting. Pro: unlimited lists/items, Fast Scan, XLSX, templates, target/actual and history comparisons, difference reports, Watch lists and optional private iCloud sync. Family Sharing shares the entitlement, not inventories. Imported master data stays local. Device minimums: iOS/iPadOS 18, watchOS 10.

The owner explicitly requested launch messaging without a preview label on 13 September 2026. Website publication does not submit or release the app in App Store Connect. No app source files are changed by this website project.
