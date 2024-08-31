def file():
    dict = {}

    with open("1000.txt") as file:
        for line in file:
            (key, val) = line.split()
            dict[key] = val

    file.close()
    #print(dict)
    for x in dict:
        print(x, ":", dict[x])

def main():
    file()

main()
