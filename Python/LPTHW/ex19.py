# Define a function called cheese and crackers and have its arguments to be cheese count and boxes of crackers counts
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!") # Print the value for the cheese_count variable, which at this point is empty but won't soon enough
    print(f"You have {boxes_of_crackers} boxes of crackers!") # Same thing, but for the number of cracker boxes
    print("Man, that's enough for a party!") # Friendly words
    print("Get a blanket.\n") # Weird words

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30) # Assign 20 to cheese_count (first argument) and 30 to boxes_of_crackers (second argument)

print ("OR, we can use variables from our script:")
amount_of_cheese = 10 # Creating an additional variable instead of assigning the values directly to the function arguments
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers) # Feeding the function arguments with the variables' values

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) # Same as 15, but with mathematical operation