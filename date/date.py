def date(timestamp, pattern):
    output = (pattern
              .replace('%%', '%')
              .replace('%Y', str(timestamp.year))
              .replace('%m', str(timestamp.month))
              .replace('%d', str(timestamp.day))
              .replace('%H', str(timestamp.hour))
              .replace('%M', str(timestamp.minute))
              .replace('%S', str(timestamp.second)))
    print(output)
