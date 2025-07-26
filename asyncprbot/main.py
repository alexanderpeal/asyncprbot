import os
import sys
from anthropic import Anthropic
from dotenv import load_dotenv

def main():
    load_dotenv()

    api_key = os.getenv("ANTHROPIC_API_KEY")

    if api_key is None:
        print("Error: ANTHROPIC_API_KEY environment variable not found")
        sys.exit(1)

    try:
        client = Anthropic(
            api_key=api_key
        )

        user_messages = [
            "Hello, Claude!"
        ]

        message = client.messages.create(
            model="claude-opus-4-20250514",
            max_tokens=100,
            messages=[
                {
                    "role": "user",
                    "content": user_messages[0]
                }
            ]
        )

        print("Connected to Claude!")
        print("You said: ", user_messages[0])
        print("Claude says: ", message.content[0].text)
    
    except Exception as e:
        print(f"Error connecting to Claude API: {e}")

if __name__ == "__main__":
    main()
