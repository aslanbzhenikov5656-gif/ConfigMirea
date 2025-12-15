import math
from lark import Transformer, Token, Tree

class ConfigTransformer(Transformer):
    # Токены
    def INT(self, tok: Token):
        return int(str(tok))

    def NAME(self, tok: Token):
        return str(tok)

    def STRING(self, tok: Token):
        s = str(tok)        # например: q(Это строка)
        return s[2:-1]      # убираем q( и )

    # Правила
    def number(self, items):
        # items уже содержит INT -> int
        return items[0]

    def string(self, items):
        # items содержит результат STRING()
        return items[0]

    def array(self, items):
        # items — список значений (уже преобразованных)
        return list(items)

    def const_decl(self, items):
        # items: [NAME, value]
        name = str(items[0])
        value = items[1]
        # сохраняем как Python value
        self.consts[name] = value
        return None

    def value_stmt(self, items):
        # items: [value]
        return items[0]

    def var(self, items):
        name = str(items[0])
        if name not in self.consts:
            raise ValueError(f"Неизвестная константа: {name}")
        return self.consts[name]

    def add(self, items):
        return items[0] + items[1]

    def sub(self, items):
        return items[0] - items[1]

    def function(self, items):
        # варианты: sqrt(expr) -> items: [val]
        #          concat(expr,expr) -> items: [left, right]
        if len(items) == 1:
            return math.sqrt(items[0])
        return items[0] + items[1]

    def const_expr(self, items):
        # items: [expr value]
        return items[0]

    def object(self, items):
        obj = {}
        for k, v in items:
            obj[str(k)] = v
        return obj

    def pair(self, items):
        return (items[0], items[1])

    def start(self, items):
        # убираем None (объявления const возвращают None)
        return [x for x in items if x is not None]

    # Инициализация состояния трансформера
    def __init__(self):
        super().__init__()
        self.consts = {}

    # Универсальный "fallback" — если какой-то узел не обработан,
    # Lark вызовет __default__ (data, children, meta).
    # Мы пытаемся вернуть "детей" либо одиночное значение для удобства.
    def __default__(self, data, children, meta):
        # Если ребенок — единственный, просто возвращаем его
        if len(children) == 1:
            return children[0]
        return children
