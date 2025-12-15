import os

import cohere

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
