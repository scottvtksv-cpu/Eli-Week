// Rendert index.html op 390 px (gsm) en 820 px (tablet) en maakt per week een screenshot.
// Gebruik:  NODE_PATH=$(npm root -g) node tools/render.js [uitvoermap]
// Faalt (exit 1) als de pagina horizontaal overloopt. De screenshots moet je daarna zelf bekijken:
// niets mag afbreken, overlappen of afgesneden zijn.
const { chromium } = require('playwright');
const path = require('path');
const uit = process.argv[2] || '.';
// Vooraf geïnstalleerde Chromium meegeven; nooit `playwright install` draaien.
const CHROME = process.env.CHROME || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';

(async () => {
  const browser = await chromium.launch({ executablePath: CHROME });
  let fout = false;
  for (const breedte of [390, 820]) {
    const p = await browser.newPage({ viewport: { width: breedte, height: 800 }, deviceScaleFactor: 1 });
    await p.goto('file://' + path.resolve('index.html'));
    await p.waitForTimeout(1500);                                  // lettertypes laten laden
    const over = await p.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
    console.log(`${breedte}px: horizontale overloop ${over}px`);
    if (over > 0) fout = true;
    const weken = await p.$$('section.week');
    for (let i = 0; i < weken.length; i++) {
      const f = path.join(uit, `week${i + 1}-${breedte}.png`);
      await weken[i].screenshot({ path: f });
      console.log('  ', f);
    }
    await p.close();
  }
  await browser.close();
  process.exit(fout ? 1 : 0);
})();
