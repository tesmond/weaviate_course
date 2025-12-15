import os
from datetime import datetime, timezone

import weaviate
from weaviate.classes.query import Filter, MetadataQuery

headers = {
    "X-Cohere-Api-Key": os.getenv("COHERE_APIKEY")
}  # Replace with your Cohere API key

client = weaviate.connect_to_local(headers=headers)

# Configure collection object
movies = client.collections.use("Movies")

# Perform query
response = movies.query.near_text(
    query="dystopian future",
    limit=5,
    return_metadata=MetadataQuery(distance=True),
    filters=Filter.by_property("release_date").greater_than(
        datetime(
            2020, 1, 1, tzinfo=timezone.utc
        )  # add timezone to avoid timezone warning
    ),
)

# Inspect the response
for o in response.objects:
    print(
        o.properties["title"], o.properties["release_date"].year
    )  # Print the title and release year (note the release date is a datetime object)
    print(
        f"Distance to query: {o.metadata.distance:.3f}\n"
    )  # Print the distance of the object from the query

client.close()
