cars = 100 # Number of available cars.
space_in_a_car = 4 # Number of spaces available in a car.
drivers = 30 # Number of available drivers.
passengers = 90 # Number of passengers.
cars_not_driven = cars - drivers # Calculates the number of cars that can't be used because of non-available drivers by subtracting number of cars from the number of available drivers. Won't make sense if there are more drivers than cars.
cars_driven = drivers # Attributes the value of the variable drivers to the variable cars_driven. Since there are no loops on this program, I don't have to worry about cars_driven receiving different values each time it's invoked.
carpool_capacity = cars_driven * space_in_a_car # Calculates capacity by multipliying the number of available cars by the number of spaces on each car.
average_passengers_per_car = passengers / cars_driven # Distributes the number of passengers evenly throughout available cars by dividing number of passengers by the number of drivers.


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, " passengers to carpool today.")
print("We need to put about", average_passengers_per_car, " passengers in each car.")


# QUESTION: When I wrote this program the first time I had a mistake, and Python told me about it like this: Click here to view code image Traceback (most recent call last):
#  File "ex4.py", line 8, in <module>
#    average_passengers_per_car = car_pool_capacity / passenger
# NameError: name 'car_pool_capacity' is not defined
# Explain this error in your own words. Make sure you use line numbers and explain why.
# ANSWER: Typo, you meant carpool_capacity instead of car_pool_capacity. That means the variable you are referencing does not exist, thus can't be used.

# QUESTION: I used 4.0 for space_in_a_car, but is that necessary? What happens if it’s just 4?
# ANSWER: It doesn't make sense to allow a non-integer result for this operation since we're count humans (you don't want to fit 0.5 humans or 1.5 humans in a car, unless you mean midgets or obese people, in which case you're just being mean)
# ANSWER: So no, it's not necessary and if you use just 4 you will have only integer results.
