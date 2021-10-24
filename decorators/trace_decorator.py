from typing import Any, Callable

# Instance as a decorator...
# Notice that the __call__ method is the one that
# will wrap the function rather then the __init__ like
# in the class decorator

class Trace:
    def __init__(self) -> None:
        self.enabled = True

    def __call__(self, f: Callable) -> Any:
        def wrap(*args, **kwargs):
            if self.enabled:
                print(f"Calling {f}")
            return f(*args, **kwargs)
        return wrap


tracer = Trace()

@tracer
def rotate_list(l):
    return l[1:] + [l[0]]

rotate_list([1,2,3,4])