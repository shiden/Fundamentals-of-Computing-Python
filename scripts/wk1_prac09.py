#Write a Python function name_and_age that takes as input the parameters name
#(a string) and age (a number) and returns a string of the form "% is % years
#old." where the percents are the string forms of name and age. Reference the
#test cases in the provided template for an exact description of the format of
#the returned string. Name and age template --- Name and age solution ---
#Name and age (Checker)

# Compute the statement about a person's name and age, given the person's name and age.

#saved as: http://www.codeskulptor.org/#user44_cuhkCTyEnu_0.py
###################################################
# Name and age formula
# Student should enter function on the next lines.
def name_and_age( name, age):
	sentence = name + " is " + str(age) + " years old."
	return sentence


###################################################
# Tests
# Student should not change this code.

def test(name, age):
	print name_and_age(name, age)

test("Joe Warren", 52)
test("Scott Rixner", 40)
test("John Greiner", 46)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#Joe Warren is 52 years old.
#Scott Rixner is 40 years old.
#John Greiner is 46 years old.
