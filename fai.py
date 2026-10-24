import os
from langchain_groq import ChatGroq

# Get the API key directly from Render's environment variable
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise Exception("ERROR: GROQ_API_KEY not found. Set it in Render's Environment tab.")

# Create the LLM client
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.7,
    api_key=api_key
)

def run(choice: str):
    """Send text to Groq and return the response."""
    response = llm.invoke(choice)
    return response.content
