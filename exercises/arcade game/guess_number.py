import random
from functions import *

def play_guess_number(player_name, stats):

    def start_game():

        while True:

            try:
                player_guess = int(input(f"\n{player_name}, please guess an integer number between 1 and 5: "))
            except ValueError:
                print("Invalid input. Please enter an integer number.")
                continue

            if player_guess not in range(1, 6):
                print("Invalid guess, choose a number between 1 and 5")
                continue

            stats["playing_times"] += 1
            computer_guess = random.randint(1, 5)

            guess_number_winner(stats, player_guess, computer_guess)

            if play_again(player_name):
                continue

            return stats

    return start_game


if __name__ == '__main__':

    stats = initialize_stats()
    player_name = input("Please enter your name: ").strip().capitalize()
    start_game = play_guess_number(player_name, stats)
    print_summary("Guess the Number", start_game())