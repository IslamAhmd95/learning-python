import random
from functions import *

def play_rps(player_name, stats):

    choices = ["Rock", "Paper", "Scissors"]
           
    def start_game():

        while True:

            player_choice = input(f"\n{player_name}, please choose one of the following({", ".join(choices)}): ").strip().capitalize()

            if player_choice not in choices:
                print("Invalid choice, try again.")
                continue

            stats["playing_times"] += 1
            computer_choice = random.choice(choices)

            print(f"{player_name}, You chose {player_choice} while computer chose {computer_choice}")

            rps_winner(stats, player_choice, computer_choice)

            if play_again(player_name):
                continue

            return stats

    return start_game


if __name__ == "__main__":

    stats = {"playing_times":0, "winning_times":0, "lost_times":0}
    player_name = input("Please enter your name: ").strip().capitalize()
    rps_stats = initialize_stats()
    start_game = play_rps(player_name, rps_stats)
    print_summary("Rock-Paper-Scissors", start_game())