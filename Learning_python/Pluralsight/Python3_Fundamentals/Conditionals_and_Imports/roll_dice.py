#Ramdomized roll for 6 sided dice
import random
roll = random.randint(1,6)
guess = int(input( "Guess the dice roll:\n"))
if guess == roll:
    print("Correct! They rolled a " + str(roll))
else:
    print("Wrong they rolled a " + str(roll))