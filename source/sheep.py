from animal import Animal


class Sheep(Animal):
    """A sheep class"""

    def __init__(self, weight: float, growth_rate: float, food_need: float, water_need: float, name: str) -> None:
        self.weight = weight
        self._days_growing = 0
        self.growth_rate = growth_rate
        self.food_need = food_need
        self.water_need = water_need
        self._status = "Baby"
        self._type = "Sheep"
        self.name = name

    def grow(self, food: float, water: float) -> None:
        if food >= self.food_need and water >= self.water_need:
            if food >= 7:
                self.weight += self.growth_rate
            if food >= 3:
                self.weight += self.growth_rate * 0.6
            if food >= 0:
                self.weight += self.growth_rate * 0.3

        self._days_growing += 1
        self._update__status()
