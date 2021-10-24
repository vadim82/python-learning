from typing import Callable, List
import functools
import random


def retry(*error_types: List[Exception]):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            while True:
                try:
                    return func(*args, **kwargs)
                except Exception as ex:
                    if type(ex) not in error_types:
                        raise
                    else:
                        print(f"retrying.... {type(ex).__name__}")
        return wrapper
    return decorator


class CustomError(Exception):
    pass


@retry(ValueError, CustomError)
def calculation():
    number = random.randint(-5, 5)
    if number == -5:
        raise CustomError("test")
    elif abs(1 / number) > 0.2:
        raise ValueError(number)
    return number


if __name__ == "__main__":
    result = calculation()
    print(result)
