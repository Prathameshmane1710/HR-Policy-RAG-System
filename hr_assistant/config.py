"""All settings for the app"""

import os
from dotenv import load_dotenv

load_dotenv()

## Env variables

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
JINA_API_KEY = os.getenv("JINA_API_KEY")

# GUARD MODEL

GUARD_MODEL_NAME = "openai/gpt-oss-safeguard-20b"


# TRACING

LANGSMITH_TRACING = os.getenv("LANGSMITH_TRACING","false")
LANGSMITH_ENDPOINT = os.getenv("LANGSMITH_ENDPOINT")
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")
LANGSMITH_PROJECT = os.getenv("LANGSMITH_PROJECT")



## Define Path - Data / Vector store
DATA_FILE_PATH = os.path.join("data","hr_policy.txt")

## Vector stores
VECTOR_STORE_PATH = os.path.join("data","faiss_index")


## Models
# LLM and Embeding Model

LLM_MODEL_NAME = "openai/gpt-oss-20b"

EMBEDDING_MODEL_NAME = "jina-embeddings-v2-base-en"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# Retrival Results
TOP_K_RESULTS = 3

## System  Instructions

SYSTEM_PROMPT = """
        You are a friendly HR assistant working for Acme Crop.
        Always use the search_hr_policy tool to look up
        facts before answering.If the answer isn't in the search results,say you don't know
        instead of guessing.
    """

def check_api_keys()->None:
    """Stop early with clear message if a requried API key is missing"""
    if not GROQ_API_KEY:
        raise ValueError("Missing GROQ_API_KEY in environment variables")
    if not JINA_API_KEY:
        raise ValueError("Missing JINA_API_KEY in environment variables")
