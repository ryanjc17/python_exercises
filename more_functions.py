class Rectangle:
	def __init__(self, length, width):
		self.length = int(length)
		self.width = int(width)

	def area(self):
		return self.length * self.width

	def perimeter(self):
		return (2 * self.length) + (2 * self.width)

input_l = input("Enter the length of your rectangle: ")
input_w = input("Enter the width of your rectangle: ")

Rectangle = Rectangle(input_l, input_w)
print(f"Perimeter: {Rectangle.perimeter()}")
print(f"Area: {Rectangle.area()}")