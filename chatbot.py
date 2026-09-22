import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
if not API_KEY:
    print("Error: API_KEY is not configured.")
    print("Please add your API key to the .env file.")
    exit()
URL = "https://api.kie.ai/codex/v1/responses"

conversation = []

print("🤖 GPT-6 Astra Chatbot")
print("Type 'exit' to quit\n")


def ask_gpt(message):
    conversation.append({
        "role": "user",
        "content": [
            {
                "type": "input_text",
                "text": message
            }
        ]
    })

    payload = {
        "model": "gpt-6-astra",
        "input": conversation,
        "stream": False,
        "reasoning": {
            "effort": "medium"
        }
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(
            URL,
            headers=headers,
            json=payload
        )

        response.raise_for_status()
        data = response.json()

        assistant_message = ""

        for item in data.get("output", []):
            if item.get("type") == "message":
                for content in item.get("content", []):
                    if content.get("type") == "output_text":
                        assistant_message += content.get("text", "")

        conversation.append({
            "role": "assistant",
            "content": [
                {
                    "type": "output_text",
                    "text": assistant_message
                }
            ]
        })

        return assistant_message

    except Exception as e:
        return f"Error: {e}"


while True:
    user_message = input("You: ")

    if user_message.lower() in ["exit", "quit", "bye"]:
        print("Bot: Goodbye! 👋")
        break

    print("\nBot is thinking...\n")

    answer = ask_gpt(user_message)

    print("GPT-6 Astra:", answer)
    print()