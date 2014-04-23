def date(timestamp, pattern):
    output = (pattern
              .replace('%%', '%')
              .replace('%Y', str(timestamp.year)))
    print(output)
