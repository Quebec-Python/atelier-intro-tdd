from grep import grep


def test_given_empty_file_when_empty_pattern_then_prints_nothing(capsys, tmpdir):
    path = tmpdir.join('emptyfile')
    path.write('')

    grep('', str(path))

    out, err = capsys.readouterr()
    assert out == "\n"


def test_given_file_with_a_line_when_empty_pattern_then_prints_line(capsys, tmpdir):
    path = tmpdir.join('oneline')
    path.write('one line')

    grep('', str(path))

    out, err = capsys.readouterr()
    assert 'one line' in out


def test_given_file_with_two_lines_when_pattern_contains_a_line_then_prints_line(capsys, tmpdir):
    path = tmpdir.join('twolines')
    path.write('a\nb\n')

    grep('b', str(path))

    out, err = capsys.readouterr()
    assert 'b' in out
    assert 'a' not in out
