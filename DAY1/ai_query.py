import ollama
response = ollama.chat(
    model="llama3.2:3b",
    message=[
        {
            "role": "user",
            "content": "Plan a trip to goa."
        }
        ]
)
print(response["message"]["content"])';lweryi'