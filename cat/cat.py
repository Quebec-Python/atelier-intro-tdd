import sys

def cat(filename):
    message = "cat: {}: No such file or directory"
    sys.stderr.write(message.format(filename))
