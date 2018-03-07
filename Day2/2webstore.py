orders = [
  {
    'id': 'order_001',
    'item': 'Introduction to Python',
    'quantity': 1,
    'price_per_item': 32
  },
  {
    'id': 'order_002',
    'item': 'Advanced Python',
    'quantity': 3,
    'price_per_item': 40

  },
  {
    'id': 'order_003',
    'item': 'Python web frameworks',
    'quantity': 2,
    'price_per_item': 51
  }
]


def compute_totals_for(arg):
    totals = []
    for i in arg:
        total_price = i["quantity"] * i["price_per_item"]
        if total_price < 100:
            total_price += 10
        totals.append((i["id"], total_price))

    return totals


def compute_totals(arg):
    return list(map(lambda x:(x["id"], x["quantity"] * x["price_per_item"]) if x["quantity"] * x["price_per_item"] >= 100 else (x["id"], x["quantity"] * x["price_per_item"] + 10), arg))


print(compute_totals_for(orders))
print(compute_totals(orders))
