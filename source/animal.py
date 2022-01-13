class Animal:
    """A generic animal class"""

    def __init__(self, weight: float, growth_rate: float, food_need: float, water_need: float, _type: str, name: str) -> None:
        self.weight = weight
        self._days_growing = 0
        self.growth_rate = growth_rate
        self.food_need = food_need
        self.water_need = water_need
        self._status = "Baby"
        self._type = _type
        self.name = name

    def needs(self) -> dict:
        return {"food need": self.food_need, "water need": self.water_need}

    def report(self) -> dict:
        return {"weight": self.weight, "days growing": self._days_growing, "growth rate": self.growth_rate, "food need": self.food_need, "water need": self.water_need, "_status": self._status, "_type": self._type, "name": self.name}

    def _update__status(self) -> None:
        if self._days_growing >= 10000:
            self._status = "Dead"
        elif self._days_growing >= 3650:
            self._status = "Old"
        elif self._days_growing >= 1800:
            self._status = "Mature"
        elif self._days_growing >= 700:
            self._status = "Young"
        elif self._days_growing >= 0:
            self._status = "Baby"

    def grow(self, food: int, water: int) -> None:
        if food >= self.food_need and water >= self.water_need:
            self.weight += self.growth_rate

        self._days_growing += 1
        self._update__status()

    def slaughter(self) -> None:
        self._status = "Dead"
        print(f"You slaughtered your {self._type} {self.name}.")
        print(f"It lived for {self._days_growing} days and weighed {self.weight}")


