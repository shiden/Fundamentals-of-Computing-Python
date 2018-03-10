# Compute the number of feet corresponding to a number of miles.

##Write a Python function miles_to_feet that takes a parameter miles and
#returns the number of feet in miles miles. Miles to feet template --- Miles
#to feet solution --- Miles to feet (Checker)

#There are 5280 feet in a mile, because one mile is defined as 8 furlongs
#and 1 furlong is 660 feet, that makes 8 * 660 ft = 5280 feet in a mile.
###################################################
# Miles to feet conversion formula
# Student should enter function on the next lines.


#saved as: http://www.codeskulptor.org/#user44_FVnIZ9YzZi_0.py


def miles_to_feet(miles):
	feet = miles * 5280
	#print "miles: ", miles
#s	print "feet: ", feet
	return feet

###################################################
# Tests
# Student should not change this code.


def test(miles):
    print str(miles) + " miles equals",
    print str(miles_to_feet(miles)) + " feet."

test(13)
test(57)
test(82.67)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#13 miles equals 68640 feet.
#57 miles equals 300960 feet.
#82.67 miles equals 436497.6 feet.
