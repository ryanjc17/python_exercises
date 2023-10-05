age = input("How old are you? ")
height = int(input("How tall are you? (inches)"))
weight = input("How much do you weigh? ")

f_height = int(height/12)
i_height = height%12

print(f"So you're {age} years old, {f_height} feet {i_height} inches tall, and weigh {weight} pounds.")