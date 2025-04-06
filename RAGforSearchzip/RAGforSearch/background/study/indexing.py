# Separate Code for Creating and Saving FAISS Index
import json
import numpy as np
import faiss

# Load Tokenized Data
tokenized_path = "E:/DreamProject/Ai_Agent_fineTuning/RAGforSearch/dataset/tokenized_data.json"

with open(tokenized_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# Extract Embeddings
df_embeddings = np.array([item["embeddings"] for item in data])

# Create FAISS Index
index = faiss.IndexFlatL2(df_embeddings.shape[1])
index.add(df_embeddings)

# Save Index
index_path = "E:/DreamProject/Ai_Agent_fineTuning/RAGforSearch/dataset/faiss_index.index"
faiss.write_index(index, index_path)

print("✅ FAISS index saved successfully!")
