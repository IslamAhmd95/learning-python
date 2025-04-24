def play_again(player_name):
    play_again = input(f"{player_name}, Do you want to play again? (yes/no): ").strip().lower()
    if play_again == 'yes':
        return True
    return False 

def initialize_stats():
    return {"playing_times": 0, "winning_times": 0, "losing_times": 0}


def print_summary(game, player_stats):

    summary = f"Game {game} Summary: Played {player_stats['playing_times']} times | Wins: {player_stats['winning_times']} | Losses: {player_stats['losing_times']}"

    if game == "Rock-Paper-Scissors":
        summary += f" | Ties: {player_stats['playing_times'] - (player_stats['winning_times'] + player_stats['losing_times'])}"

    print(summary)

def rps_winner(stats, player_choice, computer_choice):

    winning_situations = {
        "Rock": "Scissors",
        "Paper": "Rock",
        "Scissors": "Paper"
    }

    if player_choice == computer_choice:
        print('it\'s a Tie')
    elif (computer_choice == winning_situations[player_choice]):
        stats["winning_times"] += 1
        print('You win!')
    else:
        stats["losing_times"] += 1
        print('You lose!')

def guess_number_winner(stats, player_guess, computer_guess):
    if player_guess == computer_guess:
        stats["winning_times"] += 1
        print("Correct guess")
    else:
        stats["losing_times"] += 1
        print("Wrong! Computer guess was " + str(computer_guess))