class AsyncPrBot:
    def __init__(self, anthropic_client):
        self.client = anthropic_client

    def work_on_ticket(self, file_content: str, instructions: str) -> str:
        prompt = f"""
        You are a senior software engineer and expert in Python code quality, design patterns, and maintainability.

        You will receive:
        1. A complete Python source file.
        2. A task description with instructions similar to a Jira ticket or GitHub issue.

        Your task:
        - Return ONLY the full, revised Python file with all necessary edits applied.
        - DO NOT include explanations, comments, or summaries.
        - Ensure changes strictly follow the task description while maintaining idiomatic, readable, and performant
        Python code.
        - Preserve the original formatting and module structure unless otherwise instructed.
        - Do not add formatting or tick marks to the final output. The output must be able to be plugged into a Python
        file and ran as-is.

        Original Python file:
        {file_content}

        Task instructions:
        {instructions}

        Begin now.
        """

        try:
            message = self.client.messages.create(
                model="claude-opus-4-20250514", max_tokens=2000, messages=[{"role": "user", "content": prompt}]
            )
            return message.content[0].text
        except Exception as e:
            raise Exception(f"Failed to process code with Claude: {e}") from e
