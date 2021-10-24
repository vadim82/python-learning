import random
from typing import Callable


def multiple_runs(number_of_times=2):
    def wrap(func: Callable):
        def repeater(*args, **kwargs):
            return tuple(
                func(*args, **kwargs)
                for _ in range(number_of_times)
            )
        return repeater
    return wrap


@multiple_runs(10)
def roll_dice():
    return random.randint(1, 6)


if __name__ == "__main__":
    result = roll_dice()
    print(result)
