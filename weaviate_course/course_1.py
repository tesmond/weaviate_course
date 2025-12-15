import json

import weaviate

headers = {
    # "X-Cohere-Api-Key": os.getenv("COHERE_APIKEY")
}  # Replace with your Cohere API key
try:
    client = weaviate.connect_to_local(headers=headers)
    print("Weaviate is ready:", client.is_ready())

    assert client.is_ready()
    metainfo = client.get_meta()
    print(json.dumps(metainfo, indent=2))
finally:
    client.close()
