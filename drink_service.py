from drink_repository import DrinkRepository


class DrinkService:
    def __init__(self):
        self.drinks = []

    def add_drink(self, drink):
        self.drinks.append(drink)

    def all_drinks(self):
        return self.drinks

    def find_drinks_by_name(self, name):
        for drink in self.drinks:
            if drink.name() == name:
                return drink
