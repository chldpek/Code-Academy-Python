#Section 7.1
def tax(bill):
    """Adds 8% tax to a restaurant bill."""
    bill *= 1.08
    print "With tax: %f" % bill
    return bill

def tip(bill):
    """Adds 15% tip to a restaurant bill."""
    bill *= 1.15
    print "With tip: %f" % bill
    return bill

meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)

#Section 7.2
def spam():
    print "Eggs!"
"""printing eggs function"""

# Define the spam function above this line.
spam()

#Section 7.3
def square(n):
    """Returns the square of a number."""
    squared = n**2
    print "%d squared is %d." % (n, squared)
    return squared

# Call the square function on line 9! Make sure to
# include the number 10 between the parentheses.
square(10)

#Section 7.4
def power(base, exponent):  # Add your parameters here!
    result = base**exponent
    print "%d to the power of %d is %d." % (base, exponent, result)

power(37,4)

#Section 7.5
def one_good_turn(n):
    return n + 1

def deserves_another(n):
    return one_good_turn(n) + 2

#Section 7.6
def cube(number):
    return number ** 3

def by_three(number):
    if number % 3 ==0:
        return cube(number)
    else:
        return False

#Section 7.8
import math
print math.sqrt(25)

#Section 7.9
from math import sqrt

#Section 7.10
from math import *

#Section 7.11
import math            # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print everything       # Prints 'em all!

#Section 7.12
def biggest_number(*args):
    print max(args)
    return max(args)

def smallest_number(*args):
    print min(args)
    return min(args)

def distance_from_zero(arg):
    print abs(arg)
    return abs(arg)


biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

#Section 7.13
maximum = max(2, 50, 602, 26036)

print maximum

#Section 7.14
minimum = min(105, 23,-352, -2)

print minimum

#Section 7.15
absolute = abs(-42)

print absolute

#Section 7.16
print type(32)
print type(3.1)
print type('blah')

#Section 7.17
def shut_down(s):
    if s=='yes':
        return "Shutting down"
    elif s=="no":
        return "Shutdown aborted"
    else:
        return "Sorry"

#Section 7.18
