import pika
import requests
import os
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin

MAX_PAGES = 50
visited = set()

if not os.path.exists("pages"):
    os.makedirs("pages")

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel = connection.channel()

channel.queue_declare(queue='url_queue')
channel.basic_qos(prefetch_count=1)

def callback(ch, method, properties, body):
    global visited

    if len(visited) >= MAX_PAGES:
        print("Reached max pages. Stopping worker.")
        ch.stop_consuming()
        return

    url = body.decode()

    if url in visited:
        print(f"Skipped (visited): {url}")
        ch.basic_ack(delivery_tag=method.delivery_tag)
        return

    print(f"Processing: {url}")
    visited.add(url)

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            filename = re.sub(r'[\\/*?:"<>|]', "_", url)
            filename = filename.replace("https://", "").replace("http://", "")

            with open(f"pages/{filename}.html", "w", encoding="utf-8") as f:
                f.write(response.text)

            soup = BeautifulSoup(response.text, "html.parser")

            for link in soup.find_all("a", href=True):
                new_url = urljoin(url, link["href"])

                if not new_url.startswith("http"):
                    continue

                channel.basic_publish(
                    exchange='',
                    routing_key='url_queue',
                    body=new_url
                )

        print(f"Done: {url}")

    except Exception as e:
        print(f"Error processing {url}: {e}")

    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue='url_queue', on_message_callback=callback)

print("Worker started. Waiting for messages...")
channel.start_consuming()
