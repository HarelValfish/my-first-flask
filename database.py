# pulls in env vars, mongo driver, and the cert bundle for tls connections
import os
from dotenv import load_dotenv
from pymongo import MongoClient
import certifi

# loads .env so os.getenv picks up MONGO_URI and MONGO_DB
load_dotenv()

# ensures you don't open a new connection every time you want to talk to the database
_client = None
_db = None


# builds a mongo client, adding the system ca bundle only for atlas (srv) connections
def _build_client(mongo_uri: str) -> MongoClient:
    options = {"serverSelectionTimeoutMS": 2000}
    if mongo_uri.startswith("mongodb+srv://"):
        options["tlsCAFile"] = certifi.where()
    return MongoClient(mongo_uri, **options)

# connects to mongo, selects the right database, and stashes it on the flask app config
def init_db(app):
    global _client, _db
    mongo_connection_string = os.getenv("MONGO_URI", "mongodb://127.0.0.1:27017")
    db_name = os.getenv("MONGO_DB", "prod")
    _client = _build_client(mongo_connection_string)
    _db = _client[db_name]
    app.config["db"] = _db # make it accessible throughout the entire app without having to re-initialize it

# returns a collection by name, blowing up early if init_db was never called
def get_collection(name):
    if _db is None:
        raise RuntimeError("Database is not initialized. Call init_db(app) before using models.")
    return _db[name]