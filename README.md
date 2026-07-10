# Book Scraper (Python)

A Python web scraper that extracts book titles, prices, ratings, and stock availability from [books.toscrape.com](https://books.toscrape.com) and exports the data to a CSV file. Built with `requests` and `BeautifulSoup`.

## Features

- Scrapes multiple pages of book listings automatically
- Extracts title, price (£), star rating, and stock availability for each book
- Handles failed requests gracefully instead of crashing
- Adds a short delay between page requests to avoid hammering the server
- Saves all results to a clean, structured CSV file

## Tech Stack

- Python 3
- `requests` — for fetching webpage HTML
- `BeautifulSoup` (`bs4`) — for parsing and extracting data from HTML
- `csv` (standard library) — for exporting data

## How It Works

1. `fetch_page()` requests the raw HTML of a catalogue page
2. `parse_books()` searches that HTML for each book entry and pulls out its title, price, rating, and availability
3. `scrape_all_pages()` repeats this across multiple pages and combines the results
4. `save_to_csv()` writes the final list of books to `books.csv`

## Setup & Usage

```bash
pip install -r requirements.txt
python scraper.py
```

This will scrape 5 pages of book listings and save the results to `books.csv` in the same folder.

## Sample Output

| title | price_gbp | rating | availability |
|---|---|---|---|
| A Light in the Attic | 51.77 | 3 | In stock |
| Tipping the Velvet | 53.74 | 1 | In stock |

## Notes

This project was built as a practice exercise for web scraping fundamentals, using a site specifically designed to be scraper-friendly for learning purposes. Real-world e-commerce sites (Amazon, Flipkart, etc.) often use bot detection, JavaScript-rendered content, and CAPTCHAs that require more advanced tools like Selenium or official APIs.

## License

This project is licensed under the MIT License.
