import re


def grep(pattern, *paths, **options):
    regex = compile_regex(pattern, options)
    matching = find_matching_lines(regex, paths)
    lines = format_lines(matching, options)
    print('\n'.join(lines))


def compile_regex(pattern, options):
    flags = 0
    if options.get('ignore_case', False):
        flags |= re.I

    return re.compile(pattern, flags)


def find_matching_lines(regex, paths):
    matching = []
    for path in paths:
        with open(path) as reader:
            matching.extend(filter_matching_lines(regex, reader))

    return matching


def filter_matching_lines(regex, reader):
    matching = []
    for line_number, line in enumerate(reader.readlines(), 1):
        if regex.match(line):
            matching.append((line_number, line.strip()))

    return matching


def format_lines(matching, options):
    template = '{line}'
    if options.get('line_number', False):
        template = '{number}:{line}'

    return [template.format(number=number, line=line) for (number, line) in matching]
