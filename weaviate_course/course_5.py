import os

import weaviate
from weaviate.classes.query import MetadataQuery

headers = {
    "X-Cohere-Api-Key": os.getenv("COHERE_APIKEY")
}  # Replace with your Cohere API key

client = weaviate.connect_to_local(headers=headers)


# Configure collection object
movies = client.collections.use("Movies")

# Perform query
response = movies.query.bm25(
    query="history", limit=5, return_metadata=MetadataQuery(score=True)
)

# Inspect the response
for o in response.objects:
    print(
        o.properties["title"], o.properties["release_date"].year
    )  # Print the title and release year (note the release date is a datetime object)
    print(
        f"BM25 score: {o.metadata.score:.3f}\n"
    )  # Print the BM25 score of the object from the query

client.close()
