const {chromium}=require('playwright');
const path=require('node:path');
(async()=>{
 const b=await chromium.launch({headless:true,channel:'chrome'});
 try{for(const lang of ['de','en'])for(const [size,height]of [['square',1080],['story',1920]]){
  const p=await b.newPage({viewport:{width:1080,height},deviceScaleFactor:1});
  await p.goto(`http://127.0.0.1:8765/marketing/source/${size}-${lang}.html`);
  await p.evaluate(async()=>{await document.fonts.ready;await Promise.all([...document.images].map(i=>i.decode()))});
  await p.screenshot({path:path.join(__dirname,`../assets/marketing/${size}-${lang}-1080x${height}.png`)});
  await p.close();
 }}finally{await b.close()}
 console.log('Rendered 4 marketing PNGs: square and story, German and English.');
})().catch(e=>{console.error(e);process.exit(1)});
