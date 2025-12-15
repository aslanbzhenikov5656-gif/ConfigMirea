from pathlib import Path
from .conftest import parse_cfg


def test_it_system_config(parser):
    text = Path("examples/it_system.cfg").read_text(encoding="utf-8")
    result = parse_cfg(parser, text)

    assert isinstance(result, list)

    system = result[0]
    assert system[0] == "system"

    # system[1] = ["cpu", 6, "memory", 24]
    cpu_mem = system[1]
    assert cpu_mem[0] == "cpu"
    assert cpu_mem[1] == 6
    assert cpu_mem[2] == "memory"
    assert cpu_mem[3] == 24

    # system[2] = ["nodes", [ ... ]]
    nodes = system[2]
    assert nodes[0] == "nodes"

    node_list = nodes[1]
    assert len(node_list) == 2

    node1 = node_list[0]
    assert node1 == ["node", 1, "cpu", 4]

    node2 = node_list[1]
    assert node2 == ["node", 2, "cpu", 6]
