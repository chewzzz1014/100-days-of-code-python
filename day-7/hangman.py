# create a hangman game
import random
import hangman_figures as hf
import hangman_wordlist as hw


end_of_game = False
stages = hf.stages
word_list = hw.word_list
guessed = []
chosen_word = random.choice(word_list)
print(f'Pssst, the solution is {chosen_word}.')

print(hf.logo)
lives = 6
display = []
for _ in range(len(chosen_word)):
    display.append("_")


def check_in_chosen_word(guess, chosen_word):
    for idx in range(len(chosen_word)):
        if chosen_word[idx]==guess:
            display[idx] = guess

def check_lives(lives, guess, chosen_word, end_game):
    if guess not in chosen_word:
        print(f"{guess} not in the word.")
        lives -= 1
        # out of lives
        if lives == 0:
            end_of_game = True
            print("You lose")
    return lives, end_game

def win_game(end_of_game):
    if "_" not in display:
        end_of_game = True
        print("You win")
    return end_of_game

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in guessed:
        print(f"You've enter {guess}. Enter another character.")
    else:
        guessed.append(guess)
        # is the letter in the chosen word?
        check_in_chosen_word(guess, chosen_word)
        # lives = 0?
        (lives, end_of_game) = check_lives(lives, guess, chosen_word,end_of_game)
        # guessed all words?
        end_of_game = win_game(end_of_game)
        print(" ".join(display))
        print(stages[lives])














