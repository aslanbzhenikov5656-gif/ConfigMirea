import sys
from pathlib import Path

# Добавляем src в PYTHONPATH
PROJECT_ROOT = Path(__file__).parent.parent
SRC_PATH = PROJECT_ROOT / "src"
sys.path.insert(0, str(SRC_PATH))

import pytest
from lark import Lark
from transformer import ConfigTransformer


@pytest.fixture(scope="module")
def parser():
    grammar_path = SRC_PATH / "grammar.lark"
    grammar = grammar_path.read_text(encoding="utf-8")
    return Lark(grammar, parser="lalr")


def parse_cfg(parser, text):
    tree = parser.parse(text)
    transformer = ConfigTransformer()
    return transformer.transform(tree)
