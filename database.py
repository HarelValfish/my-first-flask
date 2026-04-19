import os
from dotenv import load_dotenv
from pymongo import MongoClient
import certifi

load_dotenv()

_client = None
_db = None


def _build_client(mongo_uri: str) -> MongoClient:
    options = {"serverSelectionTimeoutMS": 2000}
    if mongo_uri.startswith("mongodb+srv://"):
        options["tlsCAFile"] = certifi.where()
    return MongoClient(mongo_uri, **options)

def init_db(app):
    global _client, _db
    mongo_connection_string = os.getenv("MONGO_URI", "mongodb://127.0.0.1:27017")
    db_name = os.getenv("MONGO_DB", "prod")
    _client = _build_client(mongo_connection_string)
    _db = _client[db_name]
    app.config["db"] = _db
        
def get_collection(name):
    if _db is None:
        raise RuntimeError("Database is not initialized. Call init_db(app) before using models.")
    return _db[name]