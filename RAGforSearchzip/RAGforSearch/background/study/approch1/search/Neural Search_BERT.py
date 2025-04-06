from sentence_transformers import SentenceTransformer
import faiss

# Load a BERT-based model for sentence embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")

# Encode document texts into vectors
doc_embeddings = model.encode(doc_texts, convert_to_numpy=True)
doc_ids = list(document_map.keys())

# Store embeddings in FAISS index
index = faiss.IndexFlatL2(doc_embeddings.shape[1])
index.add(doc_embeddings)

def neural_search(query, top_n=5):
    query_embedding = model.encode([query], convert_to_numpy=True)
    D, I = index.search(query_embedding, top_n)  # Get top-N closest matches
    
    results = [
        {
            "title": document_map[doc_ids[i]]["title"],
            "url": document_map[doc_ids[i]]["url"],
            "description": " ".join(document_map[doc_ids[i]]["description"]),
            "similarity_score": 1 - D[0][i]  # Higher score means better match
        }
        for i in I[0]
    ]
    
    return results

# Test Query
results = neural_search(query)
for res in results:
    print(res)
