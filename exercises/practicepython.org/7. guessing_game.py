import random

playing_times = 0
winning_times = 0

print("Welcome to the Number Guessing Game! Type 'exit' to quit.\n")

while True:
    user_input = input("Guess a number between 1 and 9 (or type 'exit' to quit): ").strip().lower()

    if user_input == "exit":
        break  # Exit the game

    try:
        user_guess = int(user_input)
        if user_guess < 1 or user_guess > 9:
            print("❌ Please select a number between 1 and 9!")
            continue
    except ValueError:
        print("❌ Invalid input. Please enter a valid number or type 'exit' to quit.")
        continue

    # Generate a random number
    computer_guess = random.randint(1, 9)
    playing_times += 1

    if user_guess == computer_guess:
        winning_times += 1
        print("🎉 Congratulations! You guessed correctly.")
    elif user_guess < computer_guess:
        print("📉 Too low! Try again.")
    else:
        print("📈 Too high! Try again.")

# Final game summary
print("\n📊 Game Summary:")
print(f"🎮 Total games played: {playing_times}")
print(f"✅ Games won: {winning_times}")
print(f"❌ Games lost: {playing_times - winning_times}")
print("Thanks for playing! 🎉")
