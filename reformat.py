import csv

input1 = input("Input your filename: ")

with open(input1, mode='r') as csv_file:
		#read csv file
		csv_reader = csv.DictReader(csv_file)
		line = 0
		#look at rows and if row is 0, list column names and generate column names
		for row in csv_reader:
			if line == 0:
				column_names = ", ".join(row)
				print(f"Column names are [{column_names}]")
				line +=1
			else:
				print(row)
