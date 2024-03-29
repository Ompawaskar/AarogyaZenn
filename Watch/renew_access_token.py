import requests
import os
import base64
from dotenv import load_dotenv

load_dotenv()
# Define your client ID, client secret, and refresh token
client_id = os.getenv('FITBIT_CLIENT_ID')
client_secret = os.getenv('FITBIT_CLIENT_SECRET')
refresh_token = os.getenv('FITBIT_REFRESH_TOKEN')

# Make a request to the Fitbit token endpoint to refresh the token
response = requests.post(
    "https://api.fitbit.com/oauth2/token",
    headers={"Authorization": f"Basic {base64.b64encode(f'{client_id}:{client_secret}'.encode()).decode()}"},
    data={
        "grant_type": "refresh_token",
        "refresh_token": refresh_token
    }
)
# Check if the request was successful
if response.status_code == 200:
    # Extract the new access and refresh tokens from the response
    token_data = response.json()
    new_access_token = token_data['access_token']
    new_refresh_token = token_data['refresh_token']  # Optional, may or may not change
    print("Token refreshed successfully!")
    print(f"New Access Token: {new_access_token}")
    print(f"New Refresh Token: {new_refresh_token}")  # May or may not be provided
else:
    print(f"Error: {response.status_code} - {response.reason}")
