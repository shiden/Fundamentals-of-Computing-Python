#Write a Python function circle_circumference that takes a single parameter
#radius corresponding to the radius of a circle in inches and returns the the
#circumference of a circle with radius radius in inches. Do not use pi=3.14,
#instead use the math module to supply a higher-precision approximation to pi.
#Circumference of circle template --- Circumference of circle solution ---
#Circumference of circle (Checker)
# Compute the circumference of a circle, given the length of its radius.

#saved as: http://www.codeskulptor.org/#user44_ghgu7wEpx7_0.py
###################################################
# Circle circumference formula
# Student should enter function on the next lines.
import math

def circle_circumference(radius):
#	print math.pi
	circumference = 2 * math.pi * radius
	return circumference

###################################################
# Tests
# Student should not change this code.

def test(radius):
	print "A circle with a radius of " + str(radius),
	print "inches has a circumference of",
	print str(circle_circumference(radius)) + " inches."

test(8)
test(3)
test(12.9)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#A circle with a radius of 8 inches has a circumference of 50.2654824574 inches.
#A circle with a radius of 3 inches has a circumference of 18.8495559215 inches.
#A circle with a radius of 12.9 inches has a circumference of 81.0530904626 inches.
