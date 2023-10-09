from sys import argv

script, first, second, third = argv

print("What is your fourth argument?:")
fourth = input()
print("What is your fifth argument?:")
fifth = input()

print("The name of your script is:", script)
print("Your first argument is:", first)
print("Your second argument is:", second)
print("Your third argument is:", third)

print(f"Your script is called: {script}. Your arguments are as follows: {first}, {second}, {third}, {fourth}, {fifth}")
