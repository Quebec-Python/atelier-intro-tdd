import pytest

from echo import echo


class Output(object):

    def __init__(self, capsys):
        self.capsys = capsys

    @property
    def out(self):
        stdout, _ = self.capsys.readouterr()
        return stdout


@pytest.fixture
def output(capsys):
    return Output(capsys)


def test_given_no_arguments_then_prints_newline(output):
    echo()
    assert output.out == "\n"


def test_given_empty_string_then_prints_newline(output):
    echo("")
    assert output.out == "\n"


def test_given_one_character_then_prints_character_and_newline(output):
    echo("a")
    assert output.out == "a\n"


def test_given_multiple_arguments_then_prints_them_seperated_by_spaces(output):
    echo("a", "b", "c")
    assert output.out == "a b c\n"


def test_given_option_newline_disabled_then_does_not_print_new_line(output):
    echo("a", newline=False)
    assert output.out == "a"
