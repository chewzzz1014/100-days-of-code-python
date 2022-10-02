class MoneyMachine:
    def __init__(self):
        self.profit = 0

    def report(self):
        print(f"Money: ${self.profit}")

    def make_payment(self, cost):
        coins = self.get_coins()
        return self.process_coin(cost, coins[0], coins[1], coins[2], coins[3])

    def get_coins(self):
        print("Please insert coins.")
        penny = int(input("how many pennies?: "))
        dime = int(input("how many dimes?: "))
        nickle = int(input("how many nickles?: "))
        quarter = int(input("how many quarters?: "))
        return [penny, dime, nickle, quarter]

    def process_coin(self, price, penny, dime, nickle, quarter):
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