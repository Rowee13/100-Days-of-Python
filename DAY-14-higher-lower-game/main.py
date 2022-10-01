# ##### HIGHER LOWER GAME #####
# ##### using different instagram accounts and the number of follower each account have #####

import random
from replit import clear
from art import logo, vs
from game_data import data


def get_random_account():
    """generate random account from the game data"""
    return random.choice(data)


def format_data(account):
    """format data into printable format from dictionary"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"f{name}, a {description}, from {country}"


def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess and return if it's true"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(logo)
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    # account_b outside the while loop to generate account every rounds
    account_b = get_random_account()

    while game_should_continue:
        # make the account_b transfer data to account_a after every rounds
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        guess = input("WHo has more followers? Type 'A' or 'B': ").lower()

        # checking of followers value vs the two given accounts
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        clear()
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score is {score}.")


game()
