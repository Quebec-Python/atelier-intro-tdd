from cat import cat

def test_given_wrong_file_name_then_prints_error_message(capsys):
    cat('superduperfilename')

    out, err = capsys.readouterr()
    assert err == "cat: superduperfilename: No such file or directory"


def test_given_empty_file_then_prints_newline(capsys, tmpdir):
    filepath = tmpdir.join('emptyfile')
    filepath.write('')

    cat(str(filepath))

    out, err = capsys.readouterr()
    assert out == "\n"


def test_given_single_file_then_prints_newline(capsys, tmpdir):
    filepath = tmpdir.join('poem')
    filepath.write("The quick brown fox jumps over the lazy dog")

    cat(str(filepath))

    out, err = capsys.readouterr()
    assert out == "The quick brown fox jumps over the lazy dog\n"
