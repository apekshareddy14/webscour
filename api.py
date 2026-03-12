from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import re

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load index files
with open("inverted_index.json") as f:
    inverted_index = json.load(f)

with open("idf.json") as f:
    idf = json.load(f)


def tokenize(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text.split()


def search(query):
    tokens = tokenize(query)
    scores = {}

    for word in tokens:
        if word in inverted_index:
            for doc, tf in inverted_index[word]:
                score = tf * idf[word]
                scores[doc] = scores.get(doc, 0) + score

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    return [{"document": doc, "score": score} for doc, score in ranked[:10]]


@app.get("/search")
def search_api(q: str):
    return search(q)