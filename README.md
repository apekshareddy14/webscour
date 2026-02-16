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

Distributed Web Crawler – Milestone 2

Project Overview

This project implements a Distributed Web Crawler using RabbitMQ.

In Milestone 2, the basic sequential crawler was upgraded into a distributed system using a producer-consumer architecture, allowing multiple workers to process URLs in parallel.

The system demonstrates scalability, reliability, and message-based communication.

Architecture
Producer  →  RabbitMQ Queue  →  Worker(s)

🔹 Producer

Pushes initial seed URLs into the queue.

Starts the crawling process.

🔹 RabbitMQ

Stores URLs safely inside a queue (url_queue).

Distributes messages fairly among workers.

Handles message acknowledgment for reliability.

🔹 Worker

Consumes URLs from the queue.

Fetches webpage content.

Saves HTML locally.

Extracts hyperlinks.

Publishes newly discovered URLs back into the queue.

Avoids duplicate processing.

Features Implemented

Distributed crawling using message queues

Producer-consumer architecture

Duplicate URL detection

Maximum crawl limit control

Message acknowledgment (fault tolerance)

HTML page storage

Parallel worker support (scalable design)

Technologies Used

.Python

.RabbitMQ

.pika (Python RabbitMQ client)

.requests

.BeautifulSoup

How to Run the Project?

1️⃣ Start RabbitMQ Server

Make sure RabbitMQ is installed and running locally.

Open:

http://localhost:15672


Default login:

Username: guest
Password: guest

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run Producer
python producer.py


This pushes initial seed URLs into the queue.

4️⃣ Run Worker(s)
python worker.py


You can run multiple workers in different terminals to enable parallel crawling.

Output:

Crawled HTML pages are stored in the pages/ directory.

.RabbitMQ dashboard shows:

.Ready messages

.Unacked messages

.Active consumers

Learning Outcomes:

Understanding distributed systems

Implementing message queue architecture

Handling fault tolerance using acknowledgments

Designing scalable backend systems

Managing asynchronous task processing

Conclusion:

Milestone 2 successfully transforms a basic crawler into a distributed web crawling system using RabbitMQ.
The implementation supports parallel processing, reliability, and controlled crawling, making it scalable and production-oriented.