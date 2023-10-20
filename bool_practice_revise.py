answer_input = '> '
correct_count = 0

QA =[
	"True and True",
	"False and True", 
	"1 == 1 and 2 == 1",
	"'test' == 'test'", 
	"1 == 1 or 2 != 1"
]

print("**********************************************************")
print("PLEASE INPUT YOUR ANSWERS TO THE FOLLOWING STRINGS:")
print("REMINDER: INCLUDE CAPITOL LETTERS IN YOUR ANSWERS!")
print("**********************************************************")

#for loop for determining elements of QA
for index, qq in enumerate(QA):
	#print index #+1 (starts at 0) and the second element (question)
	print(f"#{index + 1}. {qq}")
	#define new input parameter
	input_ = input(answer_input) == 't'
	#evalute if the input given by the user was the same of the boolean executed
	correct = input_ is eval(qq) #eval of the question executes the string as python
	#add to the current score based if the answer is correct
	correct_count += int(correct)
	#if user input matched the executed boolen, correct, if not wrong
	if correct:
		print("Correct!")
	else:
		print("Wrong!")

# Result Question
print("Would you like to see your final score? (Y/N)")
final_input = input(answer_input)

final_score = (correct_count / len(QA)) * 100

if final_input == 'y':
	print("*****************************************")
	print(f"You recieved {correct_count}/{len(QA)} points which is {final_score}%!")
	print("*****************************************")
else:
	print("Thank you for participating!")
