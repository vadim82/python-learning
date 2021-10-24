import functools
import random
from typing import Any, Callable


class Retry:
    _retries = 0

    def __init__(self, func: Callable):
        functools.update_wrapper(self, func)
        self._func = func

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        while True:
            try:
                return self._func(*args, **kwds)
            except Exception as e:
                Retry._retries += 1


@Retry
def only_roll_sixes():
    number = random.randint(1, 6)
    if number != 6:
        raise ValueError(number)
    return number


if __name__ == "__main__":

    r1 = only_roll_sixes()
    print(f"tried: {Retry._retries} times")
    r2 = only_roll_sixes()
    print(f"tried: {Retry._retries} times")
