class Planet:

    def __init__(
        self,
        name,
        radius_metres,
        mass_kilograms,
        orbital_period_seconds,
        surface_temperature_kelvin
    ) -> None:
        self.name = name
        self.radius_metres = radius_metres
        self.mass_kilograms = mass_kilograms
        self.orbital_period_seconds = orbital_period_seconds
        self.surface_temperature_kelvin = surface_temperature_kelvin

    @property
    def name(self):
        return self._name

    @property.setter
    def name(self, value):
        if not value:
            raise ValueError("Cannot set empty name")
        self._name = value
