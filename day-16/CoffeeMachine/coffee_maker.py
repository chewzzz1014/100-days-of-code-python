from menu_item import MenuItem

class CoffeeMake:
    def __init__(self):
        self.water = 300
        self.milk = 200
        self.coffee = 100
        self.money = 0

    def report(self):
        print(f"Water: {self.water}ml")
        print(f"Milk: {self.milk}ml")
        print(f"Coffee: {self.coffee}g")
        print(f"Money: ${self.money}")

    def is_resource_sufficient(self, drink):
        return self.water > drink.ingredients["water"] and self.milk > drink.ingredients["milk"] and self.coffee > drink.ingredients["coffee"]

    def make_coffee(self, order):
        self.water -= order.ingredients["water"]
        self.milk -= order.ingredients["milk"]
        self.coffee -= order.ingredients["coffee"]
        self.money += order.cost