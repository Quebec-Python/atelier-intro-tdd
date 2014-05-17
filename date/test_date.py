import datetime
from date import date


TIMESTAMP = datetime.datetime(2001, 2, 3, 4, 5, 6)


def test_given_no_format_then_prints_newline(capsys):
    date(TIMESTAMP, '')

    out, err = capsys.readouterr()
    assert out == '\n'


def test_given_format_with_text_then_prints_text(capsys):
    date(TIMESTAMP, 'abc 123')

    out, err = capsys.readouterr()
    assert out == 'abc 123\n'


def test_given_format_with_double_percent_then_prints_percent(capsys):
    date(TIMESTAMP, '%%')

    out, err = capsys.readouterr()
    assert out == '%\n'


def test_given_full_date_then_prints_all_fields(capsys):
    fields = {
        '%Y': TIMESTAMP.year,
        '%m': TIMESTAMP.month,
        '%d': TIMESTAMP.day,
        '%H': TIMESTAMP.hour,
        '%M': TIMESTAMP.minute,
        '%S': TIMESTAMP.second
    }

    for fmt, field in fields.items():
        date(TIMESTAMP, fmt)

        out, err = capsys.readouterr()
        assert str(field) in out


def test_given_percent_b_then_prints_full_month_name(capsys):
    months = {
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

    for number, name in months.items():
        timestamp = datetime.datetime(2000, number, 1, 0, 0, 0)
        date(timestamp, '%A')

        out, err = capsys.readouterr()
        assert name in out


def test_given_percent_a_then_prints_full_week_day(capsys):
    #days in the month of january 2000
    days = {
        2: 'Sunday',
        3: 'Monday',
        4: 'Tuesday',
        5: 'Wednesday',
        6: 'Thursday',
        7: 'Friday',
        8: 'Saturday',
    }

    for number, name in days.items():
        timestamp = datetime.datetime(2000, 1, number, 0, 0, 0)
        date(timestamp, '%B')

        out, err = capsys.readouterr()
        assert name in out
