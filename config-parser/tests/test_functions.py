from math import isclose
from .conftest import parse_cfg


def test_sqrt(parser):
    text = """
    const x = 16;
    $sqrt(x)$;
    """
    result = parse_cfg(parser, text)
    assert isclose(result[0], 4.0)


def test_concat(parser):
    text = """
    const a = q(Hello );
    const b = q(World);
    $concat(a, b)$;
    """
    result = parse_cfg(parser, text)
    assert result[0] == "Hello World"
