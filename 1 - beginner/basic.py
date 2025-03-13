import os

from openai import OpenAI
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

# -----------------------------------------------------------------------------
# Retrieving parameters from environment variables
# -----------------------------------------------------------------------------

my_api_key = str(os.getenv("OPENAI_API_KEY"))
if my_api_key == "":
    print("No OpenAI API Key found!")
    exit(0)

client = OpenAI(api_key=my_api_key)

# -----------------------------------------------------------------------------
# Call the model
# -----------------------------------------------------------------------------

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You're a helpful assistant."},
        {
            "role": "user",
            "content": "Write a joke about the Go programming language.",
        },
    ],
)

response = completion.choices[0].message.content
print(response)