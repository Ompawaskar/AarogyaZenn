import pymongo
from DB import connection
import DBfuntions


schema_validation = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["username", "password", "email", "date"],
        "properties": {
            "username": {"bsonType": "string", "description": "Username is required"},
            "hashed_password": {"bsonType": "string", "description": "Password is required"},
            "salt": {"bsonType": "string", "description": "Salt is required"},
            "email": {"bsonType": "string", "description": "Email is required", "required": True},
            "phone_no": {"bsonType": "string", "description": "Phone number is required"},
            "information": {
                "bsonType": "object",
                "properties": {
                    "user_info": {
                        "bsonType": "object",
                        "properties": {
                            "name": {"bsonType": "string", "description": "Name is required"},
                            "gender": {"bsonType": "string", "description": "Gender is required"},
                            "age": {"bsonType": "double", "description": "Age is required"},
                            "activeStatus": {"bsonType": "string", "description": "Active status is required"},
                            "height": {"bsonType": "double", "description": "Height is required"},
                            "weight": {"bsonType": "double", "description": "Weight is required"},
                            "tar_weight": {"bsonType": "double", "description": "Target weight is required"},
                            "target": {"bsonType": "string", "description": "Target is required"},
                            "medicalConditions": {"bsonType": "string", "description": "Medical conditions are required"}
                        }
                    }
                }
            },
            "date": {"bsonType": "date", "description": "Date is required"}
        }
    }
}

def create_collection():
    try:
        db = connection()
        Users = db.create_collection("Users@aarogyazen", validator=schema_validation)
        print("Collection 'Users' created successfully!")
        print("Validator:", Users.validator)
    except pymongo.errors.CollectionInvalid as e:
        print("Collection validation failed:", e)
    except Exception as e:
        print("Error creating collection:", e)