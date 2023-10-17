answer_input = '> '
correct_count = 0

print("**********************************************************")
print("PLEASE INPUT YOUR ANSWERS TO THE FOLLOWING STRINGS:")
print("REMINDER: DO NOT INCLUDE CAPITOL LETTERS IN YOUR ANSWERS!")
print("**********************************************************")

#Question 1 ------------------------------
print("1. True and True")
input_1 = input(answer_input)

if input_1 == 'true':
	print('Correct!')
	correct_count = correct_count + 1
elif input_1 == 'false':
	print('Wrong!')

#Question 2 ------------------------------
print("2. False and True")
input_2 = input(answer_input)

if input_2 == 'false':
	print('Correct!')
	correct_count = correct_count + 1
elif input_2 == 'true':
	print('Wrong!')

#Question 3 ------------------------------
print("3. 1 == 1 and 2 == 1")
input_3 = input(answer_input)

if input_3 == 'false':
	print('Correct!')
	correct_count = correct_count + 1
else:
	print('Wrong!')


#Question 4 ------------------------------
print("4. 'test' == 'test'")
input_4 = input(answer_input)

if input_4 == 'true':
	print('Correct!')
	correct_count = correct_count + 1
else:
	print('Wrong!')


#Question 5 ------------------------------
print("5. 1 == 1 or 2 != 1")
input_5 = input(answer_input)

if input_5 == 'true':
	print('Correct!')
	correct_count = correct_count + 1
else:
	print('Wrong!')

#Question 6 ------------------------------
print("6. True and 1 == 1")
input_6 = input(answer_input)

if input_6 == 'true':
	print('Correct!')
	correct_count = correct_count + 1
else:
	print('Wrong!')

#Question 7 ------------------------------
print("7. False and 0 != 0")
input_7 = input(answer_input)

if input_7 == 'false':
	print('Correct!')
	correct_count = correct_count + 1
else:
	print('Wrong!')

#Question 8 ------------------------------
print("8. True or 1 == 1")
input_8 = input(answer_input)

if input_8 == 'true':
	print('Correct!')
	correct_count = correct_count + 1
else:
	print('Wrong!')

#Question 9 ------------------------------
print("9. 'test' == 'testing'")
input_9 = input(answer_input)

if input_9 == 'false':
	print('Correct!')
	correct_count = correct_count + 1
else:
	print('Wrong!')

#Question 10 ------------------------------
print("10. 1 != 0 and 2 == 1")
input_10 = input(answer_input)

if input_10 == 'false':
	print('Correct!')
	correct_count = correct_count + 1
else:
	print('Wrong!')

#Question 11 ------------------------------
print("11. 'test' != 'testing'")
input_11 = input(answer_input)

if input_11 == 'true':
	print('Correct!')
	correct_count = correct_count + 1
else:
	print('Wrong!')

#Question 12 ------------------------------
print("12. 'test' == 1")
input_12 = input(answer_input)

if input_12 == 'false':
	print('Correct!')
	correct_count = correct_count + 1
else:
	print('Wrong!')

#Question 13 ------------------------------
print("13. not (True and False)")
input_13 = input(answer_input)

if input_13 == 'true':
	print('Correct!')
	correct_count = correct_count + 1
else:
	print('Wrong!')

#Question 14 ------------------------------
print("14. not (1 == 1 and 0 != 1)")
input_14 = input(answer_input)

if input_14 == 'false':
	print('Correct!')
	correct_count = correct_count + 1
else:
	print('Wrong!')

#Question 15 ------------------------------
print("15. not (10 == 1 or 1000 == 1000)")
input_15 = input(answer_input)

if input_15 == 'false':
	print('Correct!')
	correct_count = correct_count + 1
else:
	print('Wrong!')

#Question 16 ------------------------------
print("16. not (1 != 10 or 3 == 4)")
input_16 = input(answer_input)

if input_16 == 'false':
	print('Correct!')
	correct_count = correct_count + 1
else:
	print('Wrong!')

#Question 17 ------------------------------
print("17. not ('testing' == 'testing' and 'Zed' == 'Cool Guy')")
input_17 = input(answer_input)

if input_17 == 'true':
	print('Correct!')
	correct_count = correct_count + 1
else:
	print('Wrong!')

#Question 18 ------------------------------
print("18. 1 == 1 and (not ('testing' == 1 or 1 == 0))")
input_18 = input(answer_input)

if input_18 == 'true':
	print('Correct!')
	correct_count = correct_count + 1
else:
	print('Wrong!')

#Question 19 ------------------------------
print("19. 'chunky' == 'bacon' and (not (3 == 4 or 3 == 3))")
input_19 = input(answer_input)

if input_19 == 'false':
	print('Correct!')
	correct_count = correct_count + 1
else:
	print('Wrong!')

#Question 20 ------------------------------
print("20. 3 == 3 and (not ('testing' == 'testing' or 'Python' == 'Fun'))")
input_20 = input(answer_input)

if input_20 == 'false':
	print('Correct!')
	correct_count = correct_count + 1
else:
	print('Wrong!')

#Result Question
print("Would you like to see your final score? (Y/N)")
final_input = input(answer_input)

final_score = (correct_count / 20) * 100

if final_input == 'y':
	print(f"You recieved {correct_count}/20 points which is {final_score}%!")
else:
	print("Thank you for participating!")