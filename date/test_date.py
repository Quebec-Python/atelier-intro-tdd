import datetime
from date import date


TIMESTAMP = datetime.datetime(2001, 2, 3, 4, 5, 6)

def test_given_no_format_then_prints_newline(capsys):
    date(TIMESTAMP, '')

    out, err = capsys.readouterr()
    assert out == '\n'
