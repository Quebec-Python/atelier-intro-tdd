import pytest

from cat import cat


class FileMaker(object):

    def __init__(self, tmpdir):
        self.tmpdir = tmpdir

    def create_file(self, filename, contents):
        filepath = self.tmpdir.join(filename)
        filepath.write(contents)
        return str(filepath)


@pytest.fixture
def filemaker(tmpdir):
    return FileMaker(tmpdir)


def test_given_wrong_file_name_then_prints_error_message(capsys):
    cat('superduperfilename')

    out, err = capsys.readouterr()
    assert err == "cat: superduperfilename: No such file or directory"


def test_given_directory_then_prints_error_message(capsys, tmpdir):
    dirname = str(tmpdir)

    cat(dirname)

    out, err = capsys.readouterr()
    assert err == "cat: {}: is a directory".format(dirname)


def test_given_empty_file_then_prints_nothing(capsys, filemaker):
    filepath = filemaker.create_file("emptyfile", "")

    cat(filepath)

    out, err = capsys.readouterr()
    assert out == ""


def test_given_single_file_then_prints_newline(capsys, filemaker):
    filepath = filemaker.create_file("poem",
        "The quick brown fox jumps over the lazy dog")

    cat(filepath)

    out, err = capsys.readouterr()
    assert out == "The quick brown fox jumps over the lazy dog\n"


def test_given_multiple_files_then_prints_them_in_order(capsys, filemaker):
    first_file = filemaker.create_file("firstfile", "Roses are red")
    second_file = filemaker.create_file("secondfile", "Violets are blue")

    cat(first_file, second_file)

    out, err = capsys.readouterr()
    assert out == "Roses are red\nViolets are blue\n"


def test_given_option_number_then_prints_line_numbers(capsys, filemaker):
    filepath = filemaker.create_file("multiline", "a\nb\nc")

    cat(filepath, number=True)

    out, err = capsys.readouterr()
    assert out == "1: a\n2: b\n3: c\n"
