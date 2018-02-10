types_of_people = 10
x = f"There are {types_of_people} types of people" # So x equals a formatted string which also references another variable. I tought that formatted strings only use was to print a string + the value of a variable. Why are we attributing a string to a variable if this variable is not being printed?
# ^ string inside a string

binary = "binary" # I just realized here that I'm not defining/declaring the variable type as string like on C++. The value of the variable itself is defining its type. So binary is a string variable because its value is a string.
do_not = "don't" # another string

y = f"Those who know {binary} and those who {do_not}" # another string, or rather formated string. I don't get why I would need to store a formatted string in a variable - that is the practical use of storing a formatted string in a string variable.
# ^ string inside a string

print(x)
print(y)

print(f"I said: {x}")
# ^ string inside a string

print(f"I also said: '{y}'")
# ^ string inside a string

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))
# ^ string inside a string

w = "This is the left side of..."
e = "a string with a right side"

print(w + e)


# QUESTION: Explain why adding the two strings w and e with + makes a longer string.
# ANSWER: Strings can't really be added, so they just are printed after each other.
bolo = "bolo"
cafe = "cafe"
print(bolo + cafe)
lanche=bolo+cafe
print(lanche)
