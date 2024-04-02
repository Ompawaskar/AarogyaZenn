from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from pymongo import MongoClient
from Nutrition.Nutritionapi_connection import nutritional_info

connection_string ='mongodb+srv://ompawaskar:ruchita@cluster0.lsshopg.mongodb.net/'
client = MongoClient(connection_string, tlsAllowInvalidCertificates=True)
db = client["AarogyaZen"]
Users = db["Users@aarogyazen"]

app = Flask(__name__)

# Global variable to store session state
session_state = {}

# Function to send a message
def send_message(message):
    resp = MessagingResponse()
    resp.message(message)
    return str(resp)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming SMS messages."""
    global session_state

    # Fetch the incoming message
    incoming_message = request.form.get('Body')

    # Determine current state of the conversation
    if 'state' not in session_state:
        session_state['state'] = 'START'

    state = session_state['state']

    if state == 'START':
        if incoming_message.lower() == "hello aarogyazen":
            response = "Welcome to AarogyaZen!\nPlease provide your username."
            # Update session state
            session_state['state'] = 'WAITING_USERNAME'
        else:
            response = "Invalid command. Please start by sending 'Hello AarogyaZen'."

    elif state == 'WAITING_USERNAME':
        username = incoming_message
        if username_exists(username):
            response = f"Hello, {username}!\nPlease choose a meal category:\n1. Breakfast\n2. Lunch\n3. Evening Snacks\n4. Dinner"
            # Update session state
            session_state['username'] = username
            session_state['state'] = 'WAITING_MEAL_CATEGORY'
        else:
            response = "Username invalid. Please try again."

    elif state == 'WAITING_MEAL_CATEGORY':
        meal_category_choice = incoming_message
        if meal_category_choice.isdigit() and 1 <= int(meal_category_choice) <= 4:
            meal_category = get_meal_category(int(meal_category_choice))
            response = "Please enter the name of the dish:"
            # Update session state
            session_state['meal_category'] = meal_category
            session_state['state'] = 'WAITING_DISH_NAME'
        else:
            response = "Invalid meal category choice. Please choose a valid option."

    elif state == 'WAITING_DISH_NAME':
        dish_name = incoming_message

        username = session_state['username']
        meal_category = session_state['meal_category']
        calorie_count = nutritional_info(dish_name)
        print(calorie_count)
        # Store user input (username, meal catecalorie_count = gory, dish name) in MongoDB or array
        store_user_input(username, meal_category, dish_name)
        response = "Thank you for providing the information. Your dish has been added!"
        # Reset session state
        session_state.clear()

    return send_message(response)

# Dummy functions for demo purposes
# Dummy function to simulate checking if username exists
def username_exists(username):
    # Replace this with actual database query to check if username exists
    # For example, if you're using MongoDB with PyMongo:
    # result = db.users.find_one({"username": username})
    # return result is not None
    result = Users.find_one({"username": username})
    return result is not None
   

# Dummy function to simulate getting meal category
def get_meal_category(choice):
    # Replace this with actual implementation to get meal category based on choice
    return {
        1: "Breakfast",
        2: "Lunch",
        3: "Evening Snacks",
        4: "Dinner"
    }.get(choice)

# Dummy function to simulate storing user input
def store_user_input(username, meal_category, dish_name):
    # Replace this with actual implementation to store user input in your database
    # For example, if you're using MongoDB with PyMongo:
    # db.meals.insert_one({"username": username, "meal_category": meal_category, "dish_name": dish_name})
    print("Storing:", username, meal_category, dish_name)

if __name__ == "__main__":
    app.run(debug=True)
