const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

(async () => {
    try {
        console.log("Launching browser with port 9222...");
        const profilePath = path.resolve(__dirname, 'flow_profile');
        const chromeExe = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
        
        const launchOptions = {
            headless: false,
            defaultViewport: null,
            userDataDir: profilePath,
            args: ['--start-maximized', '--remote-debugging-port=9222']
        };

        if (fs.existsSync(chromeExe)) {
            launchOptions.executablePath = chromeExe;
        }

        const browser = await puppeteer.launch(launchOptions);

        const wsEndpoint = browser.wsEndpoint();
        console.log("Browser launched. WS Endpoint:", wsEndpoint);
        
        // Extract the path part
        const wsPath = wsEndpoint.split('127.0.0.1:9222')[1];
        
        // Write the DevToolsActivePort file
        const devToolsPortPath = process.env.LOCALAPPDATA + '\\Google\\Chrome\\User Data\\DevToolsActivePort';
        try {
            fs.writeFileSync(devToolsPortPath, `9222\n${wsPath}`);
            console.log("Wrote DevToolsActivePort to", devToolsPortPath);
        } catch (err) {
            console.warn("Could not write global DevToolsActivePort:", err.message);
        }
        
        const pages = await browser.pages();
        const page = pages.length > 0 ? pages[0] : await browser.newPage();
        
        console.log("Navigating to Google Flow (https://labs.google/fx/tools/flow)...");
        await page.goto('https://labs.google/fx/tools/flow', { waitUntil: 'networkidle2' });
        
        console.log("READY_FOR_USER_LOGIN");
        
        // Keep process alive
        await new Promise(resolve => {});
    } catch (e) {
        console.error("Error:", e);
    }
})();

