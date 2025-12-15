from pathlib import Path
from math import isclose
from .conftest import parse_cfg

def test_science_measurements(parser):
    text = Path("examples/science_measurements.cfg").read_text(encoding="utf-8")
    result = parse_cfg(parser, text)

    measurements = result[0]
    assert measurements[0] == "measurements"

    sample1 = measurements[1]
    assert sample1[1] == 1
    assert sample1[3] == 9
    assert isclose(sample1[5], 3.0)

    summary = measurements[4]
    roots = summary[1]

    assert roots == [3.0, 4.0, 5.0]
