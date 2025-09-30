class ingredient:
    """Represents an ingredient in a coffee/tea shop."""

    def __init__(self, name, purchasing_cost, unit_amount, unit_of_measure):
        self.name = name
        self.purchasing_cost = purchasing_cost
        self.unit_amount = unit_amount
        self.unit_of_measure = unit_of_measure

    def __repr__(self):
        return (f"Ingredient(name='{self.name}', cost={self.purchasing_cost}, "
                f"unit_amount={self.unit_amount}, unit='{self.unit_of_measure}')")

    def cost_per_unit(self):
        """Returns the cost per unit amount."""
        return self.purchasing_cost / self.unit_amount


class Inventory:
    """Manages a collection of ingredients."""

    def __init__(self):
        self.ingredients = []

    def add_ingredient(self, ingredient):
        """Add a new ingredient to the inventory."""
        self.ingredients.append(ingredient)

    def list_ingredients(self):
        """List all ingredients in the inventory."""
        return self.ingredients

    def find_ingredient(self, name):
        """Find an ingredient by name (case-insensitive)."""
        for ing in self.ingredients:
            if ing.name.lower() == name.lower():
                return ing
        return None


# __________Example Setup

inventory = Inventory()

# coffee ingredients
inventory.add_ingredient(ingredient("Coffee beans (espresso roast)", 15, 1, "lb"))
inventory.add_ingredient(ingredient("Whole milk", 4, 1, "gallon"))
inventory.add_ingredient(ingredient("Oat milk", 5, 1, "quart"))
inventory.add_ingredient(ingredient("Pumpkin puree (fall seasonal)", 4, 15, "oz"))

# tea ingredients
inventory.add_ingredient(ingredient("Black tea leaves (English Breakfast)", 9, 1, "lb"))
inventory.add_ingredient(ingredient("Green tea leaves (Sencha)", 11, 1, "lb"))
inventory.add_ingredient(ingredient("Chai tea concentrate (spiced)", 8, 32, "oz"))
inventory.add_ingredient(ingredient("Matcha powder", 18, 100, "g"))
inventory.add_ingredient(ingredient("Apple cider (fall seasonal)", 6, 64, "oz"))


#________Example Usage 
print("All Ingredients:")
for ing in inventory.list_ingredients():
    print(ing)

print("\nSearch Example:")
found = inventory.find_ingredient("Matcha powder")
if found:
    print(f"Found: {found} | Cost per {found.unit_of_measure}: ${found.cost_per_unit():.2f}")
