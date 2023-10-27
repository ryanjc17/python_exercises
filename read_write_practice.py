import csv

input_ = input("Input your filename: ")
input__ = input("Would you like to read or write this file? (r/w): ")

with open(input, mode=input__) as csv_file:
	csv_reader = csv.DictReader(csv_file)
	line = 0
	for row in csv_reader:
		if line == 0:
			print(f"Column names are{", ".join(row)}")
			column_names = ", ".join(row)
			line +=1
