from game_data import data
import random

def get_random_account():
    """Get data from random account"""
    return random.choice(data)

def format_data(accounts):
    """Format account into printable format: name, description and country"""
    name = accounts["name"]
    description = accounts["description"]
    country = accounts["country"]
    return f"{name}, a {description}, from {country}"


def check_answer(guess, a_followers, b_followers):
    """Check followers against user's guess and returns True If they got iit right or False if they got it wrong."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()
        
        while account_a == account_b:
            account_b = get_random_account()
            print(f"Compare A: {format_data(account_a)}.")
            print("vs")
            print(f"Against B: {format_data(account_b)}.")
            
            guess = input("Who has more followers? Type 'A' or 'B': ").lower()
            a_follower_count = account_a["follower_count"]
            b_follower_count = account_b["follower_count"]
            is_correct = check_answer(guess, a_follower_count, b_follower_count)
            if is_correct:
                score += 1
                print(f"You're right! Current Score: {score}.")
            else:
                game_should_continue = False
                print(f"Sorry, that's wrong. Final Score: {score}")
game()
    
