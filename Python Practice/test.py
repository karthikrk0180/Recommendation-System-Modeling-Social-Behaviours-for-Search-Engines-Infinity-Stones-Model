import json
import random

def process_json_files(json_files):
    category_data = {}
    
    # Load data from JSON files and store it in the category_data dictionary
    for file_name in json_files:
        try:
            with open(file_name, 'r') as json_file:
                category_name = file_name.split('.')[0]
                data = json.load(json_file)
                category_data[category_name] = data
        except FileNotFoundError:
             print("{} not found.".format(file_name))
    
    return category_data

def recommend_items_space(category_data, search_category, num_recommendations=5):
    recommended_items = []
    while len(recommended_items) < num_recommendations:
        recommended_category = random.choice(list(category_data.keys()))
        if recommended_category != search_category:
            recommended_item = random.choice(category_data[recommended_category])
            recommended_items.append((recommended_category, recommended_item))
    return recommended_items

def recommend_items_power(category_data, search_category):
    recommended_items = []
    
    # Define a weight for each category based on its "power"
    category_weights = {
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
    
    # Determine the power of the search category
    search_category_power = category_weights.get(search_category, 0)
    
    # Recommend items from categories with lower power levels
    for category, data in category_data.items():
        category_power = category_weights.get(category, 0)
        if category_power < search_category_power:
            recommended_item = random.choice(data)
            recommended_items.append((category, recommended_item))
    
    # If the search category is the weakest, recommend an item from itself
    if search_category_power == min(category_weights.values()):
        recommended_item = random.choice(category_data[search_category])
        recommended_items.append((search_category, recommended_item))
    
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
    
    category_data = process_json_files(json_files)
    
    while True:
        print("\nMenu:")
        print("1. Recommend based on Space Stone")
        print("2. Recommend based on Power Stone")
        print("3. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            search_category = input("Enter a category: ")
            if search_category in category_data:
                recommended_items = recommend_items_space(category_data, search_category)
                print("\nRecommended items in different categories (Space Stone):")
                for i, (category, item) in enumerate(recommended_items, start=1):
                    print(f"Recommendation {i} from {category}:")
                    for key, value in item.items():
                        print(f"{key}: {value}")
                    print()
            else:
                print("Invalid category")
        elif choice == '2':
            search_category = input("Enter a category: ")
            if search_category in category_data:
                recommended_items = recommend_items_power(category_data, search_category)
                print("\nRecommended items with weaker power levels (Power Stone):")
                for i, (category, item) in enumerate(recommended_items, start=1):
                    print(f"Recommendation {i} from {category}:")
                    for key, value in item.items():
                        print(f"{key}: {value}")
                    print()
            else:
                print("Invalid category")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
