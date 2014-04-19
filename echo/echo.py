import sys

def echo(*args, **kwargs):
    output = " ".join(args)
    sys.stdout.write(output)

    if kwargs.get('newline', True):
        sys.stdout.write("\n")
