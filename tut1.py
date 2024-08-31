def main():
    file = open("myfile.txt", "r+")
    content = file.read()
    print(content)
    file.close()

main()
