# WebScour Search Engine

## Overview

WebScour is a simple search engine prototype built using Python.
The system crawls web pages, builds an inverted index, ranks documents using TF-IDF, and provides a searchable interface through a web API and frontend.

This project demonstrates the core components of a search engine including crawling, indexing, ranking, and querying.

---

## Features

* Web crawling to collect webpage data
* Inverted index creation for efficient searching
* TF-IDF based ranking algorithm
* REST API built with FastAPI
* Simple web interface for searching documents
* Displays top relevant documents with ranking scores

---

## Project Architecture

User → Web Interface (HTML + JavaScript) → FastAPI Backend → Search Engine → Results

1. User enters a query in the web interface
2. The frontend sends the query to the FastAPI API
3. The backend searches the inverted index
4. TF-IDF scores are calculated
5. The most relevant documents are returned and displayed

---

## Project Structure

webscour/

crawler.py – Web crawler to collect webpage data
indexer.py – Builds the inverted index
search_engine.py – Implements search and ranking logic
api.py – FastAPI backend for search requests
index.html – Frontend search interface
inverted_index.json – Stored inverted index data
idf.json – IDF scores for ranking
README.md – Project documentation
LICENSE – Project license

---

## Technologies Used

Python
FastAPI
HTML
JavaScript
TF-IDF Ranking Algorithm

---

## How to Run the Project

### 1. Clone the repository

git clone <your-repository-link>

cd webscour

### 2. Install dependencies

pip install fastapi uvicorn

### 3. Start the backend server

uvicorn api:app --reload

### 4. Open the search interface

Open the file:

index.html

in your browser.

### 5. Search Example

Enter a query such as:

python crawler

The system will return the most relevant documents ranked by TF-IDF score.

---

## Example Output

https___github.com_topics_python.html Score: 66.61
https___github.com_topics_http-server.html Score: 25.16
http___python-requests.org.html Score: 23.68

---

## Future Improvements

Add a database for storing indexed pages
Improve crawling coverage
Enhance ranking algorithms
Create a modern frontend interface
Add pagination and filtering

---

## License

This project is licensed under the MIT License.
