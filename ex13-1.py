from sys import argv

#script, first, second, third = argv

#print "Loaded:", script
#print "The first variable is:", first
#print "The second variable is:", second
#print "The third variable is:", third

#----------------------------------------------------
power, first = argv

first = raw_input("Choose your Race:\nHm\nDw\nEv\nOr\n:")
power = raw_input("Choose your Power:\nert\nwnd\nfir\nwat\n:")


print '''
If you choose to become a %s who wields the power of %s\n 
You will not be able to know the life you had before\n
such decisions were brought to your awareness''' % (rc, power)
