import json
import argparse
from pathlib import Path
from lark import Lark, exceptions
from transformer import ConfigTransformer

def main():
    argp = argparse.ArgumentParser(
        description="Учебный конфигурационный язык → JSON"
    )
    argp.add_argument(
        "--input", required=True, help="Путь к входному файлу"
    )
    args = argp.parse_args()

    base_dir = Path(__file__).parent
    grammar_path = base_dir / "grammar.lark"

    with open(grammar_path, encoding="utf-8") as f:
        grammar = f.read()

    input_path = Path(args.input)
    # если передали относительный путь от текущей директории, используем его как есть
    if not input_path.exists():
        print(f"Входной файл не найден: {args.input}")
        return

    with open(input_path, encoding="utf-8") as f:
        text = f.read()

    parser = Lark(grammar, parser="lalr", propagate_positions=True, maybe_placeholders=False)

    try:
        tree = parser.parse(text)
        transformer = ConfigTransformer()
        result = transformer.transform(tree)

        # --- дополнительная проверка: если вдруг остался Tree, покажем где ---
        from lark import Tree
        def find_first_tree(obj, path="root"):
            if isinstance(obj, Tree):
                return (path, obj)
            if isinstance(obj, list):
                for i, v in enumerate(obj):
                    res = find_first_tree(v, path + f"[{i}]")
                    if res:
                        return res
            return None

        bad = find_first_tree(result)
        if bad:
            path, tree_node = bad
            print("В результате трансформации остался узел Tree — это баг трансформера.")
            print("Путь:", path)
            print("Tree:", tree_node)
            # печатаем структуру для отладки
            print("Полный результат (repr):", repr(result))
            return

        print(json.dumps(result, ensure_ascii=False, indent=2))

    except exceptions.LarkError as e:
        print("Синтаксическая ошибка:")
        print(e)
    except Exception as e:
        print("Ошибка трансляции:")
        print(e)

if __name__ == "__main__":
    main()
