class bakedGood:
    """
    Gives attributes to food items.
    Returns:
        Food name price and allergen.
    """

    def __init__(
        self,
        name,
        purchasing_cost,
        markup_percentage,
        vendor_name,
        sale_price,
        allergens,
    ):
        self.name = name
        self.markup_percentage = markup_percentage
        self.purchasing_cost = purchasing_cost
        self.vedor_name = vendor_name
        self.sale_price = self.calculate_sale_price()
        self.allergens = allergens

    def calculate_sale_price(self):
        return round(self.purchasing_cost * (1 + self.markup_percentage), 2)

    def __str__(self):
        return f"\n{self.name}\nsale price: {self.sale_price}\nallergen: {self.allergens}\n\n"


cinnamon_roll = bakedGood("Cinnamon roll", 5.50, 0.20, "shop", 10, "wheat")
muffin = bakedGood("Muffin", 5.50, 0.20, "shop", 5, "wheat")
coffee_cake = bakedGood("Coffe Cake", 5.50, 0.20, "shop", 5, "wheat")
croissant = bakedGood("croissant", 5.50, 0.20, "shop", 5, "wheat")
bread = bakedGood("bread", 5.50, 0.20, "shop", 5, "wheat")

baked_list = [cinnamon_roll, muffin, coffee_cake, croissant, bread]

allergens_list = [
    "milk",
    "eggs",
    "wheat",
    "soy",
    "peanuts",
    "tree nuts",
    "fish",
    "shellfish",
    "sesame",
]
