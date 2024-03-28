from Database.db_connection import connection

def add_meal(meal):
       try:
         db = connection()
         meals_collection = db["meals"]
         meals_collection.insert_one(meal)
         print("Meal added succesfully!")
       except Exception as e:
            print("Error occured while adding meal" , e)

def delete_meal(username, meal_date, meal_type):
  
       try:
         db = connection()
         meals_collection = db["meals"]
         result = meals_collection.delete_one({"username": username, "date": meal_date, "meal_type": meal_type})
         if result.deleted_count == 1:
            print("Meal deleted successfully!")
         else:
            print("Meal not found for deletion.")
       except:
            print("Error occured while deleting meal")

def show_meals(username,meal_date,meal_type):
     try:
         db = connection()
         meals_collection = db["meals"]
         cursor = meals_collection.find({"username": username,
                                         "date":meal_date,
                                         "meal_type":meal_type})
         
     except Exception as e:
            print("Error occured while adding meal" , e)
    