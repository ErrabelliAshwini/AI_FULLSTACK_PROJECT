import ollama
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": "What is AI?  what are types of ai and explain them in them in the 20 words"

        }
        ]
)
print(response["message"]["content"])