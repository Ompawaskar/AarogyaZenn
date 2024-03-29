import requests
import base64

# Replace these with your actual values
client_id = "23RS2V"
client_secret = "42ea0a7b62bc34f180562befe7f6284d"
authorization_code = "50df245fa3e84a443f9c0237f610b3ece0f49d21"
redirect_uri = "http://127.0.0.1:8080/"
code_verifier = "6FfwJ9zspCl1v9y-x3miQSPCP-IdfzoBHAdh4bzKuC1W7hMZZQyEjUEKbw"

# Fitbit token endpoint URL
token_url = "https://api.fitbit.com/oauth2/token"

# Prepare data for the POST request
data = {
    "client_id": client_id,
    "code": authorization_code,
    "code_verifier": code_verifier,
    "grant_type": "authorization_code"
}

# If your application is a server type, include the Authorization header with Basic Authentication
credentials = f"{client_id}:{client_secret}"
headers = {
    "Authorization": f"Basic {base64.b64encode(credentials.encode()).decode()}",
    "Content-Type": "application/x-www-form-urlencoded"
}

# Make the POST request with headers
response = requests.post(token_url, data=data, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    token_data = response.json()

    # Extract the access token and refresh token
    access_token = token_data["access_token"]
    refresh_token = token_data["refresh_token"]

    # Print or use the tokens as needed
    print(f"Access Token: {access_token}")
    print(f"Refresh Token: {refresh_token}")

else:
    # Print an error message if the request was not successful
    print(f"Error: {response.status_code}, {response.text}")

