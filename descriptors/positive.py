from weakref import WeakKeyDictionary


class Positive:
    """A data-descriptor for positive numeric values"""

    def __init__(self) -> None:
        self._instance_data = WeakKeyDictionary()

    def __get__(self, instance, owner):
        if self:
            print([(x, v) for x, v in self._instance_data.items()])
        return self._instance_data[instance]

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError(f"Value {value} is not positive")
        self._instance_data[instance] = value

    def __delete__(self, instance):
        raise AttributeError("Cannot delete attribute")