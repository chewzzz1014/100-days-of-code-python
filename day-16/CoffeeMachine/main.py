from menu import Menu
from menu_item import MenuItem
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker

to_cont = True


menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

customer_order = input(f"What would you like? ({menu.get_items()}) ").lower()
print()

while to_cont:

    if customer_order == "off":
        to_cont = False
    elif customer_order == "report":
        coffeeMaker.report()
    elif menu.find_drink(customer_order):
        menuItem = MenuItem(customer_order)
        if coffeeMaker.is_resource_sufficient(menuItem) and moneyMachine.make_payment(menuItem.cost):
            coffeeMaker.make_coffee(menuItem)

    get_to_cont = input("Would you like to continue? (y/n) ").strip().lower()
    if get_to_cont == "n":
        to_cont = False
        break

    customer_order = input(f"What would you like? ({menu.get_items()}) ").lower()
    print()
