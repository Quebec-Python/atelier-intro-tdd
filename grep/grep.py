def grep(pattern, path):
    with open(path) as reader:
        print(reader.read())
