# call up the argument variable module
from sys import argv

# list variables to use
script, input_file = argv

# create function 'print_all' applying to the variable 'f'
def print_all(f):
# print to user what is read in the variable 'f'
    print f.read()

# create funtion 'rewind' applying to the variable 'f'    
def rewind(f):
# move to '0' bytes in variable
    f.seek(0)
    
# create function 'print_a_line' with variables 'line_count' and 'f'
def print_a_line(line_count, f):
# print to user line count and than read one line from variable 'f'
    print line_count, f.readline()
    
#create variable 'current_file' as function 'open' variable 'input_file'
current_file = open(input_file)

# print to user with new line after text
print "First let's print the whole file:\n"

# print to user the contents of 'input_file'
print_all(current_file)

# prompt user
print "Now let's rewind, kind of like a tape."

# move to '0' bytes in 'input_file'
rewind(current_file)

# prompt user
print "lets's print three lines:"

# set current line in file as '1'
current_line = 1
# prints to user line count then current line in file
print_a_line(current_line, current_file)

# set current line in file to '1' after the line at the start
current_line = current_line + 1
# prints to user line count then current line in file
print_a_line(current_line, current_file)

# set current line in file to '1' after the line at the start
current_line = current_line + 1
# prints to user line count then current line in file
print_a_line(current_line, current_file)
    
