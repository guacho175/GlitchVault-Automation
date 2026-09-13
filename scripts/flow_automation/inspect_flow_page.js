const puppeteer = require('puppeteer-core');

(async () => {
    try {
        const browser = await puppeteer.connect({
            browserURL: 'http://127.0.0.1:9222',
            defaultViewport: null
        });
        
        const pages = await browser.pages();
        const page = pages.find(p => p.url().includes('google.com') || p.url().includes('flow.google')) || pages[0];
        
        console.log("Current Page URL:", page.url());
        console.log("Title:", await page.title());

        const buttons = await page.evaluate(() => {
            return Array.from(document.querySelectorAll('a, button'))
                .map(el => ({
                    text: el.innerText.trim(),
                    href: el.href || null,
                    tag: el.tagName
                }))
                .filter(el => el.text.length > 0 && el.text.length < 50);
        });

        console.log("Action buttons / links:");
        buttons.forEach(b => console.log(`[${b.tag}] "${b.text}" -> ${b.href}`));

        browser.disconnect();
    } catch (e) {
        console.error("Error:", e);
    }
})();
