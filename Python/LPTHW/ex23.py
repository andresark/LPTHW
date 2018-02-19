import sys
script, input_encoding, error = sys.argv # is there any other argv besides sys's?
# I start with your usual command line argument handling that you already know.

def main(language_file, encoding, errors): # function main takes a file, the file's encoding and errors?
    line = language_file.readline() # read one line from the languages file it is given ## readline function will return an empty string when it reaches the end of the file

    if line: # What is the condition to be met here? If the file is not empty (has a line)? ## if line simply tests for readline's empty string 
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors) # Calling main inside main. Loop. Loop will stop when the IF condition is false.
# As long as readline gives us something, this will be true, and the code under (indented in, lines 9-10) will run. When this is false, Python will skip lines 9-10.

def print_line(line, encoding, errors):
    next_lang = line.strip() # Strip? ## This is a simple stripping of the trailing \n on the line string.
    raw_bytes = next_lang.encode(encoding, errors=errors) # errors = errors? encode?
    cooked_string = raw_bytes.decode(encoding, errors=errors)
# I then do the extra step of showing the inverse of line 15 by creating a cooked_string variable from the raw_bytes. Remember, "DBES" says I "Decode Bytes", and raw_bytes is bytes, so I call .decode() on it to get a Python string. This string should be the same as the next_lang variable.
    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)
# bytes > decode > string. bytes.decode(string)
# mnemonic "DBES" which stands for "Decode Bytes Encode Strings".
#  I say "dee bess" in my head when I have to convert bytes and strings.
#  When you have bytes and need a string, "Decode Bytes". When you have a string and need bytes, "Encode Strings".