const {chromium} = require('playwright');
const fs = require('fs');
(async () => {
  const b = await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome'});
  const p = await b.newPage({viewport:{width:1080,height:1350}, deviceScaleFactor:2});
  fs.mkdirSync('out', {recursive:true});
  for (const n of ['slide1','slide2','slide3','slide4','slide5','slide6']) {
    await p.goto('file://' + process.cwd() + '/html/' + n + '.html');
    await p.evaluate(() => document.fonts.ready);
    await p.evaluate(() => Promise.all([...document.images].map(i => i.decode().catch(()=>{}))));
    await p.locator('.stage').screenshot({path:`out/${n}_2x.png`});
    console.log('rendered', n);
  }
  await b.close();
})();
