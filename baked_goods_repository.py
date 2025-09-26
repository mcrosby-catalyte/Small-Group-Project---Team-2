# Baked Good
# name
# purchasing cost
# markup percentage
# vendor name
# list of known allergens (ex. wheat, peanuts, milk)
# sale price (calculated from purchasing cost + markup percentage when created


class bakedGood:
    def __init__(
        self,
        name,
        purchasing_cost,
        markup_percentage,
        vendor_name,
        allergens,
    ):
        self.name = name
        self.markup_percentage = markup_percentage
        self.purchasing_cost = purchasing_cost
        self.vedor_name = vendor_name
        self.sale_price = round(purchasing_cost * (1 + markup_percentage))
        self.allergens = allergens

    def __str__(self):
        return f"{self.name} {self.sale_price} {self.allergens}"


cinnamon_rolls = bakedGood("bread", 5.50, 0.20, "shop")
muffin = bakedGood(
    "bread",
    5.50,
    0.20,
    "shop",
)
cake = bakedGood(
    "bread",
    5.50,
    0.20,
    "shop",
)
croissant = bakedGood(
    "bread",
    5.50,
    0.0,
    "shop",
)
bread = bakedGood(
    "bread",
    5.50,
    0.20,
    "shop",
)

baked_list = [cinnamon_rolls, muffin, cake, croissant, bread]
