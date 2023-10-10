from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you want that, hit RETURN.")

input("?")
answer_input = "> "

print("Opening the file...")
#changing the 'w' to an 'r+' allows for reading and writing within the same script rather than having to call 'r' as a part of the bottom function call
target = open(filename, 'r+')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print("Would you like to close the file you just created? (Y/N)")
close_file = input(answer_input)

if close_file == 'y':

	print("File has successfully been closed.")
	target.close()

if close_file == 'n':
	
	#reading the file after writing it requires the 'r' string attached within the open function
	target = open(filename)
	print(target.read())
	target.close()
