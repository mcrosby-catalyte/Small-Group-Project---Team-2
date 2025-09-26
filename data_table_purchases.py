import timestamp_gen as gen


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

    def __repr__(self):
        return f"{self.date_time}, {self.item_purchased}, {self.total_cost}, {self.customer}\n"


purchases = []


def create_transaction(count):
    for i in range(count):
        purchases.append(
            Purchase(gen.timestamps[i], "list of items", "total cost", "customer")
        )
    return purchases


print(create_transaction(4))
