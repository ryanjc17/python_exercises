name = 'John C. Ryan'
age = 24 #years old
height = 74 #inches
m_height = height * 2.54
f_height = int(height/12)
i_height = int(height%12)
weight = 210 #pounds
m_weight = weight * 0.453592
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {f_height} foot, {i_height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

print(round(m_height))
print(round(m_weight))

total = age + height + weight
print(f"If I had {age}, {height}, and {weight}, I get {total}.")
