import ollama
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "system",
            "content": "Give answers in 1S lines only."
        },
        {
            "role": "user",
            "content": "explain AI?"

        }
    ]
)
print(response["message"]["content"])