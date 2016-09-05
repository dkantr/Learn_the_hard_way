# Assigning embedded string to 'x'.
x = "There are %d types of people." % 10
# Creating string.
binary = "binary"
# Creating string.
do_not = "don't"
# Assigning embedded string to 'y'.
y = "Those who know %s and those who %s." % (binary, do_not)

# Print variable
print x
# Print variable
print y

# Print string embedded with variable
print "I said: %r." % x
# Print string embedded with variable
print "I also said: '%s'." % y 

# Creating string
hilarious = False
# Creating string
joke_evaluation = "Isn't that joke so funny?! %r"

# Print string embedded string
print joke_evaluation % hilarious

# Assigning string to variable
w = "This is the left side of..."
# Assigning string to variable
e = "a string with a right side."

# Print strings
print w + e
