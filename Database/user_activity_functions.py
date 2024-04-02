from Database.db_connection import connection
from datetime import datetime
import pprint

date_string = "2024-03-29"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d")

def get_water_consumed(username,date):
     try:
         db = connection()
         activity_collection = db["user_activity"]
         water_consumed_document = activity_collection.find_one({'username':username,
                                       'date':date})
         return water_consumed_document['water_drank']
     except Exception as e:
            print("Error occured while getting water consumed" , e) 

def update_water_consumed(username,date,water_consumed):
    try:
         db = connection()
         activity_collection = db["user_activity"]
         activity_collection.update_one(
               {'username':username,'date':date},
               {"$set": {'water_drank': water_consumed}})
    except Exception as e:
            print("Error occured while updating water consumed" , e)

def get_calories_burned(username,date):
    try:
         db = connection()
         activity_collection = db["user_activity"]
         calories_burned_document = activity_collection.find_one({'username':username,
                                       'date':date})
         return calories_burned_document['Cals_burned']
    except Exception as e:
            print("Error occured while getting calories" , e)  

def update_calories_burned(username,date,Cals_burned):
      try:
         db = connection()
         activity_collection = db["user_activity"]
         activity_collection.update_one(
               {'username':username,'date':date},
               {"$set": {'Cals_burned': Cals_burned}})
      except Exception as e:
            print("Error occured while updating cals" , e)

def get_steps_walked(username,date):
      try:
         db = connection()
         activity_collection = db["user_activity"]
         steps_walked_document = activity_collection.find_one({'username':username,
                                       'date':date})
         return steps_walked_document['steps_walked']
      except Exception as e:
            print("Error occured while getting steps" , e)

def update_steps_walked(username,date,steps_walked):
     try:
         db = connection()
         activity_collection = db["user_activity"]
         activity_collection.update_one(
               {'username':username,'date':date},
               {"$set": {'steps_walked': steps_walked}})
     except Exception as e:
            print("Error occured while updating steps" , e)
      
def get_hours_slept(username,date):
      try:
         db = connection()
         activity_collection = db["user_activity"]
         hours_slept_document = activity_collection.find_one({'username':username,
                                       'date':date})
         return hours_slept_document['hours_slept']
      except Exception as e:
            print("Error occured while getting hours sleep" , e)

def update_sleep_hours(username,date,hours_sleep):
     try:
         db = connection()
         activity_collection = db["user_activity"]
         activity_collection.update_one(
               {'username':username,'date':date},
               {"$set": {'hours_slept': hours_sleep}})
     except Exception as e:
            print("Error occured while updating hours sleep" , e)

# update_water_consumed("AtharvaYadav",parsed_date,7) 
