import os
import sys

from anthropic import Anthropic
from dotenv import load_dotenv

from asyncprbot.asyncprbot import AsyncPrBot


def main():
    load_dotenv()

    api_key = os.getenv("ANTHROPIC_API_KEY")

    if api_key is None:
        print("Error: ANTHROPIC_API_KEY environment variable not found")
        sys.exit(1)

    try:
        client = Anthropic(api_key=api_key)

        bot = AsyncPrBot(client)

        calculator_code = """
        def add(a, b):
            return a + b

        def subtract(a, b):
            return a - b

        print("Calculator ready!")
        print("5 + 3 =", add(5, 3))
        print("10 - 4 =", subtract(10, 4))
        """

        instructions = """Add a multiply function that takes two parameters and returns their product. Also add a print
        statement that demonstrates the multiply function with 4 and 6."""

        modified_code = bot.work_on_ticket(file_content=calculator_code, instructions=instructions)

        print(modified_code)

    except Exception as e:
        print(f"Error connecting to Claude API: {e}")


if __name__ == "__main__":
    main()
