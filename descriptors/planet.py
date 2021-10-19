from positive import Positive


class Planet:

    def __init__(
        self,
        name,
        radius_metres: int,
        mass_kilograms,
        orbital_period_seconds,
        surface_temperature_kelvin
    ) -> None:
        self.name = name
        # the code below.. is proxied by the Positive descriptor
        # this means it called the __set__ method of the positive descriptor like this
        # Positive.__set__(Planet.__dict__["radius_metres"], self, radius_metres)
        # This is because __setattribute__ is what = does.. and Descriptors take precendence
        # over setting stuff on the instance.
        self.radius_metres = radius_metres
        self.mass_kilograms = mass_kilograms
        self.orbital_period = orbital_period_seconds
        self.surface_temperature = surface_temperature_kelvin
        self.test = 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Cannot set empty name")
        self._name = value

    # These are class attributes and run before __init__
    # when you call pluto.radius_metres that is the same as calling
    # Positive.__get__(Planet.__dict__["radius_metres"], pluto, Planet)
    radius_metres = Positive()
    mass_kilograms = Positive()
    orbital_period = Positive()
    surface_temperature = Positive()

    test = 44
