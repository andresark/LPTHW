print("Mary had a little lamb.")
print("Its fleece was white as {}, yes, snow.".format('snow')) #this line "formats" the word "snow" and it wil insert this formatted text between the "{}". https://python-forum.io/Thread-New-to-Python--3880. *moderator answer on that forum thread is wrong, he missed the ''
print(">>>>>>>>> debug here")
print(f"Its fleece was white as {'snow'}, yes, snow.")
print("And everywhere that Mary went.")
print("."*100) # what does that do? It printed the '.' character 10 times

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = '' at the end. Try removing it to see what happens
print(end1 + end2 + end3 + end4 + end5 + end6, end='') # That end='' somehow removes the line break. end='' attributes an empty character to the end string. # Explanation: that was added on Python 3. If you don't want a line break after finishing printing a string, print an empty character.
burger= (end7 + end8 + end9 + end10 + end11 + end12)
print(burger)
# https://stackoverflow.com/questions/42163846/positional-argument-follows-keyword-argument
