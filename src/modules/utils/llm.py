""""
This module is responsible for creating the LLM models based on the config file. 
It is used by other modules by holding all LLM models in a single place.

"""
from config import settings
from langchain_openai import ChatOpenAI, OpenAIEmbeddings


CHAT_MODEL_TO_USE = settings.CHAT_MODEL_CONFIG
EMBEDDING_MODEL_TO_USE = settings.EMBEDDING_MODEL_CONFIG


# Set the LLM model to use
if CHAT_MODEL_TO_USE["type"] == "openai":
    ChatLLM = ChatOpenAI(**CHAT_MODEL_TO_USE["kwargs"])
else:
    raise ValueError(f"Model type {CHAT_MODEL_TO_USE['type']} not supported")


# Set the embedding model to use
if EMBEDDING_MODEL_TO_USE["type"] == "openai":
    EmbeddingLLM = OpenAIEmbeddings(**EMBEDDING_MODEL_TO_USE["kwargs"])
else:
    raise ValueError(f"Model type {EMBEDDING_MODEL_TO_USE['type']} not supported")

