# API Code for Search Engine using FAISS
from flask import Flask, request, jsonify
import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

app = Flask(__name__)

# Paths
tokenized_path = "E:/DreamProject/Ai_Agent_fineTuning/RAGforSearch/dataset/tokenized_data.json"
index_path = "E:/DreamProject/Ai_Agent_fineTuning/RAGforSearch/dataset/faiss_index.index"

# Load Data and Index
with open(tokenized_path, "r", encoding="utf-8") as file:
    data = json.load(file)

index = faiss.read_index(index_path)

# Load Model for Query Embedding
model = SentenceTransformer("all-MiniLM-L6-v2")

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    # Generate Embedding for Query
    query_embedding = model.encode([query]).astype(np.float32)

    # Perform Search using FAISS
    k = 10  # Number of results
    distances, indices = index.search(query_embedding, k)

    # Fetch Results
    results = []
    for i in range(len(indices[0])):
        if indices[0][i] < len(data):
            results.append({
                "url": data[indices[0][i]]["url"],
                "title": data[indices[0][i]]["title"],
                "description": data[indices[0][i]]["description"],
                "distance": float(distances[0][i])
            })

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

print("✅ Search API is running on http://localhost:5000/search?query=your_query")
