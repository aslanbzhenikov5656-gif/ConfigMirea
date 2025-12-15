import pytest
from lark import exceptions
from .conftest import parse_cfg


def test_unknown_constant(parser):
    text = """
    $unknown + 1$;
    """
    with pytest.raises(Exception):
        parse_cfg(parser, text)


def test_syntax_error(parser):
    text = """
    const a = 1
    """
    with pytest.raises(exceptions.LarkError):
        parse_cfg(parser, text)
