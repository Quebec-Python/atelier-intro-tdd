from sousou import translate_number


def test_given_number_one_when_translated_then_prints_kere(capsys):
    translate_number(1)

    out, err = capsys.readouterr()
    assert "kere" in out
