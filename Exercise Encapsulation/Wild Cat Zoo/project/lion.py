from project.animal import Animal


class Lion(Animal):
    MONEY_FOR_CARE = 50

    def __init__(self, name, gender, age, money_for_care=50):
        super().__init__(name, gender, age, Lion.MONEY_FOR_CARE)