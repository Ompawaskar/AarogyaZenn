from pymongo import MongoClient
from dotenv import load_dotenv
import os
from pprint import pprint
from marshmallow import Schema, fields, validate, ValidationError

# Load environment variables from .env
load_dotenv()

try:
    mongo_uri = os.getenv("MONGODB_URI")
    client = MongoClient(mongo_uri)

    db = client["AarogyaZen"]
    user_collection = db["user"]

    user_schema = {
        "username": {"type": "string", "required": True},
        "password": {"type": "string", "required": True},
        "height": {"type": "float", "required": True},
        "weight": {"type": "float", "required": True},
        "gender": {"type": "string", "required": True},
        "activity": {"type": "string", "required": True},
        "target_weight": {"type": "float", "required": True},
        "pace": {"type": "string", "required": True},
        "medical_condn": {"type": "string", "required": True},
        "phone_no": {"type": "string", "required": True}
    }

    sample_user = {
        "username": "Yuvraj",
        "password": "secure_password",
        "height": 175.5,
        "weight": 70.2,
        "gender": "male",
        "activity": "active",
        "target_weight": 65.0,
        "pace": "moderate",
        "medical_condn": "No known conditions",
        "phone_no": "+1234567890"
    }

    user_collection.insert_one(sample_user)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the MongoDB connection in the 'finally' block to ensure it's closed regardless of success or failure
    if 'client' in locals():
        client.close()
