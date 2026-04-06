from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        viewport={"width": 1280, "height": 720},
        locale="pl-PL",
        timezone_id="Europe/Warsaw"
    )
    
    page = context.new_page()
    page.goto("https://www.lidl.pl/c/zywnosc-i-napoje/s10068374?sort=storeStartDate&category.id=10071012", wait_until="domcontentloaded")
    
    page.wait_for_timeout(6000)  # just wait 6 seconds flat
    
    html = page.content()
    browser.close()

with open("page.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Done! Open page.html and search for a price")