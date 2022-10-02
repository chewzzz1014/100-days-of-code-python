from menu_item import MenuItem

class Menu:
    def get_items(self):
        return "latte/espresso/cappuccino"

    def find_drink(self, order_name):
        if order_name in ["latte", "espresso", "cappuccino"]:
            return MenuItem(order_name)
        else:
            return None

