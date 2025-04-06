# API Code for Search Engine using FAISS
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

app = Flask(__name__)
CORS(app)

# Paths
tokenized_path = "R:/minibrowser/RAGforSearchzip/RAGforSearch/dataset/tokenized_data.json"
index_path = "R:/minibrowser/RAGforSearchzip/RAGforSearch/dataset/faiss_index.index"

# Load Data and Index
try:
    with open(tokenized_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    index = faiss.read_index(index_path)
    print("✅ FAISS index and data loaded successfully.")
except Exception as e:
    print(f"❗ Error loading index or data: {e}")

# Load Model for Query Embedding
try:
    model = SentenceTransformer("all-MiniLM-L6-v2")
    print("✅ Sentence Transformer Model Loaded.")
except Exception as e:
    print(f"❗ Error loading model: {e}")

# Search API with Pagination and Error Handling
@app.route('/search', methods=['GET'])
def search():
    try:
        query = request.args.get('query')
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))

        if not query:
            return jsonify({"error": "Query parameter is required"}), 400

        # Generate Embedding for Query
        query_embedding = model.encode([query]).astype(np.float32)

        # Perform Search using FAISS
        distances, indices = index.search(query_embedding, per_page * page)

        # Fetch Results with Pagination
        results = []
        start_index = (page - 1) * per_page
        end_index = min(start_index + per_page, len(indices[0]))

        for i in range(start_index, end_index):
            if indices[0][i] < len(data):
                results.append({
                    "url": data[indices[0][i]]["url"],
                    "title": data[indices[0][i]]["title"],
                    "description": data[indices[0][i]]["description"],
                    "distance": float(distances[0][i])
                })

        return jsonify({
            "results": results,
            "page": page,
            "per_page": per_page,
            "total_results": len(indices[0])
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Error Handler
@app.errorhandler(Exception)
def handle_error(e):
    return jsonify({"error": str(e)}), 500

# Run API
if __name__ == '__main__':
    app.run(debug=True, port=5000, threaded=True)

print("✅ Search API is running on http://localhost:5000/search?query=your_query")
