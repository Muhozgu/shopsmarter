from bs4 import BeautifulSoup
import time
import requests

urls = [
    "https://www.lidl.pl/c/zywnosc-i-napoje/s10068374",
    
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

for url in urls:
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print(f"Successfully fetched: {url} (Status: {response.status_code})")

        # ✅ Parse INSIDE the loop, using the response you already have
        soup = BeautifulSoup(response.text, "html.parser")
        products = soup.find_all("div", class_="optanon-category-C0004")

        for p in products:
            print(p.text.strip())

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")

    time.sleep(3)