d={}

def ReadFile():
    
    reading_definition = False
    with open("dictionary.txt","r") as f:
        
        for line in f:
            line=line.strip()
            if line.isupper():
                term = line
                reading_definition = True
                d[term] = ""
            elif reading_definition:
                d[term] += line + "\n" 
    #print(d)
def SearchEngine(query):
    query=query.upper()
    if query in d:
        print(d[query])
    else:
        print("Results not found")

def main():
    print("-------------------------------------------------------------------------------")
    print("WELCOME TO MY SEARCH ENGINE")

    print("*******************************************************************************")
    
    while 1:
       print("Enter the word you want to search")
       query= input()
       SearchEngine(query)
    
ReadFile()
main()
