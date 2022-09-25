import random
from logo import logo


# return random card
def return_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def print_current(user_cards, computer_cards):
    print(f"Your Cards: {user_cards}\nYour score: {sum(user_cards)}\nComputer's Cards: {computer_cards}\nComputer Score: {sum(computer_cards)}\n\n")

def computer_turn(user_cards, computer_cards, is_game_over):
    computer_score = sum(computer_cards)
    user_score = sum(user_cards)

    print("-----Computer turn-----")
    print_current(user_cards, computer_cards)

    while computer_score < 17:
        card = return_card()
        computer_cards.append(card)
        print("Computer got", card)
        computer_score = sum(computer_cards)
        print_current(user_cards, computer_cards)

    if ( computer_score == 21):
        print("Computer Wins with a Blackjack")

    elif computer_score > 21:
        print("Computer went over. User win")

    else:
        if user_score > computer_score:
            print("User wins")

        elif user_score < computer_score:
            print("User lose")

        elif user_score == computer_score:
            print("Draw")

    return True


def user_turn(user_cards, computer_cards, is_game_over):

        user_score = sum(user_cards)
        computer_score = sum(computer_cards)
        to_cont_user = True

        while to_cont_user:
            print("------Your turn-----")
            print_current(user_cards, computer_cards)

            if user_score == 21 or computer_score == 21:
                is_game_over = True
                if user_score == 21:
                    print("User Wins with a Blackjack")
                    to_cont_user = False
                else:
                    print("Computer Wins with a Blackjack")
                    to_cont_user = False

            elif user_score > 21:
                if (11 in user_cards and (user_score - 11 + 1) > 21) or (11 not in user_cards):
                    print("User went over. User lose")
                    is_game_over = True
                    to_cont_user = False
                elif (user_score - 11 + 1) < 21:
                    print("---Ace (11) is converted to 1 in your cardset---")
                    print_current(user_cards, computer_cards)
                    user_cards[user_cards.index(11)] = 1
                    user_score = user_score - 11 + 1
                elif (user_score - 11 + 1) == 21:
                    print("User Wins with a Blackjack")
                    is_game_over = True
                    to_cont_user = False

            if (to_cont_user):
                want_more_cards = input("Do you want to get another card? (y/n) ")
                if want_more_cards.lower() == "y":
                    card = return_card()
                    user_cards.append(card)
                    print("You got", card, "\n")
                    user_score = sum(user_cards)

                elif want_more_cards.lower() == "n":
                    print_current(user_cards, computer_cards)
                    to_cont_user = False

        return is_game_over

def main():
    to_repeat_game = True

    while(to_repeat_game):
        user_cards = [return_card(), return_card()]
        computer_cards = [return_card(), return_card()]

        is_game_over = False

        print(logo)
        is_game_over = user_turn(user_cards, computer_cards, is_game_over)
        if (not is_game_over):
            computer_turn(user_cards, computer_cards, is_game_over)

        get_to_repeat_game = input("Do you want to repeat the game? (y/n) ")
        if get_to_repeat_game == "y":
            to_repeat_game = True
        elif get_to_repeat_game == "n":
            to_repeat_game = False

main()




