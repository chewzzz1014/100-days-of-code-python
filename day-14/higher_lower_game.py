from data import data
from logo import logo
from logo import vs
import random
import os

clear = lambda: os.system('cls')

to_cont = True
score = 0
previous_is_correct = False
round = 0

while to_cont:
    a = random.randint(0, len(data)-1)
    b = random.randint(0, len(data)-1)

    while a == b:
        a = random.randint(0, len(data)-1)

    a_item = data[a]
    b_item = data[b]

    more_followers_ans = 'A'

    print(logo)
    # previous's result
    if round>0 and previous_is_correct:
        print(f"You're right! Current score: {score}")
    elif round>0 and not previous_is_correct:
        print(f"Sorry, that's wrong. Final score: {score}")
        to_cont = False
        break

    previous_is_correct = False
    round += 1
    print(f"Compare A: {a_item['name']}, a {a_item['description']} from {a_item['country']}.")
    print(vs)
    print(f"Compare B: {b_item['name']}, a {b_item['description']} from {b_item['country']}.")

    if a_item["follower_count"] >= b_item["follower_count"]:
        more_followers_ans = 'A'
    elif a_item["follower_count"] < b_item["follower_count"]:
        more_followers_ans = 'B'

    more_followers_guessed = input("Who has more followers? Type 'A' or 'B': ")

    print(f"A: {a_item['follower_count']}")
    print(f"B: {b_item['follower_count']}")
    if more_followers_guessed.upper() == more_followers_ans:
        score += 1
        previous_is_correct = True

    clear()







