import json
import requests

data_file = 'examples/reciepe-bot/data.json'

def give_feedback(dish_name:str, cuisine_type:str, feedback:bool):
    with open(data_file, 'r') as f:
        data = json.load(f)
    data.append({
        "dish_name":dish_name,
        "cuisine_type":cuisine_type,
        "feedback":feedback
    })
    with open(data_file, 'w') as f:
        json.dump(data, f, indent=4)

def get_feedback():
    with open(data_file, 'r') as f:
        data = json.load(f)
    return data

def get_calories(query:str):

    print("Query:", query)
    api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
    response = requests.get(api_url + query, headers={'X-Api-Key': 'xpgDcBFYnegMHckgUYUxFA==LtKi4Vk2NvxNDeWT'})
    if response.status_code == requests.codes.ok:
        print(response.text)
        data = response.json()
        prettified_data = ""
        total_calories = 0
        total_protein = 0
        total_fat = 0

        for item in data['items']:
            prettified_data += f"{item['name']} has {item['calories']} calories, {item['fat_total_g']}g fat and {item['protein_g']}g protein\n\n"
            total_fat += int(item['fat_total_g'])
            total_protein += int(item['protein_g'])
            total_calories += int(item['calories'])

        prettified_data += f"Total calories: {total_calories}\n\nTotal fat: {total_fat}g\n\nTotal protein: {total_protein}g"
        return prettified_data
    else:
        print("Error:", response.status_code, response.text)

        return "Umm, can't find calories details for this dish. :("