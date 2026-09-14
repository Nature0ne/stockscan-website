const {chromium} = require('playwright');
const assert = require('node:assert/strict');
const {execFileSync} = require('node:child_process');
const baseline = process.argv.includes('--baseline') ? execFileSync('git', ['show', 'origin/main:assets/site.css'], {encoding:'utf8'}) : null;
const fs = require('node:fs/promises');
const origin = process.env.SITE_URL || 'http://127.0.0.1:8765/';
(async () => {
  const browser = await chromium.launch({headless: true, channel: 'chrome'});
  try {
    await fs.mkdir('artifacts', {recursive: true});
    for (const width of [320, 390, 480, 481, 600, 601, 768, 1440]) {
      const page = await browser.newPage({viewport: {width, height: 960}});
      if (baseline) await page.route('**/assets/site.css', route => route.fulfill({contentType:'text/css', body:baseline}));
      for (const language of ['', 'en/']) {
        await page.goto(origin + language);
        await page.evaluate(() => document.fonts.ready);
        const failures = await page.locator('.workflow-card').evaluateAll(cards => {
          const failures = [];
          for (const card of cards) {
            const bounds = card.getBoundingClientRect();
            const phone = card.querySelector('.phone').getBoundingClientRect();
            if (phone.left < bounds.left || phone.right > bounds.right) failures.push({phoneClippedHorizontally:true});
            for (const text of card.querySelectorAll('h3, p')) {
              const range = document.createRange();
              range.selectNodeContents(text);
              for (const rect of range.getClientRects()) {
                if (!rect.width || !rect.height) continue;
                const clipped = rect.left < bounds.left || rect.right > bounds.right || rect.bottom > bounds.bottom;
                const overlapped = rect.left < phone.right && rect.right > phone.left && rect.top < phone.bottom && rect.bottom > phone.top;
                if (clipped || overlapped) failures.push({text: text.textContent, clipped, overlapped});
              }
            }
          }
          return failures;
        });
        assert.deepEqual(failures, [], `${language || 'de'} at ${width}px`);
        if (width === 320) await page.locator('.workflow-grid').screenshot({path: `artifacts/workflow-${language ? 'en' : 'de'}-320.png`, style: '.site-header, .skip { visibility: hidden !important; }'});
      }
      await page.close();
    }
    console.log('Passed: workflow text remains inside cards and clear of phones in both languages at 8 widths (320–1440px).');
  } finally { await browser.close(); }
})().catch(error => { console.error(error); process.exit(1); });
