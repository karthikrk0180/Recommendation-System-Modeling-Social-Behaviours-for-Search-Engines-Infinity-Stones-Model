import json
import random

# assign group weights based on functionality of devices
GROUP_WEIGHTS = {
    'CameraLens': 0.2,
    'Laptop': 0.9,
    'LaptopPeriferals': 0.3,
    'Mobile': 0.8,
    'Refrigerator': 0.5,
    'Tablet': 0.7,
    'TV': 0.6,
    'WashingMachine': 0.5,
    'WearableSmartDevice': 0.4
}


def load_json(json_files): # function to load the json files data
    group_data = {}
    for files in json_files:
        try:
            with open(files, 'r') as json_file:
                group_name = files.split('.')[0]
                group_data[group_name] = json.load(json_file)
        except FileNotFoundError:
            print(f"files not found")
    return group_data


def recommend_items(group_data, search_group):  # Function to recommend items based on weights
    recommended_items = []
    search_power = GROUP_WEIGHTS.get(search_group, 0)
    
    for group, data in group_data.items():
        group_power = GROUP_WEIGHTS.get(group, 0)
        if group_power < search_power or group == search_group: #condition to check current group weight less than search group weight if same too
            recommended_item = random.choice(data)
            recommended_items.append((group, recommended_item))
    
    return recommended_items


def main():
    json_files = [
        'CameraLens.json',
        'Laptop.json',
        'LaptopPeriferals.json',
        'Mobile.json',
        'Refrigerator.json',
        'Tablet.json',
        'TV.json',
        'WashingMachine.json',
        'WearableSmartDevice.json'
    ]
    
    group_data = load_json(json_files)
    
    search_group = input("What do you want to buy....? ")
    
    if search_group in group_data:
        recommended_items = recommend_items(group_data, search_group)
        print("\nCustomers who also bought this:")
        for i, (group, item) in enumerate(recommended_items, start=1):
            print(f"\nRecommendation {i} from {group}: {item}")
            for key, value in item.items():
                print(f"{key}: {value}")
            print()
    else:
        print("Invalid group")

main()
