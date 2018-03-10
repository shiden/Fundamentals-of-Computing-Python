#Write a Python function is_even that takes as input the parameter number
#(an integer) and returns True if number is even and False if number is odd.
#Hint: Apply the remainder operator to n (i.e., number % 2) and compare to zero.
#Even template --- Even solution --- Even (Checker)

# Compute whether an integer is even.

#saved as http://www.codeskulptor.org/#user44_waubLkKopy_0.py
###################################################
# Is even formula
# Student should enter function on the next lines.

def is_even(number):
	number = number % 2
	#print number
	if number == 0:
		return True
        else :
	   return False

###################################################
# Tests
# Student should not change this code.

def test(number):
	"""Tests the is_even function."""
	if is_even(number):
		print number, "is even."
	else:
		print number, "is odd."

test(8)
test(3)
test(12)

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#8 is even.
#3 is odd.
#12 is even.
