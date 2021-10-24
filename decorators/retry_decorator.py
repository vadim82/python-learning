from typing import Callable, Union

import random
import functools

def retry(max_calls: Union[int, None] = None):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            i = 0
            while True:
                if max_calls != None and max_calls <= i:
                    print("reached max limit")
                    return None
                i += 1
                try:
                    print(f"run {i}")
                    return func(*args, **kwargs)
                except:
                    continue
        return wrapper
    return decorator


@retry()
def only_roll_sixes():
    number = random.randint(1, 6)
    if number != 6:
        raise ValueError(number)
    return number

if __name__ == "__main__":
    result = only_roll_sixes()
    print(f"rolled {result}")
