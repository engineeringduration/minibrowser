from sklearn.metrics.pairwise import cosine_similarity

def cosine_similarity_search(query, top_n=5):
    query_vec = vectorizer.transform([query])  # Convert query to vector
    similarities = cosine_similarity(tfidf_matrix, query_vec).flatten()  # Compute cosine similarity
    ranked_indices = np.argsort(similarities)[::-1][:top_n]  # Get top results

    results = [
        {
            "title": document_map[doc_ids[i]]["title"],
            "url": document_map[doc_ids[i]]["url"],
            "description": " ".join(document_map[doc_ids[i]]["description"]),
            "similarity_score": similarities[i]
        }
        for i in ranked_indices if similarities[i] > 0
    ]

    return results

# Test Query
results = cosine_similarity_search(query)
for res in results:
    print(res)
