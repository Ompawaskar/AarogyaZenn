from db_connection import connection

try:
    db = connection()
    users_collection = db['Users']
    userInfo = users_collection.information.user_info
    print(type(users_collection))
except Exception as e:
    print("Error connecting:",e)

def calculate_daily_calories(user):
    # Extract user information from the dictionary
    weight = user.get("weight")
    height = user.get("height")
    gender = user.get("gender")
    activity_level = user.get("activity_level")
    age = user.get("age")

    # Define Harris-Benedict constants based on gender
    if gender.lower() == 'male':
        bmr_constant = 88.362
        height_constant = 4.799
        weight_constant = 13.397
        age_constant = 5.677
    elif gender.lower() == 'female':
        bmr_constant = 447.593
        height_constant = 3.098
        weight_constant = 9.247
        age_constant = 4.330
    else:
        raise ValueError("Invalid gender. Must be 'male' or 'female'.")

    # Calculate Basal Metabolic Rate (BMR)
    bmr = bmr_constant + (weight_constant * weight) + (height_constant * height) - (age_constant * age)

    # Adjust BMR based on activity level
    if activity_level.lower() == 'sedentary':
        calories = bmr * 1.2
    elif activity_level.lower() == 'lightly active':
        calories = bmr * 1.375
    elif activity_level.lower() == 'moderately active':
        calories = bmr * 1.55
    elif activity_level.lower() == 'very active':
        calories = bmr * 1.725
    elif activity_level.lower() == 'extra active':
        calories = bmr * 1.9
    else:
        raise ValueError("Invalid activity level. Must be 'sedentary', 'lightly active', 'moderately active', 'very active', or 'extra active'.")

    return calories

def calculate_minimum_calories_burned(user):


    # Extract user information from the dictionary
    weight = user.get("weight")
    height = user.get("height")
    gender = user.get("gender")
    activity_level = user.get("activity_level")
    age = user.get("age")

    if gender.lower() == 'male':
        bmr_constant = 88.362
        height_constant = 4.799
        weight_constant = 13.397
        age_constant = 5.677
    elif gender.lower() == 'female':
        bmr_constant = 447.593
        height_constant = 3.098
        weight_constant = 9.247
        age_constant = 4.330
    else:
        raise ValueError("Invalid gender. Must be 'male' or 'female'.")

    bmr = bmr_constant + (weight_constant * weight) + (height_constant * height) - (age_constant * age)

    if activity_level.lower() == 'sedentary':
        activity_factor = 1.2
    elif activity_level.lower() == 'lightly active':
        activity_factor = 1.375
    elif activity_level.lower() == 'moderately active':
        activity_factor = 1.55
    elif activity_level.lower() == 'very active':
        activity_factor = 1.725
    elif activity_level.lower() == 'extra active':
        activity_factor = 1.9
    else:
        raise ValueError("Invalid activity level. Must be 'sedentary', 'lightly active', 'moderately active', 'very active', or 'extra active'.")

    tdee = bmr * activity_factor

    return tdee

user_info = {
    "weight": 60,
    "height": 180,
    "gender": "male",
    "activity_level":'moderately active' ,
    "age" : 20
}

print(calculate_minimum_calories_burned(user_info))
print(calculate_daily_calories(user_info))


