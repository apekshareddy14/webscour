# WebScour - Distributed Web Crawler

## Description
WebScour is a simple Python-based web crawler that starts from a seed URL and crawls multiple pages while saving HTML content locally.

## Features
- Uses queue for URL management
- Uses visited set to prevent duplicates
- Saves HTML pages
- Extracts hyperlinks
- Limits crawling to 10 pages
- Includes politeness delay

## Technologies Used
- Python
- Requests
- BeautifulSoup

## How to Run

1. Create virtual environment:
   python -m venv venv

2. Activate:
   venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Run crawler:
   python crawler.py
