from grep import grep


def test_given_empty_file_when_empty_pattern_then_prints_nothing(capsys, tmpdir):
    path = tmpdir.join('emptyfile')
    path.write('')

    grep('', str(path))

    out, err = capsys.readouterr()
    assert out == "\n"
