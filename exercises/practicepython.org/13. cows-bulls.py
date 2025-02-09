"""
reate a program that will play the “cows and bulls” game with the user. The game works like this:

Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout the game and tell the user at the end
"""

import random

def number_to_list(number):
    return [int(digit) for digit in str(number)]

def play_game(computer_guess, user_guess):
    cows = 0
    bulls = 0
    computer_guess_list = number_to_list(computer_guess)
    user_guess_list = number_to_list(user_guess)

    for i in range(4):
        if computer_guess_list[i] == user_guess_list[i]:
            cows += 1

    bulls = sum(min(computer_guess_list.count(d), user_guess_list.count(d)) for d in set(user_guess_list)) - cows

    return cows, bulls


computer_guess = random.randint(1000, 9999)

while True:

    try:
        user_guess = input("\nEnter your guess number (number must contain 4 digits) or type 'exit' to quit the game:").strip()

        if user_guess.lower() == 'exit':
            print("Game has been terminated.")
            break

        if len(user_guess)!= 4 or not user_guess.isdigit():
            raise ValueError
    
    except ValueError:
        print("Invalid input! Please enter a 4-digit number.")
        continue


    user_guess = int(user_guess)
    cows, bulls = play_game(computer_guess, user_guess)
    print(f"Computer's guess: {computer_guess}")
    print(f"User's guess: {user_guess}")
    print(f"Cows: {cows}")
    print(f"Bulls: {bulls}")

    if cows == 4:
        print("Congratulations! You've guessed the correct number.")
        break


