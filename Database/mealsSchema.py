from db_connection import connection
from datetime import datetime
from meals_functions import add_meal

meal_example = {
    "Total_Calories": 500.0,
    "protein": 25.0,
    "fats": 20.0,
    "sugar": 10.0,
    "carbohydrates": 60.0,
    "username": "AtharvaYadav",
    "meal_type": "breakfast",
    "date": datetime.now()  # Assuming current date and time
}

schema_validation = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["Total_Calories", "protein", "fats", "sugar", "carbohydrates", "username", "meal_type", "date"],
        "properties": {
            "Total_Calories": {
                "bsonType": "double",
                "description": "must be an double and is required"
            },
            "protein": {
                "bsonType": "double",
                "description": "must be a double and is required"
            },
            "fats": {
                "bsonType": "double",
                "description": "must be a double and is required"
            },
            "sugar": {
                "bsonType": "double",
                "description": "must be a double and is required"
            },
            "carbohydrates": {
                "bsonType": "double",
                "description": "must be a double and is required"
            },
            "username": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "meal_type": {
                "bsonType": "string",
                "description": "must be a string and is required"
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
        meals_collection = db.create_collection("meals", validator=schema_validation)
        
    except Exception as e:
        print("Error creating collection", e)

#create_collection()
        
#Example user
add_meal(meal_example)





