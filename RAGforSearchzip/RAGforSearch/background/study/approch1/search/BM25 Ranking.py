import math

# BM25 Parameters
k1 = 1.5
b = 0.75

# Compute document lengths
document_lengths = {doc_id: len(" ".join(doc["description"])) for doc_id, doc in document_map.items()}
avg_doc_length = sum(document_lengths.values()) / len(document_lengths)

def compute_bm25_score(query, doc_id):
    query_words = query.lower().split()
    score = 0
    for word in query_words:
        if word in inverted_index and doc_id in inverted_index[word]:
            tf = inverted_index[word].count(doc_id)
            df = len(inverted_index[word])
            idf = math.log((len(document_map) - df + 0.5) / (df + 0.5) + 1)
            dl = document_lengths[doc_id]
            score += idf * ((tf * (k1 + 1)) / (tf + k1 * (1 - b + b * (dl / avg_doc_length))))
    return score

def bm25_search(query, top_n=5):
    relevant_docs = set()
    for word in query.lower().split():
        if word in inverted_index:
            relevant_docs.update(inverted_index[word])

    scored_results = [
        {
            "title": document_map[doc_id]["title"],
            "url": document_map[doc_id]["url"],
            "description": " ".join(document_map[doc_id]["description"]),
            "score": compute_bm25_score(query, doc_id)
        }
        for doc_id in relevant_docs if doc_id in document_map
    ]

    scored_results.sort(key=lambda x: x["score"], reverse=True)
    return scored_results[:top_n]

# Test Query
results = bm25_search(query)
for res in results:
    print(res)
