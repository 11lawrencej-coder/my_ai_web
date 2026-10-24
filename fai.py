import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load .env file
load_dotenv()

# Make sure the key actually loaded
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise Exception("ERROR: GROQ_API_KEY not found. Make sure your .env file is in the SAME folder as this script.")

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