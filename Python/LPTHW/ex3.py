print("I will now count my chickens:") # Prints text

print("Hens", 25.0 + 30.0 / 6.0) # Prints "Hens" then the result of 25+30/6. PEMDAS says the order for calculating the result is 30/6 then add 25.
print("Roosters", 100.0 - 25.0 * 3.0 % 4.0) # Prints "Roosters" then the result of the calculation. Notable here is the use of Modulus: 25*3 = 75. 75/4 = 18.75. So 18*4 = 72, which means 75%4 = 75-72

# From StackOverflow (https://stackoverflow.com/questions/4432208/how-does-work-in-python):
#
#
# The modulus is a mathematical operation, sometimes described as "clock arithmetic." I find that describing it as simply a remainder is misleading and confusing because it masks the real reason it is used so much in computer science. It really is used to wrap around cycles.
#
# Think of a clock: Suppose you look at a clock in "military" time, where the range of times goes from 0:00 - 23.59. Now if you wanted something to happen every day at midnight, you would want the current time mod 24 to be zero:
#
# if (hour % 24 == 0):
#
# You can think of all hours in history wrapping around a circle of 24 hours over and over and the current hour of the day is that infinitely long number mod 24. It is a much more profound concept than just a remainder, it is a mathematical way to deal with cycles and it is very important in computer science. It is also used to wrap around arrays, allowing you to increase the index and use the modulus to wrap back to the beginning after you reach the end of the array.
#
#
# Also learned that Python doesn't alllow multi-line comment while trying to comment StackOverflow's post as a block: https://www.codecademy.com/en/forum_questions/505ba3cfc6addb000200e33c

print("Now I will count the eggs:")

print(3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0) #The actual order is you do the multiplication and division (M&D) in one step, from left to right, then you do the addition and subtraction in one step from left to right. So, you could rewrite PEMDAS as PE(M&D)(A&S).
# So 4%2=0, then 1/4=0.25, then 3+2+1-5+0-0.25+6, which equals exactly 6.75

print("Is it true that 3 + 2 < 5 - 7?")

print(3.0 + 2.0 < 5.0 - 7.0) # When using the < or > or <= or >=, the result is boolean: TRUE or FALSE

print("What is 3 + 2?", 3.0 + 2.0)

print("What is 5 - 7?", 5.0 - 7.0)

print("Oh, that's why it's False.")

print("How about some more.")

print("Is 5 greater than -2?", 5.0 > -2.0)
print("Is 5 greater or equal to -2?", 5.0 >= -2.0)
print("Is 5 less or equal to -2?", 5.0 <= -2.0)
