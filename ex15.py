from sys import argv
# use argv
script, filename = argv
# get the pathway
txt = open(filename)
# use the function read
print("Here's your file %r:" % filename)
print(txt.read())
# use input
print("Type the filename again:")
file_again = input(">")
# open first
txt_again = open(file_again)
# read next
print(txt_again.read())
txt_again.close()