import os

import weaviate
from weaviate.classes.config import Configure, DataType, Property

headers = {
    "X-Cohere-Api-Key": os.getenv("COHERE_APIKEY")
}  # Replace with your Cohere API key

client = weaviate.connect_to_local(headers=headers)

client.collections.create(
    name="Movies",
    properties=[
        Property(name="title", data_type=DataType.TEXT),
        Property(name="overview", data_type=DataType.TEXT),
        Property(name="vote_average", data_type=DataType.NUMBER),
        Property(name="genre_ids", data_type=DataType.INT_ARRAY),
        Property(name="release_date", data_type=DataType.DATE),
        Property(name="tmdb_id", data_type=DataType.INT),
    ],
    # Define the vectorizer module
    vector_config=Configure.Vectors.text2vec_cohere(model="embed-v4.0"),
    # Define the generative module
    generative_config=Configure.Generative.cohere(model="command-a-03-2025"),
)

client.close()
