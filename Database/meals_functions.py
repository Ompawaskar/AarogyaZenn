from Database.db_connection import connection
from datetime import datetime
import pprint

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
            print("Error occured while showing meal" , e)

def get_nutrition_consumed(username,date):
     try:
         db = connection()
         meals_collection = db["meals"]
         today_meals = meals_collection.find({'username': username,'date':date})
         total_calories = 0
         total_protein = 0
         total_fats = 0
         total_carbs = 0
         total_fiber = 0
         for meal in today_meals:
              total_calories += meal['Total_Calories']
              total_protein += meal['protein']
              total_fats += meal['fats']
              total_carbs+= meal['carbohydrates']
              total_fiber += meal['fiber']
          
         return {
            'Total_Calories': round(total_calories),
            'Total_Protein': round(total_protein),
            'Total_Fats': round(total_fats),
            'Total_Carbohydrates': round(total_carbs),
            'Total_Fiber': round(total_fiber)
        }
              
              
            
     except Exception as e:
            print("Error occured while getting meal" , e)

def get_total_calories(username):
     try:
         db = connection()
         user_collection = db["Users@aarogyazen"]
         user = user_collection.find_one({'username':username})
         total_cals = user['information'][0]['daily_calories']
         print(total_cals)
         return total_cals
     
     except Exception as e:
            print("Error occured while getting total calories" , e) 

