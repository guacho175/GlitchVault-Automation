const puppeteer = require('puppeteer-core');

(async () => {
    try {
        const browser = await puppeteer.connect({
            browserURL: 'http://127.0.0.1:9222',
            defaultViewport: null
        });
        
        const pages = await browser.pages();
        const page = pages.find(p => p.url().includes('labs.google') || p.url().includes('google.com')) || pages[0];
        
        await page.bringToFront();
        
        console.log("Current URL:", page.url());
        console.log("Current Title:", await page.title());
        
        // Check if we are on a sign-in page or workspace
        const url = page.url();
        if (url.includes('accounts.google.com') || url.includes('signin') || (await page.title()).toLowerCase().includes('iniciar sesión')) {
            console.log("STATUS: REQUIRES_LOGIN");
        } else if (url.includes('labs.google/fx/tools/flow')) {
            console.log("STATUS: FLOW_READY");
        } else {
            console.log("STATUS: READY");
        }
        
        browser.disconnect();
    } catch (e) {
        console.error("Error connecting to browser:", e);
    }
})();
