from ollama import ChatResponse, chat

messages = [
    {
        "role": "user",
        "content": "Hi there. Please explain how language models work, in just a sentence or two.",
    }
]

response: ChatResponse = chat(model="gemma3:1b", messages=messages)

print(response.message.content)
