#defining variables and nesting the variable in a string function
types_of_people = 10
x = f"There are {types_of_people} types of people."

#defining more variables and listing said variables within a function
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

#printing the above functions
print(x)
print(y)

#nesting x and y within a string function
print(f"I said: {x}")
print(f"I also said: '{y}'")

#defining a variable
hilarious = False

#defining another variable
joke_evaluation = "Isn't that joke so funny?! {}"

#defining how to print the above variables with a python function (format).
print(joke_evaluation.format(hilarious))

#as the below are defined as variables, you can use math to add the strings together
w = "This is the left side of..."
e = "a string with a right side."

#print w and e together
print(w + e)