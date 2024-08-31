import json
import random

def load_json(json_files):
    group_data = {}
    
   
    for file_name in json_files:
        try:
            with open(file_name, 'r') as json_file:
                group_name = file_name.split('.')[0]
                data = json.load(json_file) #stores all the json files data in variable data
                group_data[group_name] = data
        except FileNotFoundError:
             print("{} not found.".format(file_name))
    
    return group_data

def recommend_items_within_same_group(group_data, selected_group, num_recommendations=3):
    recommended_items = []
    
    if selected_group in group_data:
        data = group_data[selected_group]
        
        
        if data:
            recommended_items = random.sample(data, num_recommendations)
            recommended_items = [(selected_group, item) for item in recommended_items] #select the items from same group
    
    return recommended_items

def main():
    json_files = ['CameraLens.json', 'Laptop.json', 'LaptopPeriferals.json',
                  'Mobile.json', 'Refrigerator.json', 'Tablet.json', 
                  'TV.json', 'WashingMachine.json', 'WearableSmartDevice.json']
    
    group_data = load_json(json_files)
    
    selected_group = input("What do you want to buy....? ")
    
    recommended_items = recommend_items_within_same_group(group_data, selected_group, num_recommendations=3) #call the recomedning function
    
    if recommended_items:
        print(f"\n\nCustomers who also bought this from {selected_group} group:")
        for i, (group, item) in enumerate(recommended_items, start=1):
            print(f"Recommendation {i} from {group}:")
            for key, value in item.items():
                print(f"{key}: {value}")
            print()
    else:
        print(f"No items found in the {selected_group} group for recommendation.")

main()
