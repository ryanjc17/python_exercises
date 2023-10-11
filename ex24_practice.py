from sys import argv

script = argv

answer_input = "> "

def package_compile(f):
	unit = float(f)
	wrapped_unit = float(f / 1000)
	packaged_unit = float(wrapped_unit / 10)
	return unit, wrapped_unit, packaged_unit

print("How many units do you have?")
f = float(input(answer_input))

unit, wrapped_unit, packaged_unit = package_compile(f)

print(f"With a starting unit amount of: {f}")
print(f"""
You would have:
{unit} units,
{wrapped_unit} wrapped units,
AND
{packaged_unit} packaged units!
""")
