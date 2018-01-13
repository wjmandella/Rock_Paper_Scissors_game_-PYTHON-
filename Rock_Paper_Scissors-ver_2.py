from random import randint
from time import sleep


player_name = input("Hello. What's your name? ").title()

print("\nHi, " + player_name + ". Let's play a game of 'Rock, Paper, Scissors'.")
print("\nThe rules are simple:")
sleep(1)
print("-Rock beats Scissors")
sleep(1)
print("-Paper beats Rock")
sleep(1)
print("-Scissors beats Rock\n")
sleep(1)
print("We will use the abbreviatons: 'R', 'P', and 'S'.")
sleep(1)
print("\nLet's get started!")
print("When prompted, input your choice: 'R', 'P', or 'S'.")
print("(Enter 'q' if you'd like to end the game.)")

active = True
computer_score = 0
player_score = 0
while active == True:
	#sleep(2)
	computer_choice = randint(1,3) # 1 = Rock, 2 = Paper, 3 = Scissors
	if computer_choice == 1:
		computer_choice = 'R'
	elif computer_choice == 2:
		computer_choice = 'P'
	else: computer_choice = 'S'
	
	player_choice = input("\nMake your choice ('R', 'P', or 'S'): ")
	player_choice = player_choice.upper()
	
	if player_choice == 'Q':
		print("\nThanks for playing!" +
		" Final score: Computer: {} and {}: {}".format(computer_score, player_name, player_score))
		active = False
	else:
		while (player_choice == 'R' or player_choice == 'S' or player_choice == 'P'):
			if player_choice == computer_choice:
				print("The result was a tie. You and the computer both chose " + computer_choice + ".")
			else:
				if (player_choice == 'R' and computer_choice == 'S') or (player_choice == 'P' and computer_choice == 'R') or (player_choice == 'S' and computer_choice == 'P'):
					print("\nYou won!" +
					"(You chose {} and the computer chose {}.)".format(player_choice, computer_choice))
					player_score += 1
				else:
					print("\nI'm sorry, but you lost." +
					"(You chose {} and the computer chose {}.)".format(player_choice, computer_choice))
					computer_score += 1
			print("\nThe score now is: Computer: {} and {}: {}".format(computer_score, player_name, player_score))
			break
		else:
			print("That was not a valid response. Please try again.")
