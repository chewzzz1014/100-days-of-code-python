from menu_item import MenuItem

class CoffeeMaker:
    def __init__(self):
        self.water = 300
        self.milk = 200
        self.coffee = 100
        self.money = 0

    def report(self):
        print(f"Water: {self.water}ml")
        print(f"Milk: {self.milk}ml")
        print(f"Coffee: {self.coffee}g")
        if self.money > 0:
            print(f"Money: ${self.money}")

    def is_resource_sufficient(self, drink):
        if self.water < drink.ingredients["water"]:
            print("Sorry there's no enough water.")
            return False
        elif self.milk < drink.ingredients["milk"]:
            print("Sorry there's no enough milk.")
            return False
        elif self.coffee < drink.ingredients["coffee"]:
            print("Sorry there's no enough coffee.")
            return False
        else:
            return True

    def make_coffee(self, order):
        self.water -= order.ingredients["water"]
        self.milk -= order.ingredients["milk"]
        self.coffee -= order.ingredients["coffee"]
        self.money += order.cost
        print(f"Here's your {order.name}. Enjoy!")