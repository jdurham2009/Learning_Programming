#Randomized rock paper scissors game
import random
computer_choice = random.choice(["rock", "paper", "scissors"])
user_choice = input("Do you want to choose rock, paper, or scissors ")

print("Computer choice:", computer_choice)

if computer_choice == user_choice:
    print("TIE")
elif user_choice == "rock" and computer_choice == "scissors":
    print("WIN")
elif user_choice == "paper" and computer_choice == "rock":
    print("WIN")
elif user_choice == "scissors" and computer_choice == "paper":
    print("WIN")
else:
    print("You lose, computer wins :)")