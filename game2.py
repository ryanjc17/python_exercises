from sys import exit
#Welcome to a choice game centered around functions

input_ = "> "


def start():
	print(f"Welcome to the start of your adventure {pname}!")
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


	
	
print("Please enter your name adventurer:")
pname = input(input_)

start()

