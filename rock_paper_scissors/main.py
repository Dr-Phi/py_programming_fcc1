import random

def main():
  input("Welcome to my first RPS game.\npress Enter")
  choices = get_choices()
  result = check_win(choices["player"], choices["computer"])


def get_choices(): # Function with no parameters
  options = ["rock", "paper", "scissors"]
  player_choice = input("Write your choice (rock, paper, scissors): ")
  computer_choice = random.choice(options)
  choices = {
  "player": player_choice,
  "computer": computer_choice
  }
  return choices

def check_win(player, computer): # Function with 2 parameters
  print(f"You chose {player}, computer chose {computer}")
  if player == computer:
    print("It's a tie!")
  elif player == "scissors" and computer == "rock":
    print("Computer wins.")
  elif player == "scissors" and computer == "paper":
    print("Player wins!")
  elif player == "rock": # 1st refactor of code using nested if/elif
    if computer == "scissors":
      print("Player wins!")
    elif computer == "paper":
      print("Computer wins.")
  elif player == "paper": # 2nd refactor of code using nested if/else
    if computer == "rock":
      print("Player wins")
    else:
      print("Computer wins.")
  else:
    print("Write a valid choice")


if __name__ == "__main__":
  main()
  