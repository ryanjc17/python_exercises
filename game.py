import random

#randomized for loops integrated within a choose your own destiny game
#Welcome to Midieval Times! Or something like that.

input_ = '> '
input__ = 'Att/Def> '

#player set up
phealth = 0
pstrength = 0
pagility = 0
pintellect = 0

#enemy list
enemies = [
["Rat", 10, 5],
["Pigeon", 15, 3],
["Cat", 20, 5],
["Dog", 25, 6],
["Pig", 30, 7],
["Heffer", 45, 4],
["Camel", 60, 7],
["Elephant", 85, 12],
["Rhino", 95, 20],
["Giraffe", 110, 15],
["BOSS: Dragon", 250, 20]
]

#Character Stats Generation
while True:
	print("Randomize Stats? (y/n)")
	n = input(input_)
	if n == 'y':
		phealth = random.randint(0, 25)
		pattack = random.randint(1, 4)
		pstrength = random.randint(0, 10)
		pagility = random.randint(0, 10)
		pintellect = random.randint(0, 10)
		print(f"Health: {phealth}")
		print(f"Strength: {pstrength}")
		print(f"Agility: {pagility}")
		print(f"Intellect: {pintellect}")
	else:
		break


print("And now enter your name adventurer:")
pname = input(input_)

print(f"Welcome to the arena {pname}!")
print(f"\tYour Statistics:")
print(f"\tHealth: {phealth}")
print(f"\tStrength: {pstrength}")
print(f"\tAgility: {pagility}")
print(f"\tIntellect: {pintellect}")


#Attack/Defend Stucture

for index, monster in enumerate(enemies):
	m_health = monster[1]
	m_attack = monster[2]
	print(f"#{index + 1}. {monster}")
	print(f"Health: {m_health}, Attack: {m_attack}")
	while m_health > 0:
		x = input(input__)
		if x == 'Att':
			m_health = m_health - round(pattack + (1 + pstrength/5) * (1 + pagility/10) * (1 + pintellect/15))
			print(f"{monster} has {m_health} health remaining!")
		elif x == 'Def':
			print(f"{pname} defended!")
			phealth += round((pintellect / 5) + 2)
			print(f"{pname} gained 5 health points and has {phealth} health remaining!")
	print("The monster has been defeated!")
	print("You have gained a level!")
	print("Select what attribute you would like to increase:")
	print("1. Health")
	print("2. Attack")
	print("3. Strength")
	print("4. Agility")
	print("5. Intellect")
	lvlup = input(input_)
	if lvlup == '1':
		phealth += 1
	elif lvlup == '2':
		pattack += 1
	elif lvlup == '3':
		pstrength += 2
	elif lvlup == '4':
		pagility += 2
	elif lvlup == '5':
		pintellect +=1
	else:
		print("Onward and upward!")
	print("Congratulations! Onto the next monster!")


