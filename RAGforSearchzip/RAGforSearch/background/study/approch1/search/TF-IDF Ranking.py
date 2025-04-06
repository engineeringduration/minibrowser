import json
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Load document map
with open("E:/DreamProject/Ai_Agent_fineTuning/RAGforSearch/background/study/approch1/dataset/document_map.json", "r") as f:
    document_map = json.load(f)

# Prepare document texts
doc_ids = list(document_map.keys())
doc_texts = [" ".join(doc["description"]) for doc in document_map.values()]

# Compute TF-IDF matrix
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(doc_texts)

def tfidf_search(query, top_n=5):
    query_vec = vectorizer.transform([query])  # Convert query to vector
    scores = np.dot(tfidf_matrix, query_vec.T).toarray().flatten()  # Compute similarity scores
    ranked_indices = np.argsort(scores)[::-1][:top_n]  # Get top-N ranked results
    
    results = [
        {
            "title": document_map[doc_ids[i]]["title"],
            "url": document_map[doc_ids[i]]["url"],
            "description": " ".join(document_map[doc_ids[i]]["description"]),
            "score": scores[i]
        }
        for i in ranked_indices if scores[i] > 0  # Ignore zero-score results
    ]
    
    return results

# Test Query
query = "neuroscience research"
results = tfidf_search(query)
for res in results:
    print(res)
