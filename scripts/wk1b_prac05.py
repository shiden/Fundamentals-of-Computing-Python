#Write a Python function interval_intersect that takes parameters a, b, c, and
#d and returns True if the intervals [a,b] and [c,d] intersect and False
#otherwise. While this test may seem tricky, the solution is actually very
#simple and consists of one line of Python code. (You may assume that a less than b
#and c less than d.) Interval intersect template --- Interval intersect solution ---
#Interval intersect (Checker)

# Compute whether two intervals intersect.
#saved as: http://www.codeskulptor.org/#user44_vxusa0U4Bv_0.py
###################################################
# Interval intersection formula
# Student should enter function on the next lines.

def interval_intersect(a, b, c ,d):
    """
    returns if the interval insests
    """
    return (c <= b) and (a <= d)

###################################################
# Tests
# Student should not change this code.

def test(a, b, c, d):
    """Tests the interval_intersect function."""
    print "Intervals [" + str(a) + ", " + str(b) + "] and [" + str(c) + ", " + str(d) + "]",
    if interval_intersect(a, b, c, d):
        print "intersect."
    else:
        print "do not intersect."

test(0, 1, 1, 2)
test(1, 2, 0, 1)
test(0, 1, 2, 3)
test(2, 3, 0, 1)
test(0, 3, 1, 2)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#Intervals [0, 1] and [1, 2] intersect.
#Intervals [1, 2] and [0, 1] intersect.
#Intervals [0, 1] and [2, 3] do not intersect.
#Intervals [2, 3] and [0, 1] do not intersect.
#Intervals [0, 3] and [1, 2] intersect.
