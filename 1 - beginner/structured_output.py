import os

from langchain_openai import ChatOpenAI
from dotenv import find_dotenv, load_dotenv
from pydantic import BaseModel, Field


# -----------------------------------------------------------------------------
# Retrieving parameters from environment variables
# -----------------------------------------------------------------------------

load_dotenv(find_dotenv())

my_api_key = str(os.getenv("OPENAI_API_KEY"))
if my_api_key == "":
    print("No OpenAI API Key found!")
    exit(0)

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # api_key="...",  # if you prefer to pass api key in directly instaed of using env vars
    # base_url="...",
    # organization="...",
    # other params...
)

# -----------------------------------------------------------------------------
# Define structured output format
# -----------------------------------------------------------------------------

class SearchQuery(BaseModel):
    search_query: str = Field(None, description="Query that is optimized web search.")
    justification: str = Field(
        None, description="Why this query is relevant to the user's request."
    )

# -----------------------------------------------------------------------------
# Augment the LLM with schema for structured output
# -----------------------------------------------------------------------------

structured_llm = llm.with_structured_output(SearchQuery)

# -----------------------------------------------------------------------------
# Invoke the augmented LLM and print the results
# -----------------------------------------------------------------------------

output = structured_llm.invoke("How does Calcium CT score relate to high cholesterol?")

print (output.search_query)
print (output.justification)
