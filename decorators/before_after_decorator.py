from typing import List


def before_and_after(func):
    def wrapper(*args, **kwargs):
        print("BEFORE")
        result = func(*args, **kwargs)
        if result:
            print(result)
        print("AFTER")
        return result
    return wrapper


@before_and_after
def greet(name: str):
    print(f"Hi {name}")


@before_and_after
def adder(num1: int, num2: int, *args: List[int]) -> int:
    return num1 + num2 + sum(args)


if __name__ == "__main__":
    greet("Vadim")
    adder(1, 2)
