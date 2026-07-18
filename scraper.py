import requests
from bs4 import BeautifulSoup


URL = "https://www.homedepot.com/daily-deals"


def get_categories():
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/137.0 Safari/537.36"
        )
    }

    response = requests.get(URL, headers=headers, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    promo = soup.select_one('[data-testid="special-buy-promos"]')

    if promo is None:
        raise RuntimeError("Couldn't find Daily Deals ribbon.")

    categories = []
    seen = set()

    # Only use buttons that contain an image with an alt attribute.
    # The product "Add to Cart" buttons don't.
    for button in promo.select("button"):
        img = button.find("img")

        if img is None:
            continue

        text = img.get("alt", "").strip()

        if not text:
            continue

        if text in seen:
            continue

        seen.add(text)
        categories.append(text)

    return categories
