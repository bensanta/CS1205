import math
"""

Date: 2025/10/31
Week 8 Exercise List / completion: https://ucc.instructure.com/courses/83383/files/9574053?module_item_id=2781422

"""


"""
Question 1: distance b/w two points

distance formula: https://byjus.com/maths/distance-between-two-points-formula/
"""

def PointsDistance(x1, y1, x2, y2):
    return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))

print(PointsDistance(1,1,2,2))

"""
Question 3: Write and test a Python function to return the largest between three numbers, received as parameters.
"""
def LargestNum(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

"""
Question 4: Write and test a Python function to return the smallest between three numbers, received as parameters.
"""
def SmallestNum(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c

"""
Question 5: Write and test a Python function to return the largest and the smallest between three numbers, received as parameters.
"""

def DifferenceInRange(a, b, c):
    # find smallest num
    smallest = 0
    if a < b and a < c:
        smallest = a
    elif b < a and b < c:
        smallest = b
    else:
        smallest = c

    #find the largest num
    largest = 0
    if a > b and a > c:
        largest = a
    elif b > a and b > c:
        largest = b
    else:
        largest = c

    # return the difference
    return largest - smallest

"""
Question 6: Write a Python function to receive a string and a symbol and return another string containing
twice the input string with the symbol in the middle. 
Examples:   1) concat(’hello’,’*’) would return ’hello*hello’ 
            2) concat('hello',4) would return ’hello4hello’
"""

def Concat1(a, b): #type-convert in one line
    return str(a)+str(b)+str(a)

print(Concat1("Hello", 4))
print(Concat1("yo", "*"))

"""
Question 7: Code the function in Q6 in two other ways.
"""

def Concat2(a, b): #type-convert using variable and then return variables together
    aToString = str(a)
    bToString = str(b)
    return aToString+bToString+aToString

print(Concat2("helloooo", 78.9))

def Concat3(a, b): #f-string: https://www.w3schools.com/python/python_string_formatting.asp
    return f"{a}{b}{a}"

print(Concat3("heyyo", 55))
print(Concat3("helllllo", " *** "))


"""
Extra practice: 
use any loop in a python function which adds together 
the 2nd string to the first string then the first again, so outputs "str1STR2str1" 
and add in a parameter on how many times to print this
"""
def Concat4(a, b, repeats):
    #ERROR HANDLING: if the user wants to repeat with a value less than 0, ask them to enter a positive value.
    if repeats < 0:
        return "Error: Please enter a positive value"

    #ERROR HANDLING: whole numbers only
    if repeats % round(repeats,0) != 0:
        convertRepeats = input(f"You entered {repeats} as the number of repeats, a whole number is required, does {int(repeats)} work? Y/N: ")
        if convertRepeats == "Y" or "y":
            repeats = int(repeats)
        elif convertRepeats != "Y" or "y" : #!DOESNT WORK PROPERLY - NEED TO FIX
            return "Error: Enter a whole number."

    finalString = str(a)
    for i in range(repeats): #force an integer onto repeats AND if a value is below 0, converts it to the positive version
        finalString = finalString + str(b) + str(a)

    return finalString

print(Concat4("hello", 9, 1))
print(Concat4("repeats", " ** ", 3))
print(Concat4("Hello ", "Ben ", 5))
# print(Concat4("Hello ", "Ben ", 9.2))


"""
Question 8: Write a function in Python that, given two integer numbers a and b, a > b, returns the closest
number to a that can be divided exactly by b.
"""


def ClosestDivisible(a, b):

    # ERROR HANDLING: a must be larger than b
    if a < b:
        return "ERROR: Enter a value where a is larger"

    #calculate the closest in both directions
    below = a // b * b
    above = (a // b + 1) * b

    #checks which is closest
    closest = 0
    if (a - below) < (above - a):
        closest = below
    else:
        closest = above

    return closest

print(ClosestDivisible(90,6))
print(ClosestDivisible(20,21))
print(ClosestDivisible(4,6))
print(ClosestDivisible(20,5))


