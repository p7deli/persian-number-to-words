from persian_number_to_words import number_to_words


def test_simple():
    result = number_to_words(123)
    assert "صد" in result.words


def test_zero():
    result = number_to_words(0)
    assert result.words == "صفر"
