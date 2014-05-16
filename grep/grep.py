def grep(pattern, path):
    matching = []
    with open(path) as reader:
        for line in reader:
            if pattern in line:
                matching.append(line)

    print('\n'.join(matching))
