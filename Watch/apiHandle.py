import requests
import base64

# Replace these with your actual values
client_id = "23RS2V"
client_secret = "42ea0a7b62bc34f180562befe7f6284d"
authorization_code = "18de1e364b3b3ee3ddd52532c755a8971ab3c052"
redirect_uri = "http://127.0.0.1:8080/"
code_verifier = "QC5Uf3A7ZhdGn95gBMmPS3ADS-GU0ZCVnfJKO_Ia2xr3CwXYDtX_l3-lRA"

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

