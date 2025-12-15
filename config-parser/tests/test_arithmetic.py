from .conftest import parse_cfg


def test_addition(parser):
    text = """
    const a = 10;
    $a + 5$;
    """
    result = parse_cfg(parser, text)
    assert result == [15]


def test_subtraction(parser):
    text = """
    const a = 20;
    $a - 7$;
    """
    result = parse_cfg(parser, text)
    assert result == [13]
