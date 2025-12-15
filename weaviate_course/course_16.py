from ollama import ChatResponse, chat

messages = [
    {
        "role": "user",
        "content": "Hi there. Please explain how language models work, in just a sentence or two.",
    }
]

# Initial response from the model
response: ChatResponse = chat(model="gemma3:1b", messages=messages)

# Append the initial response to the messages
messages.append(
    {
        "role": "assistant",
        "content": response.message.content,
    }
)

# Provide a follow-up prompt
messages.append(
    {
        "role": "user",
        "content": "Ah, I see. Now, can you write that in a Haiku?",
    }
)

response: ChatResponse = chat(model="gemma3:1b", messages=messages)

# This response will take both the initial and follow-up prompts into account
print(response.message.content)
