import re


def grep(pattern, *paths, **options):
    flags = compile_flags(options)
    regex = re.compile(pattern, flags)
    matching = []

    for path in paths:
        with open(path) as reader:
            matching.extend(filter_matching_lines(regex, reader))

    print('\n'.join(matching))


def compile_flags(options):
    flags = 0
    if options.get('ignore_case', False):
        flags |= re.I
    return flags


def filter_matching_lines(regex, reader):
    return [line for line in reader if regex.match(line)]
