#Rock, paper or scissors game
import random
 
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)
 
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
 
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
 
    return "You lose!"
 
def play_game():
    print("Welcome to Rock-Paper-Scissors Game!")
    print("Instructions: Choose Rock/Paper/Scissors")
 
    user_score = 0
    computer_score = 0
 
    while True:
        # Get user choice
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
 
        # Validate user input
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid input! Only 'rock', 'paper', or 'scissors' are allowed")
            continue
 
        # Get computer's random choice
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
 
        # Determine the winner and update scores
        result = determine_winner(user_choice, computer_choice)
        print(result)
 
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
 
        # Display scores
        print(f"Your score: {user_score} | Computer's score: {computer_score}")
 
        # Ask if the user wants to play another round
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break
 
# Start the game
play_game()
