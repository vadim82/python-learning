from typing import Any, Dict, Mapping


class Vector:
    """An n-dimentional vector"""

    def __init__(self, **components) -> None:
        private_dims = {f"_{k}": v for k, v in components.items()}
        self.__dict__.update(private_dims)

    def __repr__(self) -> str:
        # return f"{type(self).__name__} ({self.x}, {self.y})"
        return "{} ({})".format(
            type(self).__name__,
            ", ".join(
                "{k}={v}".format(k=k, v=v)
                for k, v in self._args().items()
            )
        )

    def __getattr__(self, name: str) -> Any:
        p_name = f"_{name}"
        try:
            return self.__dict__[p_name]
        except KeyError:
            raise AttributeError(f"{self} object has no attribute {name}")

    def __setattr__(self, name: str, value: Any) -> None:
        self.__dict__[f"_{name}"] = value

    def _args(self) -> Dict[str, Any]:
        return {
            k[1:]: v
            for k, v in self.__dict__.items()
        }


class ColoredVector(Vector):
    COLOR_INDEXES = ("red", "green", "blue")

    def __init__(self, red, green, blue, **components) -> None:
        super().__init__(**components)
        self.__dict__["_color"] = [red, green, blue]

    def __getattr__(self, name: str) -> Any:
        try:
            channel = ColoredVector.COLOR_INDEXES.index(name)
        except ValueError:
            super().__getattr__(name)
        else:
            return self.__dict__["_color"][channel]

    def __setattr__(self, name: str, value: Any) -> None:
        try:
            channel = ColoredVector.COLOR_INDEXES.index(name)
        except ValueError:
            super().__setattr__(name, value)
        else:
            self.__dict__["_color"][channel] = value

    def _args(self) -> Dict[str, Any]:
        color = self.__dict__["_color"]
        args = {
            "red": color[0],
            "green": color[1],
            "blue": color[2]
        }
        args.update(super()._args())
        del args["color"]
        print(args)
        return args


if __name__ == "__main__":
    c = ColoredVector(red=10, green=25, blue=100, p=10, q=1)

    print(c)
