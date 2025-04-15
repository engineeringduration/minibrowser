from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# Paths
tokenized_path = "RAGforSearchzip/RAGforSearch/dataset/tokenized_data.json"
index_path = "RAGforSearchzip/RAGforSearch/dataset/faiss_index.index"

# Configure Gemini
GEMINI_API_KEY = "AIzaSyBwKXeud2Y2FmENDee3igwOYMvJ1gkFrys"
genai.configure(api_key=GEMINI_API_KEY)

# Load SentenceTransformer
embed_model = SentenceTransformer("all-MiniLM-L6-v2")
print("✅ SentenceTransformer model loaded.")

# Load FAISS index and data
with open(tokenized_path, "r", encoding="utf-8") as f:
    data = json.load(f)
index = faiss.read_index(index_path)
print("✅ FAISS index and data loaded.")

# Load Gemini Model
gemini_model = genai.GenerativeModel("gemini-2.0-flash")
print("✅ Gemini model loaded.")


# Helper: Classify Query Intent
def classify_intent(query):
    q = query.lower()
    if any(q.startswith(w) for w in ["how", "what", "why", "when", "where"]):
        return "informational"
    elif "buy" in q or "purchase" in q:
        return "transactional"
    elif "visit" in q or ".com" in q:
        return "navigational"
    else:
        return "general"


# Helper: Generate Gemini Answer
def generate_ai_answer(query):
    try:
        prompt = f"""
You are Jack, a smart and helpful AI. Please give a short, clear, and friendly response to the query below. Keep it **very concise**, like the AI sections in Google or Brave search.

- Maximum 15 sentences
- Highlight **important terms** in bold using markdown (**word**)
- Include **1-2 relevant clickable links** if needed (in markdown format: [text](url))
- No long intros or conclusions
- Get straight to the point

Query: "{query}"
"""

        response = gemini_model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"❗ Gemini error: {e}")
        return "Sorry, I couldn't generate an answer right now."


# ---------------------- ROUTE 1: Fast FAISS Search ---------------------
@app.route('/search_links', methods=['GET'])
def search_links():
    try:
        query = request.args.get('query')
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))

        if not query:
            return jsonify({"error": "Missing 'query' parameter"}), 400

        query_embedding = embed_model.encode([query]).astype(np.float32)
        distances, indices = index.search(query_embedding, page * per_page)

        results = []
        start_index = (page - 1) * per_page
        end_index = min(start_index + per_page, len(indices[0]))

        for i in range(start_index, end_index):
            doc_id = indices[0][i]
            if doc_id < len(data):
                results.append({
                    "url": data[doc_id]["url"],
                    "title": data[doc_id]["title"],
                    "description": data[doc_id]["description"],
                    "distance": float(distances[0][i])
                })

        intent = classify_intent(query)

        return jsonify({
            "query": query,
            "intent": intent,
            "results": results,
            "page": page,
            "per_page": per_page,
            "total_results": len(indices[0])
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ---------------------- ROUTE 2: Slow AI Answer ---------------------
@app.route('/ai_answer', methods=['GET'])
def ai_answer():
    try:
        query = request.args.get('query')
        if not query:
            return jsonify({"error": "Missing 'query' parameter"}), 400

        intent = classify_intent(query)
        ai_response = generate_ai_answer(query) if intent in ["informational", "transactional", "navigational", "general"] else None

        return jsonify({
            "query": query,
            "intent": intent,
            "ai_answer": ai_response
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ---------------------- MAIN -------------------------------
if __name__ == '__main__':
    app.run(debug=True, port=5000, threaded=True)

print("🚀 API running at http://localhost:5000/")
print("🔍 Use http://localhost:5000/search_links?query=your_query for fast search.")
print("🤖 Use http://localhost:5000/ai_answer?query=your_query for AI-generated answers.")