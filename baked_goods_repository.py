# Baked Good
# name
# purchasing cost
# markup percentage
# vendor name
# list of known allergens (ex. wheat, peanuts, milk)
# sale price (calculated from purchasing cost + markup percentage when created


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
        self.sale_price = sale_price
        self.allergens = allergens

    def __str__(self):
        return f"{self.name}\nsale price: {self.sale_price}\nallergen: {self.allergens}"


cinnamon_roll = bakedGood("Cinnamon roll", 5.50, 0.20, "shop", 10, "wheat")
muffin = bakedGood("Muffin", 5.50, 0.20, "shop", 5, "wheat")
coffee_cake = bakedGood("Coffe Cake", 5.50, 0.20, "shop", 5, "wheat")
croissant = bakedGood("croissant", 5.50, 0.20, "shop", 5, "wheat")
bread = bakedGood("bread", 5.50, 0.20, "shop", 5, "wheat")


baked_list = [cinnamon_roll, muffin, coffee_cake, croissant, bread]

print(coffee_cake)
