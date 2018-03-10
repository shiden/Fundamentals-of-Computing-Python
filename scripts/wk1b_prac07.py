#Write a Python function print_digits that takes an integer number in the range
#[0,100) and prints the message "The tens digit is %, and the ones digit is %."
#where the percents should be replaced with the appropriate values. The function
#should include an error check for the case when number is negative or greater
#than or equal to 100. In those cases, the function should instead print "Error:
#Input is not a two-digit number.". Print digits template --- Print digits
#solution --- Print digits (Checker)

# Compute and print tens and ones digit of an integer in [0,100).
#saved as: http://www.codeskulptor.org/#user44_HUBTYa2dBu_1.py
###################################################
# Digits function
# Student should enter function on the next lines.

def print_digits(num):
    """
    print tens and ones and error message
    """
    #print num
    if (num >= 0) and (num <= 100):
        tens = num // 10
        ones = num % 10
        print "The tens digit is " + str(tens) + ", and the ones digit is " + str(ones) + "."
        return None
    else:
        print "Error: Input is not a two-digit number."
        return None



###################################################
# Tests
# Student should not change this code.

print_digits(42)
print_digits(99)
print_digits(5)
print_digits(459)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The tens digit is 4, and the ones digit is 2.
#The tens digit is 9, and the ones digit is 9.
#The tens digit is 0, and the ones digit is 5.
#Error: Input is not a two-digit number.
