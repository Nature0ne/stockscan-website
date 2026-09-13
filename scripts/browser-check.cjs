const {chromium} = require('playwright');
const fs = require('node:fs/promises');
const path = require('node:path');
const assert = require('node:assert/strict');
const origin=process.env.SITE_URL||'http://127.0.0.1:8765/';
async function main(){
 const artifacts=path.join(__dirname,'../artifacts');await fs.mkdir(artifacts,{recursive:true});
 const browser=await chromium.launch({headless:true,channel:'chrome'});
 const errors=[];const results=[];
 try{
 for(const width of [1440,768,390,320]){
  const context=await browser.newContext({viewport:{width,height:960},reducedMotion:'reduce'});
  const p=await context.newPage();
  p.on('pageerror',error=>errors.push(error.message));
  p.on('response',response=>{if(response.status()>=400)errors.push(response.url()+': '+response.status())});
  for(const lang of ['','en/']){
   await p.goto(origin+lang,{waitUntil:'networkidle'});
   await p.evaluate(async()=>{for(const image of document.images){image.loading='eager'}await Promise.all([...document.images].map(i=>i.decode().catch(()=>{})))});
   assert.equal(await p.locator('h1').count(),1);
   assert.equal(await p.evaluate(()=>document.documentElement.scrollWidth>window.innerWidth),false,`Overflow ${lang} at ${width}`);
   assert.deepEqual(await p.evaluate(()=>[...document.images].filter(i=>!i.complete||!i.naturalWidth).map(i=>i.src)),[]);
   assert.equal(await p.locator('details[open]').count(),0);
   await p.locator('summary').first().click();assert.equal(await p.locator('details[open]').count(),1);
   await p.locator('summary').first().click();
   if(width>=768){
    await p.locator('[data-next]').click();
    await p.waitForFunction(()=>document.querySelector('[data-gallery]').scrollLeft>0);
    await p.locator('[data-previous]').click();
    await p.waitForFunction(()=>document.querySelector('[data-gallery]').scrollLeft<=3);
   }
   await p.evaluate(()=>scrollTo(0,0));
   await p.screenshot({path:path.join(artifacts,`home-${lang?'en':'de'}-${width}.png`),fullPage:true});
   if(width===1440||width===390){await p.evaluate(()=>scrollTo(0,0));await p.screenshot({path:path.join(artifacts,`hero-${lang?'en':'de'}-${width}.png`)});}
   await p.getByRole('link',{name:lang?'Deutsch':'English',exact:true}).click();
   assert.equal(await p.locator('html').getAttribute('lang'),lang?'de':'en');
   results.push({page:lang||'de',width,images:'passed',overflow:'none',faq:'passed',language:'passed'});
  }
  await context.close();
 }
 const p=await browser.newPage();
 for(const lang of ['','en/']){
  for(const name of ['support.html','privacy.html','impressum.html','media.html']){
   await p.setViewportSize({width:320,height:844});
   await p.goto(origin+lang+name);assert.equal(await p.locator('h1').count(),1);
   assert.equal(await p.evaluate(()=>document.documentElement.scrollWidth>window.innerWidth),false,`Overflow ${lang+name} at 320`);
   for(const href of await p.locator('a[download]').evaluateAll(xs=>xs.map(x=>x.href))){const r=await p.request.get(href);assert.equal(r.status(),200);assert.ok((await r.body()).length>100);}
   results.push({page:lang+name,status:'passed'});
  }
 }
 const nojs=await browser.newContext({javaScriptEnabled:false,viewport:{width:390,height:844}});
 const np=await nojs.newPage();await np.goto(origin);assert.ok(await np.locator('h1').isVisible());await np.locator('summary').first().click();assert.equal(await np.locator('details[open]').count(),1);await np.getByRole('link',{name:'English',exact:true}).click();assert.equal(await np.locator('html').getAttribute('lang'),'en');await nojs.close();
 assert.deepEqual(errors,[]);
 await fs.writeFile(path.join(artifacts,'browser-report.json'),JSON.stringify({origin,checks:results,noJavaScript:'passed',errors},null,2));
 console.log(JSON.stringify({checked:results.length,viewports:[1440,768,390,320],languages:['de','en'],noJavaScript:'passed',errors},null,2));
 }finally{await browser.close()}
}
main().catch(e=>{console.error(e);process.exit(1)});
