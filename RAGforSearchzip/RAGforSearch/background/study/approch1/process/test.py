import json

# Load the Inverted Index JSON
file_path = r"E:\DreamProject\Ai_Agent_fineTuning\RAGforSearch\background\study\approch1\dataset\inverted_index.json"

with open(file_path, "r", encoding="utf-8") as f:
    inverted_index = json.load(f)

# Count total unique words
total_words = len(inverted_index)

# Count total word-document associations
total_occurrences = sum(len(docs) for docs in inverted_index.values())

print(f"✅ Total Unique Words: {total_words}")
print(f"✅ Total Word-Document Associations: {total_occurrences}")
