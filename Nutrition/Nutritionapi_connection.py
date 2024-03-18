import requests

food = input("Enter the foodName: ")

url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
headers = {
    'Content-Type': 'application/json',
    'x-app-id': '9d3a1c5c',  
    'x-app-key': '56308225cee0ebc5063230f1749573f3'
}

data = {
    'query': f'{food}',
}

try:
    response = requests.post(url, headers=headers, json=data)
except Exception as e:
    print("Error fetching data",e)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: Unable to fetch data. Status code {response.status_code}")
    print(response.text)  


