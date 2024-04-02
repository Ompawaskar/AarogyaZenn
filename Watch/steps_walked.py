import requests
from datetime import datetime
import os
from dotenv import load_dotenv
from Database.user_activity_functions import update_calories_burned,update_steps_walked
from datetime import datetime
import pprint

date_string = "2024-03-29"
# Get today's date
today_date = datetime.today()

# Format today's date as a string in "YYYY-MM-DD" format
today_date_string = today_date.strftime("%Y-%m-%d")

def get_user_activity(date,user):
    load_dotenv()
    # print(f"Date:{date}")

    # Your access token
    ACCESS_TOKEN = os.getenv('FITBIT_ACCESS_TOKEN')

    # Date for which you want to retrieve activity data (in YYYY-MM-DD format)

    # Fitbit API endpoint to retrieve activity data
    url = f"https://api.fitbit.com/1/user/-/activities/date/{today_date_string}.json"

    # Header containing the authorization token
    headers = {
        'Authorization': 'Bearer ' + ACCESS_TOKEN
    }

    try:
        # Making the GET request to the Fitbit API
        response = requests.get(url, headers=headers)

        # Checking if the request was successful (status code 200)
        if response.status_code == 200:
            # Parsing the JSON response
            steps_data = response.json()
            # print(steps_data)
            # Extracting the total calories burned for the specified date
            steps_walked = steps_data['summary']['steps']
            calories_burned = float(steps_data['summary']['caloriesOut'])
            # update_steps_walked("AtharvaYadav",today_date_string,steps_walked)
            # update_calories_burned("AtharvaYadav",today_date_string,calories_burned)
            # print(f"Steps walked on {date}: {steps_walked}")
            return {"steps":steps_walked,
                    "cals":calories_burned}
            
        else:
            print(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"Error: {str(e)}")

# get_user_activity(parsed_date)