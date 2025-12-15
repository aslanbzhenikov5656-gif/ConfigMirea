from .conftest import parse_cfg


def test_simple_array(parser):
    text = """
    <<1, 2, 3>>;
    """
    result = parse_cfg(parser, text)
    assert result == [[1, 2, 3]]


def test_nested_array(parser):
    text = """
    <<
      1,
      <<2, 3>>,
      <<4, <<5>> >>
    >>;
    """
    result = parse_cfg(parser, text)
    assert result == [[1, [2, 3], [4, [5]]]]
