drink_menu = [
    {"drinkName": "Black Coffee", "markupPrice": 0.30},
    {"drinkName": "MNM Latte", "markupPrice": 0.20},
    {"drinkName": "Espresso", "markupPrice": 0.20},
    {"drinkName": "Hot Chocolate", "markupPrice": 0.20},
]


class Drinks:

    def __init__(self, name, ingredients, cost_to_produce, markup_percentage):
        self.name = name
        self.ingredients = ingredients
        self.produce_cost = cost_to_produce
        self.markup = markup_percentage

    def calculate_sale_price(self):
        sale_price = self.produce_cost + (self.produce_cost * 0.25)
