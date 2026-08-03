from langchain_groq import ChatGroq
from hr_assistant import config

def get_llm():
    """Return a ChatGroq LLM instance"""
    return ChatGroq(
        model=config.LLM_MODEL_NAME,
        temperature=0.0,
        api_key=config.GROQ_API_KEY
    )