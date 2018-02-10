from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print("[DEBUG] This is what argv is holding", repr(argv))

print("The script is called:", script) #first argument is always the script name
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# Could not resolve this: Combine input with argv to make a script that gets more input from a user. Don’t overthink it. Just use argv to get something, and input to get something else from the user.