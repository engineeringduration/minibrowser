# First Code: Tokenizing and Saving JSON Data
import json
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

# Load JSON Data
file_path = "E:/DreamProject/Ai_Agent_fineTuning/RAGforSearch/dataset/ALLdata.json"
save_tokenized_path = "E:/DreamProject/Ai_Agent_fineTuning/RAGforSearch/dataset/tokenized_data.json"

with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# Convert to DataFrame
df = pd.DataFrame(data)

# Clean descriptions
df["description"] = df["description"].apply(lambda x: " ".join(x) if x else "")

# Load Sentence Transformer Model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate Embeddings
df["embeddings"] = df.apply(lambda row: model.encode(row["title"] + " " + row["description"]).tolist(), axis=1)

# Save Tokenized Data
with open(save_tokenized_path, "w", encoding="utf-8") as file:
    json.dump(df.to_dict(orient="records"), file)

print("✅ Tokenized data saved successfully!")