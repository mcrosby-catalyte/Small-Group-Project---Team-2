# Baked Good
# name
# purchasing cost
# markup percentage
# vendor name
# list of known allergens (ex. wheat, peanuts, milk)
# sale price (calculated from purchasing cost + markup percentage when created


class bakedGood:
    def __int__(
        self, name, purchasing_cost, markup_percentage, vendor_name, sale_price
    ):
        self.name = name
        self.name = markup_percentage
        self.purchasing_cost = purchasing_cost
        self.markup_percentage = vendor_name
        self.vedor_name = vendor_name

    def __str__(self):
        return f"{self.name}"


bread = bakedGood("bread", 5.50, 0.20, "shop")

print(bread)
