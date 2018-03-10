#Challenge: Write a Python function print_digits that takes an integer number
#in the range [0,100), i.e., at least 0, but less than 100. It prints the
#message "The tens digit is %, and the ones digit is %.", where the percent
#signs should be replaced with the appropriate values. (Hint: Use the
#arithmetic operators for integer division // and remainder % to find the two
#digits. Note that this function should print the desired message, rather than
#returning it as a string. Print digits template --- Print digits solution ---
#Print digits (Checker)

# Compute and print tens and ones digit of an integer in [0,100).
#saved as: http://www.codeskulptor.org/#user44_kBKfnY3Ti6_0.py
###################################################
# Digits function
# Student should enter function on the next lines.


def print_digits(number):
    #print number
    if (number >= 0) and (number <= 100):
        tens = number // 10
        #print "tens: ", tens
        ones = number % 10
        #print "ones: ", ones
        print "The tens digit is " + str(tens) + ", and the ones digit is " + str(ones) + "."
        return None
    else:
       print "out of range"


###################################################
# Tests
# Student should not change this code.

print_digits(42)
print_digits(99)
print_digits(5)
print_digits(105)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The tens digit is 4, and the ones digit is 2.
#The tens digit is 9, and the ones digit is 9.
#The tens digit is 0, and the ones digit is 5.
