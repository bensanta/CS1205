import math

"""
Basic Operations in Python

Addition            +
Subtraction         -
Multiplication      *
Division            /
Integer Division    //
Exponentiation      **
Modulo (remainder)  %

"""


# 1.    Calculate and print the following expressions in Python:
print("Question 1 integers")
# a) 20 + 15 integer
a1 = 20 + 15
print(a1)
# b) 20 − 15 integer
b1 = 20 - 15
print(b1)
# c) 20 × 15 integer
c1 = 20 * 15
print(c1)
# d ) 20 div 15 integer
d1 = 20 // 15
print(d1)

print("\nQuestion 1 floats")
# e) 20 div 15 floating point
e1 = 20 / 15
print(e1)


# f) 20.55 + 15.34 floating point
f1 = 20.55 + 15.34
print(f1)
# g) 20.55 − 15.34 floating point
g1 = 20.55 - 15.34
print(g1)
# h) 20.55 × 15.34 floating point
h1 = 20.55 * 15.34
print(h1)



# i) 20.55 div 15.34 rounded to integer
i1 = 20.55 / 15.34
print("i1 float is: " + str(i1))
print("i1 rounded to the nearest int is: " + '%.f' % i1)


print("\nQuestion 2")
# 2.    Calculate the same expressions as in exercise 1, but now preset each value to a variable. Print
#       each variable that is floating point using a formatted output with two digits after the decimal
#       point (ex: if the result is 23.444444 the printing should read: ’The result is 23.44’).


print("e1 meaning 1.33333 rounded to the nearest two decimal places is", round(e1,2))

print("f1 is already 2 decimal places because it's just addition: " + str(f1))
print("g1 for some reason needs to be rounded, so it's " + '%.2f' % g1)
print("h1 rounded is " + '%.2f' % h1)
print("i1 rounded to the nearest 2 decimal places is " + '%.2f' % i1)


# 3.    Re-do exercise 2 but now, instead of pre-setting the variables, calculate the expressions with
#       numbers read from the user. Write appropriate messages asking for values.
print("Q3: Please type 2 numbers that you want to divide")
div1 = input("Q3: Num 1: ")
div2 = input("Q3: Num 2: ")
divComplete = int(div1) / int(div2)
print("Q3: Your final rounded result of " + div1 + " divided by " + div2 + " is: " + '%.2f' % divComplete)


# 4.    Print all the variables in exercise 2 in a single formatted output, reading ’The results are [res1]
#       [res2]...[resn]’. Print them with three decimal places.
print("Q4: The results are " + '%.3f' % e1 + " " + '%.3f' % f1 + " " + '%.3f' % g1 + " " + '%.3f' % h1 + " " + '%.3f' % i1)
print("Q4: The results are", round(e1,3), round(f1,3), round(g1,3), round(h1,3), round(i1,3))

# 5.    Write Python code to read to integer values from user (ex. A and B) and then print if A is
#       divisible by B or not. If it is, print the result of the division. If it is not, calculate and print the
#       remainder of the division.

a5 = int(input("Q5: What is the numerator of your division: "))
b5 = int(input("Q5: What is the denominator of your division: "))
# converting user input to int
# typecasting: https://www.datacamp.com/tutorial/how-to-convert-a-string-into-an-integer-in-python

# ifs - https://www.w3schools.com/python/python_conditions.asp
if (a5 % b5) == 0:
    print("Q5: The result of your division is " + '%.f' % (a5 // b5))
else:
    print("Q5: Your equation is not divisible and the remainder of the division is " + '%.f' % (a5 % b5))
    print("Q5: The floating point value of your non-int division is " + str(a5 / b5))

# 6.    Calculate and print the multiplication table for an integer number input by the user, showing
#       the results on the screen.
multipTableInput = int(input("Q6: What integer's multiplication table would you like to see? "))
rowsToMultiply = int(input("Q6: How many rows of the multiplication table would you like to see? "))
for i in range(rowsToMultiply + 1):
    print(str(i) +  " times " + str(multipTableInput) + " is " + str((i * multipTableInput)))
    i = i + 1

# manual way w/o loop
# print(str(1) + " times " + str(multipTableInput) + " = " + str(1 * int(multipTableInput)))
# print(str(2) + " times " + str(multipTableInput) + " = " + str(2 * int(multipTableInput)))
# print(str(3) + " times " + str(multipTableInput) + " = " + str(3 * int(multipTableInput)))
# print(str(4) + " times " + str(multipTableInput) + " = " + str(4 * int(multipTableInput)))

# 7. Print the results to the equations

print("Q7: ")
print((((12*4.5)/3) + (7.6-16.3)/9.9) / (125.5/45))
print(((532+3)/13.5) + 3 * 200 - 4 * 70.53/2.5)

xDegrees = math.radians(68.5)
print(((math.cos(xDegrees))**2) + ((math.sin(xDegrees))**2))



# 8.    Create variables by attributing to them your name, student number, PPSN, birth city and
#       Course you are undertaking, then print those contents with the proper messages on screen. Obs.
#       Attention to the types of the variable.


myName = "Ben Santa"
myStdNum = 125724165
myPPSN = "7393749AB"
myBirthCity = "Copenhagen"
myCourse = "CK118"

print("I'm " + myName + ". I was born in " + myBirthCity + " but recently moved to Ireland and now my PPSN is " + myPPSN +
      ". At UCC I'm studying " + myCourse + " and my UCC student number is " + str(myStdNum) + ".")


# 9.    Write and test code in Python to calculate how many seconds there are in a number of weeks
#       W.W should be read from the user.

secsInWeek = 604800

weeksToCalculate = float(input("how many weeks' seconds would you like to calculate? "))
calculatedSecondsInWeeks = secsInWeek * weeksToCalculate

print("There are " + '%.f' % calculatedSecondsInWeeks + " seconds in " + str(weeksToCalculate) + " week(s).")
print("There are", calculatedSecondsInWeeks, "seconds in", weeksToCalculate, "week(s).")


# 10.   Calculate and print the following expressions in Python, considering all floating point numbers
#       and printed with three decimal places.

print((2.5**3 + 4**2 * 25.3**0.5) / 8.6)
print(20**3 - 65.4**54 + 20**105)
xFloat = float(input("Q10: Your first float: "))
yFloat = float(input("Q10: Your second float: "))
print((xFloat**3.433 + yFloat**2) / (2.67 + 2**8))



# Rachel stuff

# print(9//5)# = 1
#
# print(9/5) # = 1.8
#
# print(9%5) # = 4

# A way to format a string

test1 = 144
sqr = math.sqrt(test1)
# actual formatting
print("The sqrt of %d is %.2f" % (test1, sqr))