from random import randint
from typing import Callable, List, Mapping

FUNCTIONS: Mapping[str, List[Callable]] = {}


def register(func: Callable):
    FUNCTIONS.setdefault(func.__name__, [])
    FUNCTIONS[func.__name__].append(func)
    return func

@register
def roll_dice():
    return randint(1, 6)

@register
def test():
    pass

if __name__ == "__main__":
    print(FUNCTIONS)
