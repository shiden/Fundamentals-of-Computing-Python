#Write a Python function is_leap_year that take as input the parameter year and
#returns True if year (an integer) is a leap year according to the Gregorian
#calendar and False otherwise. The Wikipedia entry for leap yearscontains a
#simple algorithmic rule for determining whether a year is a leap year. Your
#main task will be to translate this rule into Python. Leap year template
#--- Leap year solution --- Leap year (Checker)

# Compute whether the given year is a leap year.
#saved as: http://www.codeskulptor.org/#user44_dY8DEMgnsX_0.py
###################################################
# Is leapyear formula
# Student should enter function on the next lines.

def is_leap_year(year):
	"""
	Returns if the year is a leap year or not.
	"""
	if (year % 400) == 0:
	    return True
    elif (year % 100) == 0:
        return False
    elif (year % 4) == 0:
        return True
    else:
        return False

###################################################
# Tests
# Student should not change this code.

def test(year):
	"""Tests the is_leapyear function."""
	if is_leap_year(year):
		print year, "is a leap year."
	else:
		print year, "is not a leap year."

test(2000)
test(1996)
test(1800)
test(2013)

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#2000 is a leap year.
#1996 is a leap year.
#1800 is not a leap year.
#2013 is not a leap year.
