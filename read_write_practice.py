import csv

#input lines
input_ = input("Input your filename: ")
input__ = input("Would you like to read or write this file? (r/w): ")

#open filename based on input
#open mode based on input (read/write)
with open(input_, mode=input__) as csv_file:
	#read csv file
	csv_reader = csv.DictReader(csv_file)
	line = 0
	#look at rows and if row is 0, list column names and generate column field
	for row in csv_reader:
		if line == 0:
			print(f"Column names are{", ".join(row)}")
			column_names = ", ".join(row)
			line +=1
