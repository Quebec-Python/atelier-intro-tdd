import re


def grep(pattern, *paths, **options):
    flags = compile_flags(options)
    regex = re.compile(pattern, flags)
    matching = []

    for path in paths:
        with open(path) as reader:
            matching.extend(filter_matching_lines(regex, reader))

    if options.get('line_number', False):
        lines = ['{}:{}'.format(line_number, line)
                 for (line_number, line) in matching]
    else:
        lines = [line for (line_number, line) in matching]

    print('\n'.join(lines))


def compile_flags(options):
    flags = 0
    if options.get('ignore_case', False):
        flags |= re.I
    return flags


def filter_matching_lines(regex, reader):
    matching = []
    for line_number, line in enumerate(reader.readlines(), 1):
        if regex.match(line):
            matching.append((line_number, line))

    return matching
