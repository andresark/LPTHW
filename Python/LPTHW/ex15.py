# from the sys package, import (make available to this script) the feature argv
from sys import argv

# script and filename are the variables argv (argument variable) will hold
script, filename = argv

# variable txt will hold the contents of the file opened by function open, encoded with the UTF-8 encoding
txt = open(filename, encoding="utf-8")

# prints the filename, which was passed to the filename variable as an argument
print(f"Here's your file {filename}:")

# The contents of the file are read by the read function that's being invoked to the txt variable, and then print
print(txt.read())
txt.close()

print ("Type the filename again:")
# stores a filename on a new file_again variable by having the user inputing it and using the "> " printed on the terminal as a clue that we're waiting for user input
file_again = input("> ")

# stores the content of the file inputed to the file_again variable on the txt_again variable
txt_again = open(file_again)

# Same as line 15
print(txt_again.read())
txt_again.write('Ive been here')
txt_again.close()