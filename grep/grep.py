import re


def grep(pattern, *paths):
    regex = re.compile(pattern)
    matching = []

    for path in paths:
        with open(path) as reader:
            matching.extend(filter_matching_lines(regex, reader))

    print('\n'.join(matching))


def filter_matching_lines(regex, reader):
    return [line for line in reader if regex.match(line)]
