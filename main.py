import random
import os
from art import *
from game_data import data


def get_choice():
    return random.choice(data)


def get_highest_follower(choice1, choice2):
    if choice1['follower_count'] > choice2['follower_count']:
        return 'A'
    elif choice1['follower_count'] < choice2['follower_count']:
        return 'B'


def compare_user_choice(user_input, higher_choice):
    if user_input == higher_choice:
        return True
    else:
        return False


def game():
    print(logo)
    streak = 0
    game_over = False
    while not game_over:
        choice_a = get_choice()
        choice_b = get_choice()
        highest_follower = get_highest_follower(choice1=choice_a, choice2=choice_b)
        message_a = f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}"
        message_b = f"Compare A: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}"

        # print(choice_a)
        print(message_a)
        print(vs)
        # print(choice_b)
        print(message_b)
        # print(highest_follower)
        user_choice = input("Who has more followers? Type 'A' or 'B':").upper()

        if compare_user_choice(user_input=user_choice, higher_choice=highest_follower):
            streak += 1
            print(f"You're right! Current Score: {streak}")
        else:
            streak = 0
            game_over = True
            print("Game Over: Your last guess was incorrect.")

    play_again = input("Would you like to play again? Type'y' or 'n': ").lower()
    if play_again == 'y':
        os.system("clear")
        game()


game()

