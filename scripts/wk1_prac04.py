#Write a Python function rectangle_area that takes two parameters width and
#height corresponding to the lengths of the sides of a rectangle and returns
#the area of the rectangle in square inches. Area of rectangle template ---
#Area of rectangle solution --- Area of rectangle (Checker)

# Compute the area of a rectangle, given its width and height.

#saved as: http://www.codeskulptor.org/#user44_SCoUj0cZ5l_0.py
###################################################
# Rectangle area formula
# Student should enter function on the next lines.

def rectangle_area(width, height):
	area = width * height
	return area

###################################################
# Tests
# Student should not change this code.

def test(width, height):
	print "A rectangle " + str(width) + " inches wide and " + str(height),
	print "inches high has an area of",
	print str(rectangle_area(width, height)) + " square inches."

test(4, 7)
test(7, 4)
test(10, 10)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#A rectangle 4 inches wide and 7 inches high has an area of 28 square inches.
#A rectangle 7 inches wide and 4 inches high has an area of 28 square inches.
#A rectangle 10 inches wide and 10 inches high has an area of 100 square inches.
