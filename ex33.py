input_ = ('> ')
print("How many numbers would you like to add?")
num_var = input(input_)

def while_loop(num_var):
	numbers = []
	i = 0
	while i < int(num_var):
		print(f"At the top i is {i}")
		numbers.append(i)
		i = i + 1
		print("Numbers now: ", numbers)
		print(f"At the bottom i is {i}")

print(while_loop(num_var))