import json

# Load JSON dataset
file_path = r"E:\DreamProject\Ai_Agent_fineTuning\RAGforSearch\dataset\json2\cleaned_links.json"

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Generate unique IDs and store mapping
document_map = {}

for idx, doc in enumerate(data):
    doc_id = f"AsEo{idx+1:02d}"  # Generates IDs like AsEo01, AsEo02, ...
    document_map[doc_id] = doc  # Map ID to the document

# Save structured data to a new JSON file
output_file = r"E:\DreamProject\Ai_Agent_fineTuning\RAGforSearch\background\study\approch1\dataset\document_map.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(document_map, f, indent=4)

print("✅ Document Mapping Created & Saved!")
