import json

# File path
file_path = r"E:\DreamProject\Ai_Agent_fineTuning\RAGforSearch\dataset\json2\linksfromCHATGPT.json"
output_path = r"E:\DreamProject\Ai_Agent_fineTuning\RAGforSearch\dataset\json2\cleaned_links.json"

# Load JSON data from file
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# Removing duplicates based on 'url'
unique_data = []
seen_urls = set()

for entry in data:
    if entry["url"] not in seen_urls:
        unique_data.append(entry)
        seen_urls.add(entry["url"])

# Save cleaned data to a new file
with open(output_path, "w", encoding="utf-8") as outfile:
    json.dump(unique_data, outfile, indent=4)

print(f"Duplicates removed! Cleaned data saved to: {output_path}")
