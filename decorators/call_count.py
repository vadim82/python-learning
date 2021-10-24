from typing import Any, Callable


class CallCount:
    def __init__(self, f: Callable) -> None:
        self.f = f
        self.count = 0

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        self.count += 1
        self.f(*args, **kwargs)


@CallCount
def try_me():
    print("tried me")


try_me()
try_me()
try_me()
try_me()
print(try_me.count)