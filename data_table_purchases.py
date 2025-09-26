import timestamp_gen as gen
import baked_goods_repository as baked
import random


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


def pull_random_list_item(x):
    result = x[random.randint(0, len(x) - 1)]
    return result


def generate_list_of_items():
    items = []
    for i in range(random.randint(1, (len(baked.baked_list) - 1))):
        items.append(pull_random_list_item(baked.baked_list))

    return items


def create_transaction(count):
    items = generate_list_of_items()
    for i in range(count):
        purchases.append(Purchase(gen.timestamps[i], items, "total cost", "customer"))
    return purchases


def create_new_purchace():
    purchases.append(Purchase("date/time", "items", "cost", "customer"))
    return purchases


def delete_from_purchases():
    purchases.pop()
    return purchases


def update_purchases(target, updated_purchase):
    for target in purchases:
        i = purchases.index(target)
        purchases.pop(i)
        purchases.insert(i, updated_purchase)
    return purchases


print(create_transaction(20))
