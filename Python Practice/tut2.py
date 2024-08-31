def file_ops():
    d = {}

    with open("myfile.txt") as f:
        for line in f:
            (key,val) = line.split()
            d[int(key)] = val

    f.close()
    print(d)

def main():
    file_ops()

main()
