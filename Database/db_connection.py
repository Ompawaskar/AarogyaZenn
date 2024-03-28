from pymongo import MongoClient
from dotenv import load_dotenv
import os

#Load the env variables
load_dotenv()

def connection():
    try:
        mongo_url = os.getenv("MONGODB_URI")
        client = MongoClient(mongo_url)
        db = client["AarogyaZen"]
        return db
    except:
        print("Error connecting to MongoDb!")
        return None
    
db = connection()
meals = db['meals']