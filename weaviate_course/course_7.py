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
    single_prompt="Translate this into French: {title}",
)

# Inspect the response
for o in response.objects:
    print(o.properties["title"])  # Print the title
    print(o.generative.text)  # Print the generated text (the title, in French)

client.close()
