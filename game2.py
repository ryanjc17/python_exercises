from sys import exit
#Welcome to a choice game centered around functions

input_ = "> "


def start():
	print("You find yourself in the middle of the forrest.\nWhich direction would you like to go? (N,S,E,W)")
	choice = input(input_)
	if choice == 'n':
		bear_cave()
	elif choice == 's':
		spider_cave()
	elif choice == 'e':
		forest_e()
	elif choice == 'w':
		forest_w()

def bear_cave():
	print("You find yourself in a cave inhabited by a bear.\nThe bear seems angry.")
	print("What do you do?")
	choice = input(input_)
	if "fight" in choice:
		dead("The bear rightfully fucked you up.")
	elif "flee" in choice:
		print("You find yourself back in the area you first started in.")
		start()
	elif "taunt" in choice:
		print("The bear stands on its hind legs.")
		print("What do you do next?")
		choice_ = input(input_)
		if "pet" in choice_:
			print("The bear lays on it back and growls.\nIt appears it wants a belly rub.")
			print("You pet the bear and leave the cave, dropping you back in the area where you first started.")
			start()
	else:
		dead("The bear mawls you and treats you as his dinner.")

def spider_cave():
	print("You find yourself in a cave inhabited by spiders!\nAll the spiders seem to be sleeping.\nWhat do you do?")
	choice = input(input_)
	if "scream" in choice:
		dead("You woke all the spiders, moron.\nThey wrap you in their web and throw you in the corner.")
	elif "sing" in choice:
		print("The spiders wake but start dancing.\nYou take this opportunity to exit the cave and return to the forest.")
		start()
	elif "nothing" in choice:
		dead("Although you did nothing, you created too much noise entering the cave.\nThe spiders wrap you in their web and throw you in the corner.")
	else:
		dead("The spiders wrap you in their web.")

def forest_e():
	print("You find yourself deeper in the forest.")
	print("The trees start making noise.")
	print("What do you do?")
	choice = input(input_)
	if "scream" in choice:
		print("The ground starts to shake.")
		print("The trees turn into ents and surround you.")
		dead("What a shameful way to die.")
	elif "nothing" in choice:
		print("You think it may be better to head back to where you started.")
		start()
	elif "torch" in choice:
		print("You torch the forest.")
		print("I mean there were better ways to handle this but I guess it works.")
		print("You make your way back to where you started.")
		start()
	else:
		dead("I don't know what you mean. Anyway, the trees just killed you.")

def forest_w():
	print("You find yourself in a forest that looks as if it is opening up. Which direction do you go? (N/S/E/W)")
	choice = input(input_)
	if choice == 'n':
		bear_cave()
	elif choice == 's':
		spider_cave()
	elif choice == 'e':
		start()
	elif choice == 'w':
		complete()

def complete():
	print("Congratulations, you made it out of the forest!")
	print("Thanks for playing!")

def dead():
	print(why, "Good job!")
	exit(0)
	
print("Please enter your name adventurer:")
pname = input(input_)
print(f"Welcome to the start of your adventure {pname}!")

start()

