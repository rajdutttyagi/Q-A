from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm_validator = ChatGroq(model_name="llama3-8b-8192", api_key=GROQ_API_KEY)

def validate_answer(answer, context):
    prompt = f"""
    Check if the following answer is fully supported by the provided context. 
    If yes, return "VALID". If no, return "HALLUCINATED".

    Context:
    {context}

    Answer:
    {answer}
    """

    response = llm_validator.invoke(prompt)
    return response.content.strip()
