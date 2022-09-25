def check_sufficient(coffee, materials):
    if coffee == "espresso":
        if (materials["water"]<50):
            print("Sorry there's not enough water.")
            return False
        if (materials["coffee"]<18):
            print("Sorry there's not enough coffee.")
            return False

    elif coffee == "latte":
        if (materials["water"]<200):
            print("Sorry there's not enough water.")
            return False
        if (materials["coffee"]<24):
            print("Sorry there's not enough coffee.")
            return False
        if (materials["milk"]<150):
            print("Sorry there's not enough milk.")
            return False

    elif coffee == "cappuccino":
        if (materials["water"]<250):
            print("Sorry there's not enough water.")
            return False
        if (materials["coffee"]<24):
            print("Sorry there's not enough coffee.")
            return False
        if (materials["milk"]<100):
            print("Sorry there's not enough milk.")
            return False

    return True


def print_report(materials):
    print(f"Water: {materials['water']}ml")
    print(f"Milk: {materials['milk']}ml")
    print(f"Coffee: {materials['coffee']}g")
    print(f"Money: ${materials['money']}")

def get_coins():
    print("Please insert coins.")
    penny = int(input("how many pennies?: "))
    dime = int(input("how many dimes?: "))
    nickle = int(input("how many nickles?: "))
    quarter = int(input("how many quarters?: "))
    return [penny, dime, nickle, quarter]

def process_coin(price, penny, dime, nickle, quarter):
    amount = penny * 0.01 + dime * 0.1 + nickle * 0.05 + quarter * 0.25

    if amount < price:
        print("Sorry that's not enough money. Money refunded")
        return False

    elif amount == price:
        return False

    else:
        change = amount - price
        print(f"Here is the ${round(change, 2)} dollars in change")
        return True

def make_coffee(coffee, materials):
    if coffee == "espresso":
       materials["water"] -= 50
       materials["coffee"] -= 18
       materials["money"] += 1.5

    elif coffee == "latte":
        materials["water"] -= 200
        materials["coffee"] -= 24
        materials["milk"] -= 150
        materials["money"] += 2.5

    elif coffee == "cappuccino":
        materials["water"] -= 250
        materials["coffee"] -= 24
        materials["milk"] -= 100
        materials["money"] += 3

    print(f"Here is your {coffee}. Enjoy!")

materials = {"water": 300, "milk": 200, "coffee": 100, "money": 0}
to_cont = True

coffeeOption = input("What would you like? (espresso/latte/cappuccino):")

while to_cont:
    if coffeeOption == "off":
        to_cont = False
        break

    elif coffeeOption == "report":
        print_report(materials)

    elif coffeeOption == "espresso":
        coins = get_coins()
        is_enough_money = process_coin(1.5,coins[0], coins[1], coins[2], coins[3])
        if (is_enough_money):
            is_sufficient_material = check_sufficient("espresso", materials)
            if (is_sufficient_material):
                make_coffee("espresso", materials)

    elif coffeeOption == "latte":
        coins = get_coins()
        is_enough_money = process_coin(2.5,coins[0], coins[1], coins[2], coins[3])
        if (is_enough_money):
            is_sufficient_material = check_sufficient("latte", materials)
            if (is_sufficient_material):
                make_coffee("latte", materials)


    elif coffeeOption == "cappuccino":
        coins = get_coins()
        is_enough_money = process_coin(3,coins[0], coins[1], coins[2], coins[3])
        if (is_enough_money):
            is_sufficient_material = check_sufficient("cappuccino", materials)
            if (is_sufficient_material):
                make_coffee("cappuccino", materials)

    coffeeOption = input("What would you like? (espresso/latte/cappuccino):")