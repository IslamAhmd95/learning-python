import argparse
import sys
from rps import play_rps
from guess_number import play_guess_number
from functions import *

class CustomArgparser(argparse.ArgumentParser):
    def error(self, message):
        sys.exit("Please provide a name as an argument\nUsage: python3 main.py --name <name>")


def define_game(player_name, rps_stats, guess_stats):

    def start_playing():

        nonlocal player_name
        nonlocal rps_stats
        nonlocal guess_stats

        while True:

            player_choice = input(f"\n{player_name}, please enter 1 or 2 to choose a game .\n\nPlease choose a game:\n1 = Rock Paper Scissors\n2 = Guess My Number\n\nOr press 'x' to exit the arcade\n\n")

            if not player_choice in ['1', '2']:
                print(f"\nThank you for playing!, {player_name}")
                print_summary("Rock-Paper-Scissors", rps_stats)
                print_summary("Guess the Number", guess_stats)
                sys.exit(f"By {player_name}")

            if int(player_choice) == 1:
                start_game = play_rps(player_name, rps_stats)
                rps_stats = start_game()
            elif int(player_choice) == 2:
                start_game = play_guess_number(player_name, guess_stats)
                guess_stats = start_game()

    return start_playing


if __name__ == "__main__":

    parser = CustomArgparser(description="Arcade game")
    parser.add_argument("-n", "--name", metavar="player's name", required=True, type=str, help="Please Enter the player's name")
    args = parser.parse_args()
    player_name = args.name.strip().capitalize()
    print(f"\nHello {player_name}! Welcome to the Arcade Game. ")

    rps_stats = initialize_stats()
    guess_stats = initialize_stats()

    play = define_game(player_name, rps_stats, guess_stats)
    play()