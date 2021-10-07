from typing import Tuple
from functools import reduce


def hypervolume(length: int, *lengths: Tuple[int]):
    print(lengths)
    v = length
    for l in lengths:
        v *= l
    return v


def color(red, green, blue, **kwargs):
    print(f"{red=}")
    print(f"{green=}")
    print(f"{blue=}")
    print(kwargs)


def tag(name: str, text: str, **attributes):

    # " ".join(f"{k} = {v}" for k,v in attributes.items())
    attrs = reduce(lambda p, c: f"{p} {c[0]}={c[1]}", attributes.items(), "")
    return f"<{name}{attrs}>{text}</{name}>"


if __name__ == "__main__":
    t = tag("img", "some text", src="http://www.google.com", alt="some image")
    print(t)

    dims = (2, 4, 5, 6, 7, 8)
    print(hypervolume(*dims))

    k = {'red': 21, 'green': 68, 'blue': 1, 'alpha': 52}
    color(**k)
