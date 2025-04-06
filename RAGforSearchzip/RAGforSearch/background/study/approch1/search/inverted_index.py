import json
import re
from collections import defaultdict
import os

# Preprocessing Function
def preprocess(text):
    """Lowercase, remove punctuation, and tokenize text."""
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)  # Remove numbers and special characters
    return text.split()

# Load Inverted Index
def load_inverted_index(index_path):
    try:
        with open(index_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❗ Error: Inverted index not found at {index_path}")
        return {}
    except json.JSONDecodeError:
        print("❗ Error: Failed to decode JSON data.")
        return {}

# Perform Search in Inverted Index
def search_inverted_index(query, inverted_index):
    words = preprocess(query)
    if not words:
        return set()

    # Fetch results for each word from the inverted index
    results = [set(inverted_index.get(word, [])) for word in words]

    # Perform intersection to get documents matching all query words
    if results:
        return set.intersection(*results) if len(results) > 1 else results[0]
    return set()

# Display Results with Titles
def display_results(result_docs, data):
    if not result_docs:
        print("🔎 No results found.")
    else:
        print(f"✅ Found {len(result_docs)} results:")
        for doc_id in result_docs:
            doc = data.get(doc_id, {})
            print(f"📄 Title: {doc.get('title', 'Unknown')}")
            print(f"🔗 URL: {doc.get('url', 'Unknown')}")
            print(f"📝 Description: {' '.join(doc.get('description', []))[:200]}...\n")

# Main Function
def main():
    # File paths
    base_path = r"E:\DreamProject\Ai_Agent_fineTuning\RAGforSearch\background\study\approch1\dataset"
    document_path = os.path.join(base_path, "document_map.json")
    index_path = os.path.join(base_path, "inverted_index.json")

    # Load Data
    print("📥 Loading data and index...")
    inverted_index = load_inverted_index(index_path)
    try:
        with open(document_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"❗ Error: Document data not found at {document_path}")
        return

    print("✅ Data and Inverted Index Loaded Successfully!")
    
    # Perform Queries
    while True:
        query = input("🔎 Enter your search query (or type 'exit' to quit): ").strip()
        if query.lower() == 'exit':
            print("👋 Exiting Search.")
            break
        
        result_docs = search_inverted_index(query, inverted_index)
        display_results(result_docs, data)

# Run the Program
if __name__ == "__main__":
    main()
