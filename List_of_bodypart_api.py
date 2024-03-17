import requests

def fetch_bodyParts():
    url = "https://exercisedb.p.rapidapi.com/exercises/bodyPartList"

    headers = {
        "X-RapidAPI-Key": "4ec29fefd8mshc338b3a4826109bp180805jsn659243609fc9",
        "X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        body_parts = response.json()
        return body_parts
    except requests.exceptions.RequestException as e:
        print("Error fetching body parts:", e)
        return []

# Example usage:
body_parts = fetch_bodyParts()

