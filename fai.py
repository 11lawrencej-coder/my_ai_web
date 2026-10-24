import os
import markdown
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.7,
    api_key=os.getenv("GROQ_API_KEY")
)

def run(choice):
    response = llm.invoke(choice)
    md_text = response.content
    html = markdown.markdown(md_text)
    return html
