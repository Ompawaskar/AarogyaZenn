from Database.db_connection import connection
from datetime import datetime,timedelta

def create_activity(username,date):
     try:
         db = connection()
         activity_collection = db["user_activity"]
         user_document = activity_collection.find_one({'username':username,
                                       'date':date})
         print(user_document)
         if user_document:
              pass
         else:
              activity_collection.insert_one({
                        "username" : username,
                        "Cals_burned": 0.0,
                        "water_drank": 0,
                        "steps_walked": 0,
                        "hours_slept": 0.0,
                        "date": date
                        })
              print("Created Succesfully!")
     except Exception as e:
            print("Error occured while getting water consumed" , e)

class UserActivity:
    def __init__(self, username, date):
        try:
            self.db = connection()
            self.activity_collection = self.db["user_activity"]
            self.activity_document = self.activity_collection.find_one(
                {'username': username, 'date': date})
        except Exception as e:
            print("Error getting activity collection", e)

    def get_attribute(self, attribute_name):
        try:
            return self.activity_document[attribute_name]
        except KeyError as e:
            print(f"Error: Attribute '{attribute_name}' not found", e)

    def update_attribute(self, username, date, attribute_name, value):
        try:
            self.activity_collection.update_one(
                {'username': username, 'date': date},
                {"$set": {attribute_name: value}})
        except Exception as e:
            print(f"Error occurred while updating '{attribute_name}'", e)

     

          
           
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

def get_water_intake_last_7_days(username):
    try:
        db = connection()
        user_activity_collection = db["user_activity"]
        
        # Calculate the date 7 days ago
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        seven_days_ago = today - timedelta(days=6)
        
        # Initialize a list with 7 elements initialized to 0
        water_intake = [0] * 7
        
        # Query documents for the past 7 days
        cursor = user_activity_collection.find({
            "username": username,
            "date": {"$gte": seven_days_ago, "$lte": today}
        })

        # Update water intake values from documents
        for document in cursor:
            # Calculate the index corresponding to the document's date
            index = (document['date'] - seven_days_ago).days
            water_intake[index] = document.get('water_drank', 0)  # Get water_drank or default to 0 if not present
        
        return water_intake
    except Exception as e:
        print("Error occurred while fetching water intake:", e)


