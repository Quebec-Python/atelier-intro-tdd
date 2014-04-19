import sys
import os

def cat(*filepaths):
    for filepath in filepaths:
        print_file(filepath)


def print_file(filepath):
    if not os.path.exists(filepath):
        error_no_such_file(filepath)
    elif os.path.isdir(filepath):
        error_is_a_directory(filepath)
    else:
        output = open(filepath).read()
        print(output)


def error_no_such_file(filepath):
    message = "cat: {}: No such file or directory"
    sys.stderr.write(message.format(filepath))


def error_is_a_directory(filepath):
    message = "cat: {}: is a directory"
    sys.stderr.write(message.format(filepath))
