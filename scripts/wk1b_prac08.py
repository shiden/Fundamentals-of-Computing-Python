#Write a Python function name_lookup that takes a string first_name that corresponds to one
 #of ("Joe", "Scott", "John" or "Stephen") and then returns their corresponding last name
 #("Warren", "Rixner", "Greiner" or "Wong"). If first_name doesn't match any of those
 #strings, return the string "Error: Not an instructor". Name lookup template --- Name
 #lookup solution --- Name lookup (Checker)

 # Compute instructor's last name, given the first name.
#saved as: http://www.codeskulptor.org/#user44_LG5mwuD0fW_0.py
###################################################
# Name lookup formula
# Student should enter function on the next lines.

def name_lookup(first_name):
    if name == "Joe":
        return "Warren"
    elif name == "Scott":
        return "Rixner"
    elif name == "John":
        return "Greiner"
    elif name == "Stephen":
        return "Wong"
    else:
        return "Error: Not an instructor"



###################################################
# Tests
# Student should not change this code.

def test(first_name):
    """Tests the name_lookup function."""

    print name_lookup(first_name)

test("Joe")
test("Scott")
test("John")
test("Stephen")
test("Mary")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#Warren
#Rixner
#Greiner
#Wong
#Error: Not an instructor
