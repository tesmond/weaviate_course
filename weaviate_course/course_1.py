import weaviate

headers = {
    # "X-Cohere-Api-Key": os.getenv("COHERE_APIKEY")
}  # Replace with your Cohere API key

client = weaviate.connect_to_local(headers=headers)
print("Weaviate is ready:", client.is_ready())
client.close()
