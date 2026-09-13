const puppeteer = require('puppeteer-core');

(async () => {
    try {
        const browser = await puppeteer.connect({
            browserURL: 'http://127.0.0.1:9222',
            defaultViewport: null
        });
        
        const pages = await browser.pages();
        const page = pages.find(p => p.url().includes('flow.google') || p.url().includes('google.com')) || pages[0];
        
        console.log("Current URL:", page.url());
        
        // Find button with text 'Probar Google Flow'
        const clicked = await page.evaluate(() => {
            const btns = Array.from(document.querySelectorAll('button, a'));
            const target = btns.find(b => b.innerText && b.innerText.includes('Probar Google Flow'));
            if (target) {
                target.click();
                return true;
            }
            return false;
        });

        console.log("Clicked 'Probar Google Flow':", clicked);
        await new Promise(r => setTimeout(r, 4000));
        console.log("New URL:", page.url());
        console.log("New Title:", await page.title());

        browser.disconnect();
    } catch (e) {
        console.error("Error:", e);
    }
})();
