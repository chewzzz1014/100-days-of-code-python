class MenuItem:
    def __init__(self, name):
        self.name = name
        self.cost = self.get_cost()
        self.ingredients = self.get_ingredients()


    def get_cost(self):
        if self.name == "espresso":
            return 1.5
        elif self.name == "latte":
            return 2.5
        elif self.name == "cappuccino":
            return 3

    def get_ingredients(self):
        if self.name == "espresso":
            return {"water": 50, "milk": 0, "coffee": 18}
        elif self.name == "latte":
            return {"water": 200, "milk": 150, "coffee": 24}
        elif self.name == "cappuccino":
            return {"water": 250, "milk": 100, "coffee": 24}