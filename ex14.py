from sys import argv

script, user_name, full_name = argv
user_input = 'Put your answer here heathen> '

print(f"Hi {user_name} or {full_name}, I'm the {script} script.")
print("I'd like to ask you a few questions!")
print(f"Do you like me {full_name}?")
likes = input(user_input)

print(f"Where do you live {full_name}?")
lives = input(user_input)

print("What kind of computer do you have?")
computer = input(user_input)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}, one of the greatest cities in the world.
And you have a {computer} computer. Sick.
""")