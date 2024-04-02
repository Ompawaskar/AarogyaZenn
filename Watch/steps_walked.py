import requests
from datetime import datetime
import os
from dotenv import load_dotenv
from Database.user_activity_functions import update_calories_burned,update_steps_walked
from datetime import datetime
import pprint

date_string = "2024-03-29"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d")

def get_user_activity(date):
    load_dotenv()

    # Your access token
    ACCESS_TOKEN = os.getenv('FITBIT_ACCESS_TOKEN')

    # Date for which you want to retrieve activity data (in YYYY-MM-DD format)
    date = '2024-02-27'

    # Fitbit API endpoint to retrieve activity data
    url = f"https://api.fitbit.com/1/user/-/activities/date/{date}.json"

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
            update_steps_walked("AtharvaYadav",parsed_date,steps_walked)
            update_calories_burned("AtharvaYadav",parsed_date,calories_burned)
            # print(f"Steps walked on {date}: {steps_walked}")
            return {"steps":steps_walked,
                    "cals":calories_burned}
            
        else:
            print(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"Error: {str(e)}")
