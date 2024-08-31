import json
import random

def load_json(json_files):
    group_data = {}  #create a dictionary to store json files data

    for files in json_files:
        try:
            with open(files, 'r') as json_file:
                group_name = files.split('.')[0]  
                data = json.load(json_file) #stores all the json files data in variable data
                group_data[group_name] = data
        except FileNotFoundError:
            print("{} files not found.".format(files))

    return group_data

def recommend_items(group_data, selected_group, num_recommendations=5):
    recommended_items = []
    while len(recommended_items) < num_recommendations:
        recommended_group = random.choice(list(group_data.keys()))
        if recommended_group != selected_group:  # Selected group is not same as recomended group adhering to logic
            recommended_item = random.choice(group_data[recommended_group])
            recommended_items.append((recommended_group, recommended_item))
    return recommended_items

def main():
    json_files = ['CameraLens.json',
                  'Laptop.json',
                  'LaptopPeriferals.json',
                  'Mobile.json',
                  'Refrigerator.json',
                  'Tablet.json',
                  'TV.json',
                  'WashingMachine.json',
                  'WearableSmartDevice.json']
    
    group_data = load_json(json_files)  #Call the json loading function
    
    selected_group = input("What do you want to buy....? ")  
    
    if selected_group in group_data:  # Change variable name to group_data
        recommended_items = recommend_items(group_data, selected_group) #call the recommedning function
        print("\nCustomers who also bought this:")
        for i, (category, item) in enumerate(recommended_items, start=1):
            print(f"\nRecommendation {i} from {category}:")
            for key, value in item.items():
                print(f"{key}: {value}")
            print()
    else:
        print("Invalid category")

main()
