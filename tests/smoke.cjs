const { chromium } = require('/Users/mattsidnell/Sites/_ops-promotion-resume-20261005/node_modules/playwright');
const fs = require('node:fs');
const path = require('node:path');
(async()=>{
 const browser=await chromium.launch({headless:true,executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
 const shots=path.join(process.env.HOME,'Sites/digipixel-starter-previews/tests/screenshots');
 fs.mkdirSync(shots,{recursive:true});
 let failed=0;
 for(const [slug,port] of [['alder',8771],['fieldnote',8772],['sunday',8773]]){
  for(const width of [1440,390]){
   const page=await browser.newPage({viewport:{width,height:920},deviceScaleFactor:1});
   const errors=[];page.on('pageerror',e=>errors.push(e.message));
   const base='http://127.0.0.1:'+port;
   await page.goto(base+'/',{waitUntil:'networkidle'});
   await page.evaluate(async()=>{ for(let y=0;y<document.body.scrollHeight;y+=650){window.scrollTo(0,y);await new Promise(resolve=>setTimeout(resolve,35));} window.scrollTo(0,0);});
   await page.waitForTimeout(300);
   const headline=await page.locator('h1').innerText();
   await page.locator('img').evaluateAll(imgs=>imgs.forEach(im=>im.loading='eager'));
   await page.waitForFunction(()=>Array.from(document.images).every(i=>i.complete&&i.naturalWidth>0),null,{timeout:15000});
   const images=await page.locator('img').evaluateAll(imgs=>imgs.map(im=>({src:im.getAttribute('src'),loaded:im.complete&&im.naturalWidth>0})));
   const overflow=await page.evaluate(()=>({doc:document.documentElement.scrollWidth,viewport:innerWidth}));
   if(images.some(i=>!i.loaded)||errors.length||overflow.doc>width+1){failed++; console.log('ISSUE',slug,width,JSON.stringify({images,errors,overflow}));}
   const shot=path.join(shots,slug+'-'+width+'.png');
   await page.screenshot({path:shot,fullPage:true});
   for(const p of ['services','about','contact']){
    const resp=await page.goto(base+'/'+p+'/',{waitUntil:'domcontentloaded'});
    if(resp.status()!==200||await page.locator('h1').count()!==1){failed++;console.log('BAD_PAGE',slug,p,resp.status());}
   }
   if(width===390){
    await page.locator('.menu-toggle').click();
    if(await page.locator('.menu-toggle').getAttribute('aria-expanded')!=='true'){failed++;console.log('BAD_MENU',slug);}
    await page.locator('a.nav-link[href="/services/"]').click();
    if(!page.url().endsWith('/services/')){failed++;console.log('BAD_LINK',slug);}
   }
   await page.goto(base+'/contact/');
   await page.locator('input[name="name"]').fill('Preview Tester');
   await page.locator('input[name="email"]').fill('preview@example.com');
   await page.locator('select[name="service"]').selectOption({index:1});
   await page.locator('textarea[name="message"]').fill('Sample text');
   await page.locator('button[type="submit"]').click();
   const status=await page.locator('.form-status').innerText();
   if(!status.includes('nothing was sent')){failed++;console.log('BAD_FORM',slug,width,status);}
   console.log('OK',slug,width,'headline:',headline,'images:',images.length,'overflow:',overflow.doc-width,'form:',status.length,'screenshot:',shot);
   await page.close();
  }
 }
 await browser.close();
 console.log('FAILED=',failed);
 if(failed)process.exit(1);
})().catch(e=>{console.error(e);process.exit(1)});
