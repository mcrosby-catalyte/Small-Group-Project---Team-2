class Drinks:

    def __init__(self, name, ingredients, cost_to_produce, markup_percentage):
        self.name = name
        self.ingredients = ingredients
        self.produce_cost = cost_to_produce
        self.markup = markup_percentage

    def calculate_sale_price(self):
        sale_price = purchasing_cost + (
            purchasing_cost * drink_menu["markupPercentage"]
        )
