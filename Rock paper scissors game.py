import random

# Define options for the game
options = ["Rock", "Paper", "Scissors"]

def determine_winner(user_choice, computer_choice):
  """Compares user choice and computer choice to determine winner"""
  # Tie condition
  if user_choice == computer_choice:
    return "Tie"

  # Winning conditions based on user choice
  elif user_choice == "Rock":
    if computer_choice == "Scissors":
      return "Win"
    else:
      return "Lose"
  elif user_choice == "Paper":
    if computer_choice == "Rock":
      return "Win"
    else:
      return "Lose"
  elif user_choice == "Scissors":
    if computer_choice == "Paper":
      return "Win"
    else:
      return "Lose"
  else:
    return "Invalid Input"  # Handle unexpected user input

def play_game():
  """Main function to play the Rock-Paper-Scissors game"""
  user_choice = input("Choose Rock, Paper, or Scissors: ").capitalize()
  computer_choice = random.choice(options)
  print(f"You chose: {user_choice}")
  print(f"Computer chose: {computer_choice}")

  result = determine_winner(user_choice, computer_choice)
  if result == "Tie":
    print("It's a tie!")
  elif result == "Win":
    print("You win!")
  else:
    print("You lose!")

  # Ask user if they want to play again
  play_again = input("Play again? (y/n): ").lower()
  if play_again == 'y':
    play_game()
  else:
    print("Thanks for playing!")

# Start the game
play_game()
