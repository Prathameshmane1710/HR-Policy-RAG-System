from langchain_community.embeddings import JinaEmbeddings
from hr_assistant import config

def get_embeddings_model():
    """Return an instance of the JinaEmbeddings model using the API key from the config."""

    return JinaEmbeddings(
        model_name=config.EMBEDDING_MODEL_NAME,
        api_key=config.JINA_API_KEY,
    )