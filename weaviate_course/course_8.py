import os

import weaviate

headers = {
    "X-Cohere-Api-Key": os.getenv("COHERE_APIKEY")
}  # Replace with your Cohere API key

client = weaviate.connect_to_local(headers=headers)

# Configure collection object
movies = client.collections.use("Movies")

# Perform query
response = movies.generate.near_text(
    query="dystopian future",
    limit=5,
    grouped_task="What do these movies have in common?",
    # grouped_properties=["title", "overview"]  # Optional parameter; for reducing prompt length
)

# Inspect the response
for o in response.objects:
    print(o.properties["title"])  # Print the title
print(
    response.generative.text
)  # Print the generated text (the commonalities between them)

client.close()
