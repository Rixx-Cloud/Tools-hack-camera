import requests
from bs4 import BeautifulSoup

def scrape_public_data(url):
    """Ambil data publik dari website dengan etika."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.get_text()
    except Exception as e:
        print(f"Error: {e}")
        return None

# Contoh penggunaan:
# data = scrape_public_data("https://example.com")
# print(data)