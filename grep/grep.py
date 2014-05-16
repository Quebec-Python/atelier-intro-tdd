def grep(pattern, *paths):
    matching = []

    for path in paths:
        with open(path) as reader:
            matching.extend(filter_matching_lines(pattern, reader))

    print('\n'.join(matching))


def filter_matching_lines(pattern, reader):
    return [line for line in reader if pattern in line]
