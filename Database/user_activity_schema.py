from db_connection import connection
from datetime import datetime
from datetime import datetime

date_string = "2024-03-29"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d")


activity_example = {
    "username" : "AtharvaYadav",
    "Cals_burned": 250.5,
    "water_drank": 8,
    "steps_walked": 10000,
    "hours_slept": 7.5,
    "date": parsed_date
}



schema_validation = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ['username'],
        "properties": {
            "username": {
                "bsonType": "string",
                "description": "must be an string and is required"
            },
            "Cals_burned": {
                "bsonType": "double",
                "description": "must be an double and is required"
            },
            "water_drank": {
                "bsonType": "int",
                "description": "must be a integer and is required"
            },
            "steps_walked": {
                "bsonType": "int",
                "description": "must be a integer and is required"
            },
            "hours_slept": {
                "bsonType": "double",
                "description": "must be a double and is required"
            },
            "date": {
                "bsonType": "date",
                "description": "must be a date and is required"
            }
        }
    }
     
}

def create_collection():
    try:
        db = connection()
        activity_collection = db.create_collection("user_activity", validator=schema_validation)
        activity_collection.insert_one(activity_example)
        print("Created Succesfully")

        
    except Exception as e:
        print("Error creating collection", e)

create_collection()







