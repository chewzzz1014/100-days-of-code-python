import random

def toss():
    random_int = random.randint(0, 1)
    if random_int == 0:
        print("Heads")
    else:
        print("Tails")


rounds = int(input("Enter number of rounds: "))
for _ in range(rounds):
    toss()