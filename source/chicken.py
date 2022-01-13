from animal import Animal


class Chicken(Animal):
    """A chicken class"""

    def __init__(self, weight: float, growth_rate: float, food_need: float, water_need: float, name: str) -> None:
        self.weight = weight
        self._days_growing = 0
        self.growth_rate = growth_rate
        self.food_need = food_need
        self.water_need = water_need
        self._status = "Baby"
        self._type = "Chicken"
        self.name = name

    def grow(self, food: float, water: float) -> None:
        if food >= self.food_need and water >= self.water_need:
            if food >= 5:
                self.weight += self.growth_rate * 1.5
            if food >= 2:
                self.weight += self.growth_rate * 1.2
            if food >= 0:
                self.weight += self.growth_rate

        self._days_growing += 1
        self._update__status()
