from db_connection import connection
from datetime import datetime,timedelta
import pprint

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

# Example usage
username = "AtharvaYadav"
water_intake_last_7_days = get_water_intake_last_7_days(username)
print(water_intake_last_7_days)