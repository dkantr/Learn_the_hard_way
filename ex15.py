#Selecting module 'argv'
from sys import argv

#Listing the two variables
script, filename = argv

#Assigning a variable to the file which is to open
txt = open(filename)

#Promt and file name read-back
print "Here's your file %r" % filename
#Print the txt with the .read '()' meaning no parameters
print txt.read()

print "Type the filename again:"
#the var 'file_again' will be the raw input of the user
file_again = raw_input(">")

#this time the variable is a open command of the previous variable
txt_again = open(file_again)

#another printing of file with .read command, no parameters
print txt_again.read()
