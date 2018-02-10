from sys import argv

script, user_name = argv
thevariable = '>> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me, {user_name}?")
likes = input(thevariable)

print(f"Where do you live, {user_name}?")
lives = input(thevariable)

print("What kind of computer do you have?")
computer = input(thevariable)

print(f"""
So you said \"{likes}\" about liking me.
You live in {lives}. No sure where that is.
And you have a \"{computer}\" computer. Nice.
""")