# set environment.
from sys import argv

script, filename = argv

target = open(filename, 'r')
total = target.read()
print "You have %s bottles!" % total

print "Do you wish to add more?\n(Y=ENTER, N=CTRL-C)"
raw_input("\n\n\n\n>")



# input data from user


    

# return data from file
def bottlecollected(cases, bottles):
    print "You have %s full cases\nand %s loose bottles." % (cases, bottles)
    print "ENTER to continue, CTRL-C to Abort."
    raw_input()


