formatter = "{} {} {} {}" #So I can declare a variable without a fixed value, a variable that's going to receive other values

print(formatter.format(1, 2, 3, 4, 5)) # formatter is the variable and format is a Python command. # added 5 as an argument and it's not printed since we are expecting only 4 values
print(formatter.format("one", "two", "three", "four")) # literal strings being printed
print(formatter.format(True, False, False, True )) # Boolean values
print(formatter.format(formatter, formatter, formatter, formatter)) # why does that print the {} brackets as characters? Maybe because they were interpreted as literal strings since they didn't receive any value
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))

# Format strings contain "replacement fields" surrounded by curly braces
#"{}". Anything that is not contained in braces is considered literal
#text, which is copied unchanged to the output.  If you need to include
#a brace character in the literal text, it can be escaped by doubling:
#"{{" and "}}".