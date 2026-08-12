from langchain_community.embeddings import JinaEmbeddings
from hr_assistant import config
from hr_assistant.logger import get_logger

logger = get_logger(__name__)

def get_embeddings_model():
    """Return an instance of the JinaEmbeddings model using the API key from the config."""
    logger.info("Initializing embeddings model '%s'",config.EMBEDDING_MODEL_NAME)
    return JinaEmbeddings(
        model_name=config.EMBEDDING_MODEL_NAME,
        api_key=config.JINA_API_KEY,
    )