import timestamp_gen as gen
import baked_goods_repository as baked
import random

temp_customer_list = []
temp_drinks_list = []


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
cusomer_list = temp_customer_list
drinks_list = temp_drinks_list


def pull_random_list_item(x):
    result = x[random.randint(0, len(x) - 1)]
    return result


def generate_list_of_items():
    items = []
    for goods in range(random.randint(1, (len(baked.baked_list) - 1))):
        items.append(pull_random_list_item(baked.baked_list))
    for drink in range(random.randint(1, (len(drinks_list) - 1))):
        items.append(pull_random_list_item(drinks_list))

    return items


def get_total_cost(prices):
    total = 0.0
    for price in prices:
        total += price.sale_price
    return total


def create_transaction(count):
    items = generate_list_of_items()
    for i in range(count):
        purchases.append(
            Purchase(
                gen.timestamps[i],
                items,
                get_total_cost(items),
                pull_random_list_item(cusomer_list),
            )
        )
    return purchases


def delete_from_purchases(entry):
    purchases.pop(purchases.index(entry))
    return purchases


def update_purchases(target, updated_purchase):
    for target in purchases:
        i = purchases.index(target)
        purchases.pop(i)
        purchases.insert(i, updated_purchase)
    return purchases


print(create_transaction(20))
