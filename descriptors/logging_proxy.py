from typing import Any


class LoggingProxy:
    """Intercept and log all attribute access to an object"""

    def __init__(self, target):
        super().__setattr__("target", target)

    def __getattribute__(self, name: str) -> Any:
        target = super().__getattribute__("target")

        try:
            value = getattr(target, name)
        except AttributeError as e:
            raise AttributeError(
                "{} could not forward request {} to {}".format(
                    super().__getattribute__("__class__").__name__,
                    name,
                    target
                )
            ) from e
        print(f"Retrieved attribute {name} == {value!r} from {target!r}")
        return value

    def __setattr__(self, name: str, value: Any) -> None:
        target = super().__getattribute__("target")
        setattr(target, name, value)


if __name__ == "__main__":
    from vector import ColoredVector

    c = ColoredVector(red=10, green=20, blue=30, x=1, y=5)
    proxy = LoggingProxy(c)

    proxy.red
    proxy.red = 25
    proxy.red
