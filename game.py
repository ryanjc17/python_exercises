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
			m_health = m_health - round(pattack + (pstrength/10) * (pagility/15) * (pintellect/20))
			print(f"{monster} has {m_health} health remaining!")
		elif x == 'Def':
			print(f"{pname} defended!")
			print(f"{pname} has {phealth} health remaining!")
	print("The monster has been defeated!")

