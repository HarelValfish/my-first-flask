from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()
mongo_connection_string = os.getenv("MONGO_URI")
client = MongoClient(mongo_connection_string)
db = client['prod']
todos_coll = db['data']