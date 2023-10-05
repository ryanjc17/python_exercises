#define cars as a variable and assign it a value
cars = 100
#define space in car and assign it a value. If this is a float, every calculation that uses this number will return as a float.
space_in_a_car = 4.0
#define drivers and assign it a value
drivers = 30
#define passengers and give it a value
passengers = 90
#define cars_not_driven as an equation of cars minus drivers 
cars_not_driven = cars - drivers
#define cars_driven as drivers
cars_driven = drivers
#define carpool_capacity and assign it a value based on an equation (cars driven * space in a car)
carpool_capacity = cars_driven * space_in_a_car
#define average passengers per car as an equation of passengers divided by cars driven
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")