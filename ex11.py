print("How old are you?", end=' ')
age = input()
print("How tall are you? (Inches)", end=' ')
height = int(input())
print("How much do you weigh?", end=' ')
weight = input()

f_height = int(height/12)
i_height = height%12

print(f"So, you're {age} years old, {f_height} feet, {i_height} inches tall, and {weight} pounds.")