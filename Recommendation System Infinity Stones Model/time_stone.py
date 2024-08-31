import json

def load_json(json_files):
    group_data = {} #create a dictionary to store json files data
    
   
    for file_name in json_files:
        try:
            with open(file_name, 'r') as json_file:
                group_name = file_name.split('.')[0]
                data = json.load(json_file) #stores all the json files data in variable data
                group_data[group_name] = data
        except FileNotFoundError:
             print("{} files not found.".format(file_name))
    
    return group_data

def recommend_latest_and_oldest_models(group_data, selected_group):
    if selected_group in group_data:
        data = group_data[selected_group]
        
        
        data_with_years = [item for item in data if 'Launch-Year' in item]
        
        if data_with_years:
            
            sorted_items = sorted(data_with_years, key=lambda x: x['Launch-Year']) #sort the data by launch year
            
           
            return (selected_group, sorted_items[0]), (selected_group, sorted_items[-1])  # Recommend the oldest and newest items in the selected group
    
    return None, None

def main():
    json_files = ['TV.json', 'Refrigerator.json']
    
    group_data = load_json(json_files)
    
    selected_group = input("What do you want to buy....? (e.g. TV or Refrigerator): ")
    
    oldest, newest = recommend_latest_and_oldest_models(group_data, selected_group)
    
    if oldest and newest:
        print(f"\nCustomers who also bought this: {selected_group} group:")
        for i, (group, item) in enumerate([oldest, newest], start=1):
            print(f"Recommendation {i} from {group}:")
            for key, value in item.items():
                print(f"{key}: {value}")
            print()
    else:
        print(f"No items found in the {selected_group} group with 'Launch-Year' information.")

main()
