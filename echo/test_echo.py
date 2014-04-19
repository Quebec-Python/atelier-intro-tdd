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


def test_given_multiple_arguments_then_prints_them_seperated_by_spaces(capsys):
    echo("a", "b", "c")

    out, err = capsys.readouterr()
    assert out == "a b c\n"


def test_given_option_newline_disabled_then_does_not_print_new_line(capsys):
    echo("a", newline=False)

    out, err = capsys.readouterr()
    assert out == "a"
