import random

def play_game():
    print("Welcome to the last assignment of the term, Rock, Paper, Scissors!")
    choices = ["rock", "paper", "scissors"]

    while True:
        player_choice = input("Make your choice  (rock, paper, scissors): ").lower()
        if player_choice not in choices:
            print("Not a valid choice! choose any of the following rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "scissors" and computer_choice == "paper") or \
             (player_choice == "paper" and computer_choice == "rock"):
            print("You Toke the victory HOME!")
        else:
            print("TRY AGAIN, YOU GOT THIS!")

        play_again = input("Do you feel you have another round in you? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

play_game()
