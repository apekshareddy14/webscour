import json
import math
import re

# Load index files
with open("inverted_index.json", "r") as f:
    inverted_index = json.load(f)

with open("idf.json", "r") as f:
    idf = json.load(f)


def tokenize(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text.split()


def search(query):
    tokens = tokenize(query)

    scores = {}

    for word in tokens:
        if word in inverted_index:

            postings = inverted_index[word]

            for doc, tf in postings:

                score = tf * idf[word]

                if doc not in scores:
                    scores[doc] = 0

                scores[doc] += score

    ranked_results = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    return ranked_results[:10]


if __name__ == "__main__":

    while True:
        query = input("Enter search query: ")

        results = search(query)

        for doc, score in results:
            print(doc, "Score:", score)