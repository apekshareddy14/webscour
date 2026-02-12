import requests
from bs4 import BeautifulSoup
import os
import time
from urllib.parse import urljoin, urlparse

# 1. Seed URL
seed_url = "https://iana.org/"

# 2. Queue and Visited
queue = []
visited = set()

# 3. Add seed to queue
queue.append(seed_url)

# 4. Create folder to save pages
if not os.path.exists("pages"):
    os.makedirs("pages")

# 5. Maximum pages limit
MAX_PAGES = 10

# 6. Get seed domain
seed_domain = urlparse(seed_url).netloc

# 7. Crawler loop
while queue and len(visited) < MAX_PAGES:

    current_url = queue.pop(0)

    if current_url in visited:
        continue

    print("Crawling:", current_url)

    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(current_url, headers=headers, timeout=10)

        if response.status_code != 200:
            continue

        html_content = response.text

        # Save HTML
        filename = f"pages/page_{len(visited)}.html"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_content)

        soup = BeautifulSoup(html_content, "html.parser")

        for link in soup.find_all("a", href=True):
            absolute_link = urljoin(current_url, link["href"])

            parsed_link = urlparse(absolute_link)

            # Only http/https and same domain
            if parsed_link.scheme in ["http", "https"] and parsed_link.netloc == seed_domain:

                if absolute_link not in visited and absolute_link not in queue:
                    queue.append(absolute_link)

        visited.add(current_url)

        time.sleep(1)

    except Exception as e:
        print("Error:", e)

# 8. Print summary
print("\nCrawling Completed")
print("Total pages crawled:", len(visited))
print("Total unique URLs visited:", len(visited))
