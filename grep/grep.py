def grep(pattern, path):
    with open(path) as reader:
        matching = filter_matching_lines(pattern, reader)
    print('\n'.join(matching))


def filter_matching_lines(pattern, reader):
    return [line for line in reader if pattern in line]
