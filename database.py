from dotenv import load_dotenv
from pymongo import MongoClient
import os
import certifi

load_dotenv()
mongo_connection_string = os.getenv("MONGO_URI")
cr = certifi.where()
client = MongoClient(mongo_connection_string, tlsCAFile=cr, serverSelectionTimeoutMS=2000)
db = client['prod'] 
todos_coll = db['todo']