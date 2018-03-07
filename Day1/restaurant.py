class Dish(object):

    def __init__(self, dish_name, price, ingredients):
        self.dish_name = dish_name
        self.price = price
        self.ingredients = ingredients

    def cost(self):
        fixed_cost = 10
        sum_ingr = 0
        for i in self.ingredients:
            sum_ingr += i.cost
        return fixed_cost + sum_ingr

    def profit(self):
        return self.price - self.cost()


class Restaurant(object):

    def __init__(self, order_number = 0):
        self.order_number = order_number

    def order_dish(self, item, customer):
        self.order_number += 1
        self.item = item
        self.customer = customer
        customer[]
        print("Order #" + str(self.order_number) + ": " + item.name)

    def print_check(self, customer):
        print("Customer: " + customer['name'])


class Ingredients(object):

    def __init__(self, ingr, cost):
        self.ingr = ingr
        self.cost = cost


restaurant = Restaurant()

cheese = Ingredients('Cheese', 5)
pepperoni = Ingredients('Pepperoni', 5)
dough = Ingredients('Dough', 4)
lettuce = Ingredients('Lettuce', 2)
tomato = Ingredients('Tomato', 3)


pizza = Dish("Pizza", 35, [cheese, pepperoni, dough])
salad = Dish("Salad", 40, [lettuce, cheese, tomato])

pluto = {
    'name': 'Pluto',
    id: 1
}

goofy = {
    'name': 'Goofy',
    id: 2
}

donald = {
    'name': 'Donald',
    id: 3
}

restaurant.order_dish(pizza, goofy)
restaurant.order_dish(salad, pluto)
restaurant.order_dish(salad, goofy)
restaurant.order_dish(pizza, goofy)
restaurant.print_check(goofy)
restaurant.print_check(pluto)
restaurant.print_check(donald)
