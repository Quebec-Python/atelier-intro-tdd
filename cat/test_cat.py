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


def test_given_multiple_files_then_prints_them_in_order(capsys, tmpdir):
    first_file = tmpdir.join('firstfile')
    first_file.write('Roses are red')

    second_file = tmpdir.join('secondfile')
    second_file.write('Violets are blue')

    cat(str(first_file), str(second_file))

    out, err = capsys.readouterr()
    assert out == "Roses are red\nViolets are blue\n"
