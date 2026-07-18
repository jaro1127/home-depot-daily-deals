import requests
from bs4 import BeautifulSoup


def get_categories():
    headers = {
        "User-Agent": (
            "Mozilla/5.0 "
            "(Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 "
            "(KHTML, like Gecko) "
            "Chrome/137.0 Safari/537.36"
        )
    }

    response = requests.get(
        "https://www.homedepot.com/daily-deals",
        headers=headers,
        timeout=30,
    )

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    promo = soup.select_one('[data-testid="special-buy-promos"]')

    if promo is None:
        raise Exception("Couldn't find the Daily Deals ribbon.")

    categories = []
    seen = set()

    for button in promo.select("button"):
        text = button.get_text(" ", strip=True)

        # Ignore junk
        if not text:
            continue

        if text == "Add to Cart":
            continue

        # Remove duplicates
        if text in seen:
            continue

        seen.add(text)
        categories.append(text)

    return categories
