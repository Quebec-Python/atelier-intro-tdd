import sys
import os

def cat(*filepaths, **options):
    for filepath in filepaths:
        if valid_filepath(filepath):
            print_file(filepath, options)


def valid_filepath(filepath):
    if not os.path.exists(filepath):
        error_no_such_file(filepath)
        return False
    elif os.path.isdir(filepath):
        error_is_a_directory(filepath)
        return False
    return True


def error_no_such_file(filepath):
    message = "cat: {}: No such file or directory"
    sys.stderr.write(message.format(filepath))


def error_is_a_directory(filepath):
    message = "cat: {}: is a directory"
    sys.stderr.write(message.format(filepath))


def print_file(filepath, options):
    with open(filepath) as reader:
        lines = reader.readlines()
        for number, line in enumerate(lines, 1):
            line = line.rstrip()

            if options.get('number', False):
                sys.stdout.write("{}: ".format(number))

            sys.stdout.write(line)

            if options.get('ends', False):
                sys.stdout.write('$')

            sys.stdout.write("\n")
