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
