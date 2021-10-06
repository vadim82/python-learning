from typing import Tuple
from functools import reduce

def hypervolume(length: int, *lengths: Tuple[int]):
    v = length
    for l in lengths:
        v *= l
    return v

def tag(name: str, text: str, **attributes):

    # " ".join(f"{k} = {v}" for k,v in attributes.items())
    attrs = reduce( lambda p, c: f"{p} {c[0]}={c[1]}", attributes.items(), "" )
    print(attrs)


if __name__ == "__main__":
    tag("img", "some text", src="http://www.google.com", alt="some image")
