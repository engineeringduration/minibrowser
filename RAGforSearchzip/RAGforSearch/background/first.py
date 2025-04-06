import json
import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# Load JSON file
file_path = "E:/DreamProject/Ai_Agent_fineTuning/RAGforSearch/dataset/ALLdata.json"
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# Convert to DataFrame
df = pd.DataFrame(data)

# Clean descriptions: Join into a single text block
df["description"] = df["description"].apply(lambda x: " ".join(x) if x else "")

# Load SBERT Model for embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")

# Convert title + description into embeddings
df["embeddings"] = df.apply(lambda row: model.encode(row["title"] + " " + row["description"]), axis=1)

# Convert embeddings to NumPy array
embeddings_matrix = np.vstack(df["embeddings"].values)

# Create FAISS index (L2 distance)
index = faiss.IndexFlatL2(embeddings_matrix.shape[1])
index.add(embeddings_matrix)

# Search function to retrieve top-k results
def search(query, top_k=10):
    query_embedding = model.encode(query).reshape(1, -1)
    distances, indices = index.search(query_embedding, top_k)
    results = [{"url": df.iloc[idx]["url"], "title": df.iloc[idx]["title"], "description": df.iloc[idx]["description"]} for idx in indices[0]]
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
