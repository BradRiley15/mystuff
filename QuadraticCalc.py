# Simple Quadratic Calculator for Ax^2+Bx+C=0
# Brad Riley
# 4/17/16
# Prints two solutions to a quadratic in either an integer, simplified fraction, or sort-of-simplified equation.
import math
from fractions import Fraction

print("ax"+"\u00B2"+"+"+"bx+c=0")
print("Only integers please!")
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

inRoot = (b**2 - 4*a*c) # Whats under the square root
negSqrt = False         # Boolean to tell if the equation will have a negative square root for later
negSqrt2 = False        # for 2nd solution
                        # Assumed False until it's calculated


try:                                                                    # Attempts to calculate the quadratic formula
    valuePlus = (-b + math.sqrt(inRoot)) / (2 * a)                      # Named valuePLUS for the "-b +" solution
except ValueError:                                                      # If it is a negative square root it'll make it a string isntead
    valuePlus = (str(-b) + "+√(" + str(b**2 - 4*a*c) + ")/" + str(2*a)) # It will print -b+√(#)/#
    negSqrt = True                                                      # Flip to true if its a negative so it doesn't mess with it later

    
try:
    valueMinus = (-b - math.sqrt(inRoot)) / (2 * a) # Named valueMINUS for the "-b -" solution
except ValueError:
    valueMinus = (str(-b) + "-√(" + str(b**2 - 4*a*c) + ")/" + str(2*a))
    negSqrt2 = True

    
if negSqrt == False:                            # Won't check if it is an integer if its a negative square root
    if valuePlus.is_integer() == False:         # Won't convert to fraction if it is a whole number already
        valuePlus = int(valuePlus * (2*a))      # convert to whole number
        valuePlus = Fraction(valuePlus, (2*a))  # Convert to simplified fraction
    else:
        valuePlus = int(valuePlus) # Makes it easier to read instead of a #.0
if negSqrt2 == False:     
    if valueMinus.is_integer() == False:
        valueMinus = int(valueMinus * (2*a))
        valueMinus = Fraction(valueMinus, (2*a))
    else:
        valueMinus = int(valueMinus)

        
print("The solutions are: " + str(valuePlus) + " and " + str(valueMinus))
input()

