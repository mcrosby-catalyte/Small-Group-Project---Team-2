class Purchase:

    def __init__(
        self,
        date_time,
        item_purchased,
        total_cost,
        customer,
    ):
        self.date_time = date_time
        self.item_purchased = item_purchased
        self.total_cost = total_cost
        self.customer = customer

    def __str__(self):
        return f"{self.date_time}, {self.item_purchased}, {self.total_cost}, {self.customer}"
