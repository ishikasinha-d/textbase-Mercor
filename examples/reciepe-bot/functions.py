import json

def give_feedback(dish_name:str, cuisine_type:str, feedback:bool):
    with open('data.json', 'r') as f:
        data = json.load(f)
    data.append({
        "dish_name":dish_name,
        "cuisine_type":cuisine_type,
        "feedback":feedback
    })
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)

def get_feedback():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return data