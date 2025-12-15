from .conftest import parse_cfg


def test_constant_reference(parser):
    text = """
    const x = 7;
    $x$;
    """
    result = parse_cfg(parser, text)
    assert result == [7]


def test_expression_with_constants(parser):
    text = """
    const a = 3;
    const b = 4;
    $a + b$;
    """
    result = parse_cfg(parser, text)
    assert result == [7]
