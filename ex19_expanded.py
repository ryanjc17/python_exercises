def battleships_and_warplanes(battleships, warplanes):
	print(f"This is your total count of {battleships}!")
	print(f"This is your total count of {warplanes}!")
	print(f"You have {warplanes} warplanes and {battleships} battleships!")
	print(f"You have {combined_total} warplanes and battleships!")

answer_input = ">>> "

print("Please enter how many warplanes you have:")
warplanes_input = input(answer_input)

print("Please enter how many battleships you have:")
battleships_input = input(answer_input)

combined_total = int(warplanes_input) + int(battleships_input)

battleships_and_warplanes(battleships_input, warplanes_input)

