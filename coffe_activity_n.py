# Baked Good
# name
# purchasing cost
# markup percentage
# vendor name
# list of known allergens (ex. wheat, peanuts, milk)
# sale price (calculated from purchasing cost + markup percentage when created


class bakedGood:
    def __intit__(
        self, name, purchasing_cost, markup_percentage, vendor_name, sale_price
    ):
        self.name = name
        self.name = markup_percentage
        self.purchasing_cost = purchasing_cost
        self.markup_percentage = vendor_name
        self.vedor_name = vendor_name
        self.sale_price = purchasing_cost + markup_percentage

    def __str__(self):
        return f"{self.purchasing_cost}"


cinnamon_rolls = bakedGood("bread", 5.50, 0.20, "shop")
muffin = bakedGood("bread", 5.50, 0.20, "shop")
cake = bakedGood("bread", 5.50, 0.20, "shop")
croissant = bakedGood("bread", 5.50, 0.20, "shop")
bread = bakedGood("bread", 5.50, 0.20, "shop")

print(croissant)
