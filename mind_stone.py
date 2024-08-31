import json
import random

def load_json(json_files): #load data from json files and store in data variable
    group_data = {}
    
    for files in json_files:
        try:
            with open(files, 'r') as json_file:
                group_name = files.split('.')[0]
                data = json.load(json_file)
                group_data[group_name] = data
        except FileNotFoundError:
             print("{} files not found.".format(files))
    
    return group_data

def recommend_random_items(group_data, num_recommendations=3):
    recommended_items = []
    
    for _ in range(num_recommendations):
        selected_group = random.choice(list(group_data.keys())) #select random category 
        
        if selected_group in group_data:
            data = group_data[selected_group]
            
            if data:
                recommended_item = random.choice(data)
                recommended_items.append((selected_group, recommended_item))
    
    return recommended_items

def main():
    json_files = ['CameraLens.json', 'Laptop.json', 'LaptopPeriferals.json',
                  'Mobile.json', 'Refrigerator.json', 'Tablet.json', 
                  'TV.json', 'WashingMachine.json', 'WearableSmartDevice.json']
    
    group_data = load_json(json_files)
    
    
    
    # Ask the user for input on whether they want to buy a product
    user_input = input("Wanna shop today..?(yes/no): ")
    
    if user_input.lower() == "yes":
        recommended_items = recommend_random_items(group_data, num_recommendations=3) #call the recemmendation function
        
        if recommended_items:
            print(f"\nCheckout these new items:")
            for i, (group, item) in enumerate(recommended_items, start=1):
                print(f"Recommendation {i} from {group}:")
                for key, value in item.items():
                    print(f"{key}: {value}")
                print()
        else:
            print("No items found for recommendation.")
    else:
        print("Hope you earn more money for shopping. Have a nice day!")

main()
