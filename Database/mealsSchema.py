from db_connection import connection
from datetime import datetime
from meals_functions import add_meal
from datetime import datetime

date_string = "2024-03-29"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d")


meal_example = {
    "Total_Calories": 500.25,
    "protein": 25.75,
    "fats": 20.5,
    "fiber": 8.3,
    "carbohydrates": 60.2,
    "username": "john_doe",
    "meal_type": "lunch",
    "meal_name": "Chicken Salad",
    "units": "grams",
    "quantity": 300.0,  
    "date": parsed_date
}


schema_validation = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["Total_Calories", "protein", "fats", "fiber", "carbohydrates", "username", "meal_type", "meal_name", "units", "quantity", "date"],
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
            "fiber": {
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
            "meal_name": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "units": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "quantity": {
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
        meals_collection = db.create_collection("meals", validator=schema_validation)
        
    except Exception as e:
        print("Error creating collection", e)

# create_collection()
        
#Example user
# add_meal(meal_example)





