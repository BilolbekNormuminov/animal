from animal import Animal


class Cow(Animal):
    """A cow class"""

    def __init__(self, weight: float, growth_rate: float, food_need: float, water_need: float, name: str) -> None:
        self.weight = weight
        self._days_growing = 0
        self.growth_rate = growth_rate
        self.food_need = food_need
        self.water_need = water_need
        self._status = "Baby"
        self._type = "Cow"
        self.name = name

    def grow(self, food: float, water: float) -> None:
        if food >= self.food_need and water >= self.water_need:
            if food >= 10:
                self.weight += self.growth_rate
            if food >= 5:
                self.weight += self.growth_rate * 0.75
            if food >= 0:
                self.weight += self.growth_rate * 0.5

        self._days_growing += 1
        self._update__status()
