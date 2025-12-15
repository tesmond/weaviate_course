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

# Initial response from the model
response = co.chat(
    model="command-r-plus-08-2024",
    messages=messages,
)

# Append the initial response to the messages
messages.append(
    {
        "role": "assistant",
        "content": response.message.content[0].text,
    }
)

# Provide a follow-up prompt
messages.append(
    {
        "role": "user",
        "content": "Ah, I see. Now, can you write that in a Haiku?",
    }
)

response = co.chat(
    model="command-r-plus-08-2024",
    messages=messages,
)

# This response will take both the initial and follow-up prompts into account
print(response.message.content[0].text)
