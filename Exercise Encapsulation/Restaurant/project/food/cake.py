from project.food.dessert import Dessert


class Cake(Dessert):
    GRAMS: float = 250
    CALORIES: float = 1000
    PRICE: float = 5

    def __init__(self, name: str):
        super().__init__(name, Cake.PRICE, Cake.GRAMS, Cake.CALORIES)
