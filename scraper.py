import csv
import time
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
OUTPUT_FILE = "books.csv"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

RATING_WORDS = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


def fetch_page(page_number):
    url = BASE_URL.format(page_number)
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"  ! Failed to fetch page {page_number}: {e}")
        return None


def parse_books(html):
    soup = BeautifulSoup(html, "html.parser")
    books = []

    for article in soup.select("article.product_pod"):
        title = article.h3.a["title"].strip()

        price_text = article.select_one(".price_color").text.strip()
        price = price_text.replace("£", "").strip()

        rating_class = article.select_one("p.star-rating")["class"]
        rating_word = [c for c in rating_class if c != "star-rating"][0]
        rating = RATING_WORDS.get(rating_word, 0)

        availability = article.select_one(".availability").text.strip()

        books.append({
            "title": title,
            "price_gbp": price,
            "rating": rating,
            "availability": availability,
        })

    return books


def scrape_all_pages(max_pages=5, delay=1):
    all_books = []

    for page in range(1, max_pages + 1):
        print(f"Scraping page {page}...")
        html = fetch_page(page)
        if html is None:
            break

        books = parse_books(html)
        if not books:
            print("  No more books found, stopping.")
            break

        all_books.extend(books)
        time.sleep(delay)  # be polite, don't hammer the server

    return all_books


def save_to_csv(books, filename):
    if not books:
        print("No data to save.")
        return

    fieldnames = ["title", "price_gbp", "rating", "availability"]
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)

    print(f"Saved {len(books)} books to {filename}")


if __name__ == "__main__":
    books = scrape_all_pages(max_pages=5)
    save_to_csv(books, OUTPUT_FILE)