from sys import argv

script = argv
user_input = "Put your filename here heathen> "
answer_input = '> '

print("Please enter your filename:")
filename = input(user_input)

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())


print("Would you like to close your file? (Y/N):")
close_file = input(answer_input)

if close_file == 'y':

	print("File has successfully been closed."), 
	txt.close()

if close_file == 'n':
	
	print("Please input a new file name:")

	new_filename = input(answer_input)

	txt2 = open(new_filename)
	
	print(f"Here's your file {new_filename}:")
	print(txt2.read())
	txt2.close()

