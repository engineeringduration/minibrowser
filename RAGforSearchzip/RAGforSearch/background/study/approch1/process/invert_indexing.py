import json
import re
from collections import defaultdict
import json
import re
from collections import defaultdict

# Load JSON dataset
file_path = r"E:\DreamProject\Ai_Agent_fineTuning\RAGforSearch\background\study\approch1\dataset\document_map.json"

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Function to preprocess text (tokenization & normalization)
def preprocess(text):
    """Lowercases, removes punctuation, and tokenizes text."""
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)  # Remove numbers and special characters
    return text.split()

# Function to extract meaningful words from URLs (excluding numbers)
def extract_meaningful_url_parts(url):
    """Extracts only words from URLs, ignoring 'https', 'www', special chars, and numbers."""
    url = url.lower()
    url = re.sub(r"https?://(www\.)?", "", url)  # Remove 'http://', 'https://', 'www.'
    url = re.sub(r"[^a-z\s]", " ", url)  # Remove numbers and special characters
    return url.split()

# Create Inverted Index
inverted_index = defaultdict(set)  # {word: {doc_id1, doc_id2}}

for doc_id, doc in data.items():
    url_words = extract_meaningful_url_parts(doc["url"])  # Extract words from URL
    content = " ".join([doc["title"], " ".join(doc["description"]), " ".join(url_words)])
    words = preprocess(content)
    
    for word in words:
        inverted_index[word].add(doc_id)

# Convert sets to lists for JSON storage
inverted_index = {word: list(doc_ids) for word, doc_ids in inverted_index.items()}

# Save Inverted Index to a file
output_file = r"E:\DreamProject\Ai_Agent_fineTuning\RAGforSearch\background\study\approch1\dataset\inverted_index.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(inverted_index, f, indent=4)

print("✅ Optimized Inverted Index Created & Saved!")
