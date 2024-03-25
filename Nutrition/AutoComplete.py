import requests

url = 'https://trackapi.nutritionix.com/v2/search/instant'
headers = {
    'Content-Type': 'application/json',
    'x-app-id': '9d3a1c5c',  
    'x-app-key': '56308225cee0ebc5063230f1749573f3'
}

data = {
    'query': 'hamburger',
}

def autocompleteValues(values_dict):
    values_array = values_dict['common']
    values = []
    for value in values_array:
        food_name = value['food_name']
        values.append(food_name)
    return values

try:
    response = requests.post(url, headers=headers, json = data)
except Exception as e:
    print("Error fetching data",e)

if response.status_code == 200:
    values_dict  = response.json()
    values2 = autocompleteValues(values_dict)
else:
    print(f"Error: Unable to fetch data. Status code {response.status_code}")
    print(response.text)  


