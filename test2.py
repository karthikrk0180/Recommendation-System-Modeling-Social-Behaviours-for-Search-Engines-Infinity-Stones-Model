import json
import random

# Function to load data from JSON files and store it in a dictionary
def process_json_files(json_files):
    category_data = {}
    
    for file_name in json_files:
        try:
            with open(file_name, 'r') as json_file:
                category_name = file_name.split('.')[0]
                data = json.load(json_file)
                category_data[category_name] = data
        except FileNotFoundError:
             print("{} not found.".format(file_name))
    
    return category_data

# Recommendation system based on the Space Stone
def recommend_items_space(category_data, search_category, num_recommendations=5):
    recommended_items = []
    
    while len(recommended_items) < num_recommendations:
        recommended_category = random.choice(list(category_data.keys()))
        
        if recommended_category != search_category:
            recommended_item = random.choice(category_data[recommended_category])
            recommended_items.append((recommended_category, recommended_item))
    
    return recommended_items

# Recommendation system based on the Power Stone
def recommend_items_power(category_data, search_category):
    recommended_items = []
    
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
    
    search_category_power = category_weights.get(search_category, 0)
    
    for category, data in category_data.items():
        category_power = category_weights.get(category, 0)
        
        if category_power < search_category_power:
            recommended_item = random.choice(data)
            recommended_items.append((category, recommended_item))
    
    if search_category_power == min(category_weights.values()):
        recommended_item = random.choice(category_data[search_category])
        recommended_items.append((search_category, recommended_item))
    
    return recommended_items

# Recommendation system based on the Time Stone
def recommend_latest_and_oldest_models(category_data, selected_category):
    if selected_category in category_data:
        data = category_data[selected_category]
        
        data_with_years = [item for item in data if 'Launch-Year' in item]
        
        if data_with_years:
            sorted_items = sorted(data_with_years, key=lambda x: x['Launch-Year'])
            
            return (selected_category, sorted_items[0]), (selected_category, sorted_items[-1])
    
    return None, None

# Recommendation system based on the Reality Stone
def find_smallest_and_largest_screen_sizes(category_data, category_name):
    smallest_screen_size = None
    largest_screen_size = None
    smallest_product = None
    largest_product = None
    
    if category_name in category_data:
        data = category_data[category_name]
        
        products_with_size = [(item, item.get('Screen-Size', item.get('screen-size'))) for item in data if 'Screen-Size' in item or 'screen-size' in item]
        
        products_with_size = [(item, size) for item, size in products_with_size if size is not None]
        
        if products_with_size:
            smallest_product, smallest_screen_size = min(products_with_size, key=lambda x: x[1])
            largest_product, largest_screen_size = max(products_with_size, key=lambda x: x[1])
    
    return smallest_product, largest_product

# Recommendation system based on the Mind Stone
def recommend_random_items(category_data, num_recommendations=3):
    recommended_items = []
    
    for _ in range(num_recommendations):
        selected_category = random.choice(list(category_data.keys()))
        
        if selected_category in category_data:
            data = category_data[selected_category]
            
            if data:
                recommended_item = random.choice(data)
                recommended_items.append((selected_category, recommended_item))
    
    return recommended_items

# Recommendation system based on the Soul Stone
def recommend_items_within_same_category(category_data, selected_category, num_recommendations=3):
    recommended_items = []
    
    if selected_category in category_data:
        data = category_data[selected_category]
        
        if data:
            recommended_items = random.sample(data, num_recommendations)
            recommended_items = [(selected_category, item) for item in recommended_items]
    
    return recommended_items

# Menu-driven program
def main():
    json_files = ['CameraLens.json', 'Laptop.json', 'LaptopPeriferals.json',
                  'Mobile.json', 'Refrigerator.json', 'Tablet.json', 
                  'TV.json', 'WashingMachine.json', 'WearableSmartDevice.json']
    
    category_data = process_json_files(json_files)
    
    while True:
        print("\nMenu:")
        print("1. Recommend based on Space Stone")
        print("2. Recommend based on Power Stone")
        print("3. Recommend based on Time Stone")
        print("4. Recommend based on Reality Stone")
        print("5. Recommend based on Mind Stone")
        print("6. Recommend based on Soul Stone")
        print("7. Quit")
        
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
            selected_category = input("Enter a category (e.g., TV or Refrigerator): ")
            
            oldest, newest = recommend_latest_and_oldest_models(category_data, selected_category)
            
            if oldest and newest:
                print(f"\nRecommended items in the {selected_category} category:")
                for i, (category, item) in enumerate([oldest, newest], start=1):
                    print(f"Recommendation {i} from {category}:")
                    for key, value in item.items():
                        print(f"{key}: {value}")
                    print()
            else:
                print(f"No items found in the {selected_category} category with 'Launch-Year' information.")
        elif choice == '4':
            category_name = input("Enter a category (e.g., Mobile, Laptop): ").strip()
            
            smallest_product, largest_product = find_smallest_and_largest_screen_sizes(category_data, category_name)
            
            if smallest_product is not None and largest_product is not None:
                print(f"\nCategory: {category_name}")
                print("\nSmallest Screen Size Product Specifications:")
                for key, value in smallest_product.items():
                    print(f"{key}: {value}")
                
                print("\nLargest Screen Size Product Specifications:")
                for key, value in largest_product.items():
                    print(f"{key}: {value}")
            else:
                print(f"No screen size data found for {category_name}")
        elif choice == '5':
            recommended_items = recommend_random_items(category_data, num_recommendations=3)
            
            if recommended_items:
                print(f"\nTop 3 recommended random items:")
                for i, (category, item) in enumerate(recommended_items, start=1):
                    print(f"Recommendation {i} from {category}:")
                    for key, value in item.items():
                        print(f"{key}: {value}")
                    print()
            else:
                print("No items found for recommendation.")
        elif choice == '6':
            selected_category = input("Enter a category (e.g., CameraLens or Laptop): ")
            
            recommended_items = recommend_items_within_same_category(category_data, selected_category, num_recommendations=3)
            
            if recommended_items:
                print(f"\nTop 3 recommended items in the {selected_category} category:")
                for i, (category, item) in enumerate(recommended_items, start=1):
                    print(f"Recommendation {i} from {category}:")
                    for key, value in item.items():
                        print(f"{key}: {value}")
                    print()
            else:
                print(f"No items found in the {selected_category} category for recommendation.")
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

