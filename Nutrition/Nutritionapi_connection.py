import requests
import sys
sys.path.append('..') 
from globalStore import user_meal


def nutritional_info(food):
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
        res = response.json()
        protien = res['foods'][0]["nf_protein"]
        carbs = res['foods'][0]["nf_total_carbohydrate"]
        fats = res['foods'][0]["nf_total_fat"]
        fiber = res['foods'][0]["nf_dietary_fiber"]
        user_meal['protein'] = protien
        user_meal['carbs'] = carbs
        user_meal['fats'] = fats
        user_meal['fiber'] = fiber
        

        # units = res['foods'][0]["alt_measures"]
        # user_meal['units'] = units
        # print(units)

        return res
        
    else:
        print(f"Error: Unable to fetch data. Status code {response.status_code}")
        print(response.text)  
