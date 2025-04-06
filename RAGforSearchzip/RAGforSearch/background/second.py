# API Code for Search Engine using FAISS and SBERT
import json
import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load Tokenized Data and FAISS Index
tokenized_path = "E:/DreamProject/Ai_Agent_fineTuning/RAGforSearch/dataset/tokenized_data.json"
index_path = "E:/DreamProject/Ai_Agent_fineTuning/RAGforSearch/dataset/faiss_index.index"

with open(tokenized_path, "r", encoding="utf-8") as file:
    data = json.load(file)

df = pd.DataFrame(data)
index = faiss.read_index(index_path)

# Load SBERT Model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Search Function to Retrieve Top-k Results
def search(query, top_k=10):
    query_embedding = model.encode(query).reshape(1, -1)
    distances, indices = index.search(query_embedding, top_k)
    results = [{
        "url": df.iloc[idx]["url"],
        "title": df.iloc[idx]["title"],
        "description": df.iloc[idx]["description"]
    } for idx in indices[0]]
    return results

# Example Search
while True:
    query=input("enter the query: ")
#query = "Learn C programming"
    top_results = search(query)

# Print search results
    for res in top_results:
      print(res['url'])
    
    res=input("Do you want to enter query (y/n): ")
    if res=='y' or res=='Y':
        continue
    else:
        break