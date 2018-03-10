#Write a Python function name_tag that takes as input the parameters first_name
#and last_name (strings) and returns a string of the form "My name is % %."
#where the percents are the strings first_name and last_name. Reference the
#test cases in the provided template for an exact description of the format of
#the returned string. Name tag template --- Name tag solution --- Name tag
#(Checker)


# Compute a name tag, given the first and last name.
#saved as: http://www.codeskulptor.org/#user44_wryraKZ5Tg_0.py
###################################################
# Name tag formula
# Student should enter function on the next lines.

def name_tag(first_name, last_name):
	sentence = "My name is "+ first_name + " " + last_name +"."
	return sentence

###################################################
# Tests
# Student should not change this code.

def test(first_name, last_name):
	print name_tag(first_name, last_name)

test("Joe", "Warren")
test("Scott", "Rixner")
test("John", "Greiner")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#My name is Joe Warren.
#My name is Scott Rixner.
#My name is John Greiner.
