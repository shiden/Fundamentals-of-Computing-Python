#Write a Python function total_seconds that takes three parameters hours,
#minutes and seconds and returns the total number of seconds for hours hours,
# minutes minutes and seconds seconds. Hours to seconds template --- Hours to
#seconds solution --- Hours to seconds (Checker)

# Compute the number of seconds in a given number of hours, minutes, and seconds.

#saved as: http://www.codeskulptor.org/#user44_p0PXav8dxk_0.py
###################################################
# Hours, minutes, and seconds to seconds conversion formula
# Student should enter function on the next lines.

def total_seconds(hours,minutes,seconds):
  hours_to_sec = hours * 60 * 60
  minutes_to_sec = minutes * 60
  total = seconds + hours_to_sec + minutes_to_sec
  return total

###################################################
# Tests
# Student should not change this code.

def test(hours, minutes, seconds):
	print str(hours) + " hours, " + str(minutes) + " minutes, and",
	print str(seconds) + " seconds totals to",
	print str(total_seconds(hours, minutes, seconds)) + " seconds."

test(7, 21, 37)
test(10, 1, 7)
test(1, 0, 1)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.


#7 hours, 21 minutes, and 37 seconds totals to 26497 seconds.
#10 hours, 1 minutes, and 7 seconds totals to 36067 seconds.
#1 hours, 0 minutes, and 1 seconds totals to 3601 seconds.
