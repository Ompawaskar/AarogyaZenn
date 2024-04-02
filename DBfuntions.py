from DB import connection
from pymongo.errors import DuplicateKeyError, WriteError
# from DBSchema import *
import os



def add_user(user):
    try:
        db = connection()
        Users = db["Users@aarogyazen"]
        Users.insert_one(user)
        print("User added successfully!")
        
        
    except DuplicateKeyError as e:
        print("Duplicate key error occurred:", e)
    except WriteError as e:
        print("Schema validation failed:", e)
    except Exception as e:
        print("Error occurred while adding user:", e)



def add_info(user_information,username):
    
    db = connection()
    Users = db["Users@aarogyazen"]
# Updating the document with the provided username by pushing additional_info to it
    update_result = Users.update_one(
                {"username": username},
               {"$push": user_information}
          )

# Checking if the update was successful
    if update_result.modified_count > 0:
           print("Additional information added successfully!")
    else:
            print("Failed to add additional information.")


def info_data_check(user_information,username):
        db = connection()
        Users = db["Users@aarogyazen"]
        existing_document = Users.find_one({"username": username, 
                                         "information":  user_information["information"]})

    

        if existing_document:
            return "yes"
        else:
           return "no"
    # Proceed with updating the data object
        #    add_info(user_information,username)
        #    print("Data object updated successfully.")
           