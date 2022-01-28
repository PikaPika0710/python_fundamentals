def readFile(path):
    file = open(path, 'r', encoding='utf-8')
    for line in file:
        print(line.strip())

    file.close()

readFile("test.txt")