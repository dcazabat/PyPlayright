import asyncio
from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright

urls = ["https://mercadolibre.com.ar/", "http://playwright.dev", "http://whatsmyuseragent.org/"]

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(urls[0])
        print(await page.title() + ' - Async')
        await browser.close()

asyncio.run(main())

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(urls[1])
    print(page.title() + ' - Sync')
    browser.close()


with sync_playwright() as p:
    browser = p.webkit.launch()
    page = browser.new_page()
    page.goto(urls[0])
    page.screenshot(path="captura.png")
    browser.close()