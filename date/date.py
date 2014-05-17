MONTHS = {
    1: 'January',
    2: 'Febuary',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

DAYS = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}

def date(timestamp, pattern):
    output = (pattern
              .replace('%%', '%')
              .replace('%Y', str(timestamp.year))
              .replace('%m', str(timestamp.month))
              .replace('%d', str(timestamp.day))
              .replace('%H', str(timestamp.hour))
              .replace('%M', str(timestamp.minute))
              .replace('%S', str(timestamp.second))
              .replace('%A', month_name(timestamp))
              .replace("%B", weekday_name(timestamp)))
    print(output)


def month_name(timestamp):
    return MONTHS[timestamp.month]


def weekday_name(timestamp):
    return DAYS[timestamp.weekday()]
