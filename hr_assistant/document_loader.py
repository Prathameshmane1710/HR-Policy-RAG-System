from langchain_community.document_loaders import TextLoader
from hr_assistant import config
from hr_assistant.logger import get_logger

logger = get_logger(__name__)

def load_documents(file_path:str = config.DATA_FILE_PATH):
    """Load documents from a text file and return them as a list of Document objects."""

    logger.info("LOADING DOCUMENTS from document loader",file_path)
    loader = TextLoader(file_path,encoding="utf-8")
    documents = loader.load()
    logger.info("Loaded %d document(s)", len(documents))
    return documents




