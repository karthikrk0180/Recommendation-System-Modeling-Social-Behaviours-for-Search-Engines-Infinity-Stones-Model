import json

def load_json(json_files):
    group_data = {}
    
    # Load data from JSON files and store it in the group_data dictionary
    for file_name in json_files:
        try:
            with open(file_name, 'r') as json_file:
                group_name = file_name.split('.')[0]
                data = json.load(json_file)
                group_data[group_name] = data
        except FileNotFoundError:
             print("{}files not found.".format(file_name))
    
    return group_data

def find_smallest_and_largest_screen_sizes(group_data, group_name):
    smallest_screen_size = None
    largest_screen_size = None
    smallest_product = None
    largest_product = None
    #to store the largest and smallest screen size found and to store respective other specs
    
    if group_name in group_data:
        data = group_data[group_name]
        
        if data:
            products_with_size = [(item, item.get('Screen-Size', item.get('screen-size'))) for item in data if 'Screen-Size' in item or 'screen-size' in item]
            
            
            products_with_size = [(item, size) for item, size in products_with_size if size is not None] #remove items with no attribute screen-size
            
           
            if products_with_size:
                smallest_product, smallest_screen_size = min(products_with_size, key=lambda x: x[1]) #smallest screen size
                largest_product, largest_screen_size = max(products_with_size, key=lambda x: x[1]) #largest screen size
    
    return smallest_product, largest_product

def main():
    json_files = [ 'Laptop.json', 'Tablet.json']
    
    group_data = load_json(json_files)
    
    user_input = input("Enter 'Laptop' or 'Tablet' for recommendations: ").strip().lower()
    
    if user_input == 'laptop':
        group_name = 'Laptop'
    elif user_input == 'tablet':
        group_name = 'Tablet'
    else:
        print("Invalid input. Please enter 'Laptop' or 'Tablet'.")
        return
    
    smallest_product, largest_product = find_smallest_and_largest_screen_sizes(group_data, group_name)
    
    if smallest_product is not None and largest_product is not None:
        print(f"\nGroup: {group_name}")
        print("\n\nCustomers who also bought this:")
        for key, value in smallest_product.items():
            print(f"{key}: {value}")
        
        print("\n\nCustomers who also bought this:")
        for key, value in largest_product.items():
            print(f"{key}: {value}")
    else:
        print(f"No screen size data found for {group_name}")

main()
