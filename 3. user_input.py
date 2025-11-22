import random

choices = ['Rock', 'Paper','Scissors']
while True:
    while True:
        player_choice = input('\nEnter your choice: ').strip().capitalize()
        if player_choice in choices:
            break
        else:
            print('Your choice must be one of the following: ' + ", ".join(choices))

    computer_choice = random.choice(choices)

    print('You chose:', player_choice)
    print('Computer chose:', computer_choice)

    if player_choice == computer_choice:
        print('it\'s a Tie')
    elif (player_choice == 'Rock' and computer_choice == 'Scissors'):
        print('You win!')
    elif (player_choice == 'Scissors' and computer_choice == 'Paper'):
        print('You win!')
    elif (player_choice == 'Paper' and computer_choice == 'Rock'):
        print('You win!')
    else:
        print('You lose!')

    play_again = input('Do you want to play again? (yes/no)').strip().lower()
    if play_again != 'yes':
        print('Thanks for playing!')
        break