## is-a
class Animal(object):
	pass

## is-a
class Dog(Animal):

	def __init__(self, name):
		##has-a
		self.name = name

##is-a
class Cat(Animal):

	def __init__(self, name):
		##has-a
		self.name = name


##is-a
class Person(object):

	def __init__(self, name):
		##has-a
		self.name = name

		##has-a
		self.pet = None

##is-a
class Employee(Person):

	def __init__(self, name, salary):
		##has-a salary and a name
		super(Employee, self).__init__(name)
		##has-a
		self.salary = salary

##is-a
class Fish(object):
	pass

##is-a
class Salmon(Fish):
	pass

##is-a
class Halibut(Fish):
	pass

#Rover is-a dog
rover = Dog("Rover")

#Satan is-a cat
satan = Cat("Satan")

#Mary is-a person
Mary = Person("Mary")

#Mary has-a Pet Satan
mary.pet = Satan

#Frank is-a employee that has-a Salary of 120000
frank = Employee("Frank", 120000)

#Frank has-a pet Rover
frank.pet = rover

#flipper is-a fish
flipper = Fish()

#crouse is-a salmon
crouse = Salmon()

#harry is-a Halibut
harry = Halibut()