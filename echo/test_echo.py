from echo import echo

def test_given_no_arguments_then_prints_newline(capsys):
    echo()

    out, err = capsys.readouterr()
    assert out == "\n"
