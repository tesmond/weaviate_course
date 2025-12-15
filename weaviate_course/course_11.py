import os

import cohere
import numpy as np

cohere_api_key = os.getenv("COHERE_API_KEY")
co = cohere.ClientV2(api_key=cohere_api_key)

source_texts = [
    "You're a wizard, Harry.",
    "Space, the final frontier.",
    "I'm going to make him an offer he can't refuse.",
]

response = co.embed(
    texts=source_texts,
    model="embed-english-light-v3.0",
    input_type="search_document",
    embedding_types=["float"],
)

source_embeddings = []
for e in response.embeddings.float_:
    print(len(e))  # This will be the length of the embedding vector
    print(e[:5])  # This will print the first 5 elements of the embedding vector
    source_embeddings.append(e)  # Save the embedding for later use


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

# Find the most similar source text to the query:

# Calculate the dot product between the query embedding and each source embedding
dot_products = [np.dot(query_embedding, e) for e in source_embeddings]

# Find the index of the maximum dot product
most_similar_index = np.argmax(dot_products)

# Get the most similar source text
most_similar_text = source_texts[most_similar_index]

print(f"The most similar text to '{query_text}' is:")
print(most_similar_text)
