import requests

def fetch_exercises():
    url = "https://exercisedb.p.rapidapi.com/exercises"
    querystring = {"limit":"1324"}
    headers = {
        "X-RapidAPI-Key": "4ec29fefd8mshc338b3a4826109bp180805jsn659243609fc9",
        "X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()


