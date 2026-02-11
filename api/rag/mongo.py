import os
import logging
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError

logger = logging.getLogger(__name__)

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DATABASE_NAME = "rag_sorveteria"
COLLECTION_NAME = "produtos"

_client = None
_db = None
_colecao_produtos = None


def get_mongo_client():
    global _client
    if _client is None:
        try:
            _client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
            _client.admin.command('ping')
            logger.info("Conexão MongoDB estabelecida")
        except (ConnectionFailure, ServerSelectionTimeoutError) as e:
            logger.error(f"Falha ao conectar ao MongoDB: {type(e).__name__}")
            raise
    return _client


def get_database():
    global _db
    if _db is None:
        _db = get_mongo_client()[DATABASE_NAME]
    return _db


def get_colecao_produtos():
    global _colecao_produtos
    if _colecao_produtos is None:
        _colecao_produtos = get_database()[COLLECTION_NAME]
    return _colecao_produtos


colecao_produtos = get_colecao_produtos()
