def read_dictionary(file_name):
    dictionary = {}
    
    try:
        with open("dictionary.txt", 'r') as file:
            lines = file.readlines()
            
            term = None
            definition = []
            
            for line in lines:
                line = line.strip()
                
                if line.isupper():
                    
                    if term:
                        dictionary[term] = '\n'.join(definition)
                    
                    term = line
                    definition = []
                else:
                    definition.append(line)
            
            
            if term:
                dictionary[term] = '\n'.join(definition)
                
    except FileNotFoundError:
        print("File '{dictionary.txt}' not found.")
    
    return dictionary

def search_dictionary(dictionary, term):
    term = term.upper()
    
    if term in dictionary:
        print(dictionary[term])
    else:
        print("ERROR in ANYTHING")

def main():
    print("*******************************************************************************")
    print("WELCOME TO ANYTHING")
    print("*******************************************************************************")
    
    file_name = "dictionary.txt"
    dictionary = read_dictionary(file_name)
    
    if dictionary:
        while True:
            print("Enter the word to search in anything (or 'q' to quit):")
            query = input()
            
            if query.lower() == 'q':
                break
            
            search_dictionary(dictionary, query)

if __name__ == "__main__":
    main()
