// Lossless source captures are copied from StockScan marketing/1.4.0.
// This script only creates delivery sizes; it never changes the app UI.
const sharp = require('sharp');
const fs = require('node:fs/promises');
const path = require('node:path');
async function main() {
  const dir = path.join(__dirname, '../assets/screens');
  for (const name of await fs.readdir(dir)) {
    if (!name.endsWith('.png')) continue;
    const width = name.startsWith('ipad') ? 1000 : 660;
    await sharp(path.join(dir,name)).resize({width}).webp({quality:88}).toFile(path.join(dir,name.replace('.png','.webp')));
  }
  await sharp(path.join(__dirname,'../assets/workshop.png')).webp({quality:86}).toFile(path.join(__dirname,'../assets/workshop.webp'));
  for (const lang of ['de','en']) {
    await sharp(path.join(__dirname,`../assets/marketing/release-banner-${lang}.png`)).resize(1200,630,{fit:'contain',background:'#0c3029'}).jpeg({quality:90}).toFile(path.join(__dirname,`../assets/marketing/social-${lang}.jpg`));
  }
}
main().catch(error => { console.error(error); process.exit(1); });
