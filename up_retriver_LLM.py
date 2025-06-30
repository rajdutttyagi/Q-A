import os
from dotenv import load_dotenv
from hallucination import validate_answer
from websearch import get_web_context
from quer_routey import retrieve_docs, route_query
from langchain_groq import ChatGroq

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
llm = ChatGroq(model_name="llama3-8b-8192", api_key=GROQ_API_KEY)

def answer_user_query(user_query):
    """Query -> Routing -> Context -> LLM -> Validation"""

    if route_query(user_query) == "web":
        context = get_web_context(user_query)
    else:
        text_results, table_results = retrieve_docs(user_query)
        context_parts = []

        for doc in text_results.get("documents", []):
            context_parts.append(doc if isinstance(doc, str) else "\n".join(doc))

        for doc in table_results.get("documents", []):
            context_parts.append(doc if isinstance(doc, str) else "\n".join(doc))

        context = '\n'.join(context_parts)

    prompt = f"""
    User Query: {user_query}
    Context:
    {context}
    ----
    Answer clearly and concisely based on the context.
    """

    try:
        response = llm.invoke(prompt)
        validated = validate_answer(response, context)

        return validated
    except Exception as e:
        return f"⚠️ Error: {str(e)}"
