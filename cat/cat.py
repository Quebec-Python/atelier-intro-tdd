import sys
import os

def cat(filepath):
    if not os.path.exists(filepath):
        print_no_such_file(filepath)
    else:
        output = open(filepath).read()
        print(output)


def print_no_such_file(filepath):
    message = "cat: {}: No such file or directory"
    sys.stderr.write(message.format(filepath))
