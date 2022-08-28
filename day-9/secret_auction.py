import os
from auction_logo import logo


to_cont = True
bids = {}

def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")


while to_cont:
    print(logo)
    print("Welcome to the secret auction program.")
    name = input("What is your name?: ")
    bid = float(input("What's your bid?: RM"))
    bids[name] = bid

    get_to_cont = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if "n" in get_to_cont:
        to_cont = False
    clear_screen()

max = -1
max_bidder = ""
for k, v in bids.items():
    if v>max:
        max = bids[k]
        max_bidder = k

print(f"The winner is{max_bidder} with a bid of RM{round(max, 2)}")



