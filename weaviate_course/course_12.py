import os

import cohere

cohere_api_key = os.getenv("COHERE_API_KEY")
co = cohere.ClientV2(api_key=cohere_api_key)

messages = [
    {
        "role": "user",
        "content": "Hi there. Please explain how language models work, in just a sentence or two.",
    }
]

response = co.chat(
    model="command-r-plus-08-2024",
    messages=messages,
)

print(response.message.content[0].text)
