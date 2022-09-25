from logo import logo
import random

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5


def get_num_attempts(str):
    if str.lower() == "easy":
        return EASY_ATTEMPTS
    elif str.lower() == "hard":
        return HARD_ATTEMPTS

def main():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    target = random.randint(1, 101)
    attempts_left = get_num_attempts(level)

    while attempts_left >= 1:
        print(f"You have {attempts_left} attempts remaining to guess the number.")
        guessed = int(input("Make a guess: "))
        attempts_left -= 1

        if guessed > target:
            print("Too High.")
        elif guessed < target:
            print("Too Low.")
        else:
            print(f"You got it! The answer was {target}.")
            break

        if guessed!=target and attempts_left == 0:
            print("You've run out of guesses, you lose.")
            break

        elif guessed!=target and attempts_left >= 1:
            print("Guess again.")


main()