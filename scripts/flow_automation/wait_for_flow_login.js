const puppeteer = require('puppeteer-core');

(async () => {
    try {
        const browser = await puppeteer.connect({
            browserURL: 'http://127.0.0.1:9222',
            defaultViewport: null
        });
        
        const pages = await browser.pages();
        const page = pages.find(p => p.url().includes('flow.google') || p.url().includes('labs.google')) || pages[0];
        
        const url = page.url();
        const title = await page.title();
        console.log("Current URL:", url);
        console.log("Current Title:", title);

        if (url.includes('flow.google.com') && !url.includes('signin') && !url.includes('accounts.google')) {
            console.log("LOGIN_STATE: LOGGED_IN");
        } else if (url.includes('labs.google/fx/tools/flow')) {
            console.log("LOGIN_STATE: LOGGED_IN");
        } else {
            console.log("LOGIN_STATE: PENDING_USER_LOGIN");
        }

        browser.disconnect();
    } catch (e) {
        console.error("Error:", e);
    }
})();
