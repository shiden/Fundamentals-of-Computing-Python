#Write a Python function is_cool that takes as input the string name and returns
#True if name is either "Joe", "John" or "Stephen" and returns False otherwise.
#(Let's see if Scott manages to catch this. ) Cool template --- Cool
#solution --- Cool (Checker)

# Compute whether a person is cool.
#saved as: http://www.codeskulptor.org/#user44_aO3yvoM19E_0.py
###################################################
# Is cool formula
# Student should enter function on the next lines.

def is_cool(name):
	if name == "Joe":
		return True
        elif name == "John":
	   return True
        elif name == "Stephen":
	   return True
        else:
	   return False


###################################################
# Tests
# Student should not change this code.

def test(name):
	"""Tests the is_cool function."""

	if is_cool(name):
		print name, "is cool."
	else:
		print name, "is not cool."

test("Joe")
test("John")
test("Stephen")
test("Scott")

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#Joe is cool.
#John is cool.
#Stephen is cool.
#Scott is not cool.
