import numpy as np
import ollama

source_texts = [
    "You're a wizard, Harry.",
    "Space, the final frontier.",
    "I'm going to make him an offer he can't refuse.",
]

response = ollama.embed(model="snowflake-arctic-embed:110m", input=source_texts)

source_embeddings = []
for e in response.embeddings:
    print(len(e))  # This will be the length of the embedding vector
    print(e[:5])  # This will print the first 5 elements of the embedding vector
    source_embeddings.append(e)  # Save the embedding for later use

# Get the query embedding:
query_text = "Intergalactic voyage"

response = ollama.embed(model="snowflake-arctic-embed:110m", input=query_text)

query_embedding = response.embeddings[0]

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
