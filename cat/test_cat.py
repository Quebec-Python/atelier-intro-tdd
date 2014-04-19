from cat import cat

def test_given_wrong_file_name_then_prints_error_message(capsys):
    cat('superduperfilename')

    out, err = capsys.readouterr()
    assert err == "cat: superduperfilename: No such file or directory"
