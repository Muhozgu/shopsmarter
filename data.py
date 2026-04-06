import time
import requests


urls = [
    "https://www.lidl.pl/",
    "https://www.lidl.pl/c/nasze-gazetki/s10008614"
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}


for url in urls:
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print(f"Successfully fetched: {url} (Status: {response.status_code})")
        # Process data here
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
    
    time.sleep(3)