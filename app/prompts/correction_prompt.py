CORRECTION_PROMPT = """
Your previous response was invalid.

The validation error was:

{error}

Your previous JSON was:

{response}

Fix the JSON.

Rules:
1. Remove fields that are not allowed.
2. Keep only fields defined in the schema.
3. Return valid JSON only.
4. Do not add explanations.
"""