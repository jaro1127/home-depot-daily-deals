import json
import os
from pathlib import Path

from scraper import get_categories
from discord_notify import send_notification


STATE_FILE = Path("state.json")


def load_keywords():
    with open("config.json", "r") as f:
        config = json.load(f)
    return config["watch_keywords"]


def load_previous_categories():
    if not STATE_FILE.exists():
        return []

    with open(STATE_FILE, "r") as f:
        return json.load(f)


def save_categories(categories):
    with open(STATE_FILE, "w") as f:
        json.dump(categories, f, indent=2)


def find_matches(categories, keywords):
    matches = []

    for category in categories:
        for keyword in keywords:
            if keyword.lower() in category.lower():
                matches.append(category)
                break

    return matches


def main():
    categories = get_categories()

    previous = load_previous_categories()

    if categories == previous:
        print("No changes today.")
        return

    matches = find_matches(categories, load_keywords())

    send_notification(categories, matches)

    save_categories(categories)

    print("Notification sent.")


if __name__ == "__main__":
    main()
