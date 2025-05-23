import cohere

API_KEY = "TgyrJfpx02UujwLyhe7qodbRR0NSsSTLMlBWCZvo"
client = cohere.Client(API_KEY)

response = client.chat(
    model="command-xlarge-nightly",
    messages=[
        {"role": "user", "content": "Rewrite this sentence in a casual tone."}
    ]
)

print(response.choices[0].message.content)
