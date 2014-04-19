from echo import echo

def test_given_no_arguments_then_prints_newline(capsys):
    echo()

    out, err = capsys.readouterr()
    assert out == "\n"


def test_given_empty_string_then_prints_newline(capsys):
    echo("")

    out, err = capsys.readouterr()
    assert out == "\n"


def test_given_one_character_then_prints_character_and_newline(capsys):
    echo("a")

    out, err = capsys.readouterr()
    assert out == "a\n"
