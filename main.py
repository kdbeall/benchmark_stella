import time
from sentence_transformers import SentenceTransformer
from business_texts import business_texts

import torch
print("GPU is available" if torch.cuda.is_available() else "GPU not available")
print(torch.cuda.get_device_name(0) if torch.cuda.is_available() else "")

# Load the Stella model with 1024-dimensional embedding
device = "cuda" if torch.cuda.is_available() else "cpu"
model = SentenceTransformer("dunzhang/stella_en_400M_v5", trust_remote_code=True).to(device)

# Benchmark the embedding process
start_time = time.time()

# s2p (sentence-to-passage): For retrieval tasks.
# s2s (sentence-to-sentence): For semantic textual similarity tasks.
embeddings = model.encode(business_texts, prompt_name="s2p_query", device=device)
print("This is a sample embedding")
print(embeddings[0])
print("")
end_time = time.time()

# Calculate time per embedding
total_time = end_time - start_time
time_per_embedding = total_time / len(business_texts)
time_per_embedding_ms = time_per_embedding * 1000

# Output results
print(f"Total embedding time: {total_time:.4f} seconds")
print(f"Time per embedding: {time_per_embedding:.4f} seconds")
print(f"Time per embedding: {time_per_embedding_ms:.2f} milliseconds")
