tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# \t = tab
# \n = break to a new line
# \\ = print a backslash
# """ = The break characters in the source code are interpreted as \n until the next """. How would I comment here?
# Escape backslash-n is interpreted even when between triple double-quotes