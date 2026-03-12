import os
import json
import math
import re
from bs4 import BeautifulSoup
from collections import defaultdict

PAGES_FOLDER = "pages"

# Task 1: Load HTML Documents
def load_documents(folder):
    documents = {}
    for filename in os.listdir(folder):
        if filename.endswith(".html"):
            path = os.path.join(folder, filename)
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                documents[filename] = f.read()
    return documents

# Task 2: Extract Visible Text
def extract_text(html):
    soup = BeautifulSoup(html, "html.parser")

    # Remove script and style elements
    for tag in soup(["script", "style"]):
        tag.decompose()

    text = soup.get_text(separator=" ")
    return text

# Task 3: Tokenization & Cleaning
def tokenize(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)  # remove punctuation
    tokens = text.split()
    return tokens

# Task 4: Compute Term Frequency
def compute_tf(tokens):
    tf = defaultdict(int)
    for token in tokens:
        tf[token] += 1
    return tf

# Task 5: Build Inverted Index
def build_inverted_index(documents):
    inverted_index = defaultdict(list)
    document_count = len(documents)

    for doc_id, html in documents.items():
        text = extract_text(html)
        tokens = tokenize(text)
        tf = compute_tf(tokens)

        for word, freq in tf.items():
            inverted_index[word].append((doc_id, freq))

    return inverted_index, document_count

# Task 7: Compute IDF
def compute_idf(inverted_index, total_docs):
    idf = {}
    for word, doc_list in inverted_index.items():
        doc_freq = len(doc_list)
        idf[word] = math.log(total_docs / doc_freq)
    return idf

# Main Execution
def main():
    print("Loading documents...")
    documents = load_documents(PAGES_FOLDER)

    print(f"Total documents: {len(documents)}")

    print("Building inverted index...")
    inverted_index, total_docs = build_inverted_index(documents)

    print(f"Total unique terms: {len(inverted_index)}")

    print("Computing IDF...")
    idf = compute_idf(inverted_index, total_docs)

    # Save to disk
    with open("inverted_index.json", "w", encoding="utf-8") as f:
        json.dump(inverted_index, f)

    with open("idf.json", "w", encoding="utf-8") as f:
        json.dump(idf, f)

    print("Indexing complete.")
    print("Files saved:")
    print(" - inverted_index.json")
    print(" - idf.json")

    # Sample Output
    sample_words = list(inverted_index.keys())[:5]
    print("\nSample index entries:")
    for word in sample_words:
        print(word, "->", inverted_index[word])

    print("\nSample IDF values:")
    for word in sample_words:
        print(word, "->", idf[word])


if __name__ == "__main__":
    main()