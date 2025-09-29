class DrinkName:
    def __init__(self, name, ingredients, markup_percentage):
        self.name = name
        self.ingredients = ingredients
        self.markup = markup_percentage
        self.cost_to_produce = self.calculate_cost_to_produce()
        self.sale_price = self.calculate_sale_price()

    def calculate_cost_to_produce(self):
        return sum(ingredient.purchasing_cost for ingredient in self.ingredients)

    def calculate_sale_price(self):
        return round(purchasing_cost * (1 + self.markup_percentage), 2)


black_coffee = DrinkName("black coffee", ["water", "coffee"], 0.30)
mnm_latee = DrinkName("MNM Latte", ["milk", "mnms"], 0.20)
capuccino = DrinkName("capuccino", ["espresso", "milk"], 0.25)
