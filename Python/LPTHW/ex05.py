name = 'Andre F. A. Alves'
age = 29
height = 1.77 #m
height_inches = height * 39.3701
weight = 110 #kg
weight_pounds = weight * 2.20462
eyes = 'Brown'
teeth = 'White'
hair = 'Black'


print(f"Let's talk about {name}")
print(f"He's {height} meters or {height_inches} inches tall")
print(f"He's {weight} kilos or {weight_pounds} pounds heavy")
print(f"That's actually quite heavy")
print(f"He's got {eyes} eyes and {hair} hair")
print(f"His teeth are usually {teeth} depending on the coffee")

# Get the following line right, it's tricky
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}")

# Started researching the difference between scripts and programs, since with Python I seem to be running scripts (python.exe runs ex5.py, whereas a program would be stand-alone - i.e. not needing Python - e.g. ex5.exe)
# From here https://stackoverflow.com/questions/2286552/difference-between-a-script-and-a-program it seems there's no consensus to the definition of scripts and programs.
# The answer that made more sense to me was:
#
# A "program" in general, is a sequence of instructions written so that a computer can perform certain task. ## program > execution
#
# A "script" is code written in a scripting language. A scripting language is nothing but a type of programming language in which we can write code to control another software application. ## script > program > execution
#
# In fact, programming languages are of two types:
#
# a. Scripting Language
#
# b. Compiled Language
#
# Please read this: Scripting and Compiled Languages (http://wiki.answers.com/Q/What_is_the_difference_between_programming_language_and_scripting_language)
#
# Ended up here: https://www.quora.com/In-simple-terms-what-exactly-is-a-programming-language-compiler which clarified what's the actual role of a compiler.
