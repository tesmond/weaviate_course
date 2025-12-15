import os

import cohere

cohere_api_key = os.getenv("COHERE_API_KEY")
co = cohere.ClientV2(api_key=cohere_api_key)

# Get the query embedding:
query_text = "Intergalactic voyage"

response = co.embed(
    texts=[query_text],
    model="embed-english-light-v3.0",
    input_type="search_query",
    embedding_types=["float"],
)

query_embedding = response.embeddings.float_[0]

print(len(query_embedding))
print(query_embedding[:5])
