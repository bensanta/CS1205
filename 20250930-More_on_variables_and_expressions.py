 # -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 15:09:06 2021

Second Program CS1205 - First Part is the previous program, commented

"""

'''
This is the last code:
CS 1205 2025 - 
"""

# This is a line comment#
# This is another comment


# This is a variable, initially set to contain the value 3:
a = 3  # variable a equals 3
my_var =40000






# You can print the variable:
print (a)



# You can print operations with the variables. In Python a multiplication operatior is written '*':
print (a*10)


# You can (and in fact should) also print messages in the same print() command:
    
print('the value of the variable a is ', a)
print('a multiplied by 10 is:', a*10)


# Variables can also be of non-numerical types, such as a string:

city = 'Cork'  # the 

print(city)

# Variables can be changed. Strings can have spaces and special characters:
    
city = 'Cork is a beautiful city'

print(city)


expression = a*10

print (expression)

'''
'''
Last week we started to learn a few programming concepts.

We have learned about variables, types of variables, and printing

We have also learned that we can have expressions attributed to variables or printed direcly

This week we will extend those concepts a bit, and start learning about input.


'''


# Defining a variable named term1 and attributing 35 to it

term1 = 25

# Defining a variable named term2 and attributing 12 to it

term2 = 15


# Using the term1 and term2 in an expression, and attributing its result to a variable
# named expression_1


expression_1 = 3*term1 - term2


# In the above expression, term1 is multiplied by 3, and then term2 is subtracted from it

# What is the value of expression_1 after line 88 is executed?


print('the value of the expression is', expression_1)


# let us elaborate the printing a litle more

print('the value of the expression involving',term1,' and ',term2, 'is', expression_1)

# or a little more

print('the value of the expression 3*',term1,'-',term2, 'is', expression_1)


# input() # here only to hold the program




# In programming in general we call fixed values contants. So, in the expression
# in line 88 we have two variables (term1,term2) and one constant (3). Of course
# we also have the variable expression_1, which stores the results of the expression

# Variable names in Python can have letters ('A' to 'Z' and 'a' to 'z'), 
# digits ('0' to '9'), and underscore ('_'), and must start with a letter or
# undescore. 
# Variables are case sensitive. Ex: Avar, avar and AVAR are three different variables


# REQ:  define your standard for variables and stick to it

# Types of variables
# We have learned that variables have types and we have learned string and integer
# variables so far

str1 = 'This is a string'
number1 = 56

# String variables store words and sentences and integer variables store integer numbers

print(str1,number1)
print(str1,'\n',number1)


# There is another numerical type in python, the floating point variable, used
# to store real numbers

number2 = 15.4

print(number2)

expression_2 = number2 - number2*3.4

print(expression_2)

# naturally, an expression can result in negative numbers. An expression using
# floating point values (contants and variables) will result in  floating point 
# results

input()

expression_3 = number1 - number2 - 0.6

print(expression_3)

# 
# Expressions
'''
In Python, these are the most common operations for maths:
    
    *  multiplication
    - subtraction
    + sum
    / division
    // integer division
    ** power
    
 '''   

# calculate and store: (2^8 - 156)/8 (yes Python allows round brackets in expressions)

for i in range(1,20):
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz")
        i = i + 1
    elif i % 3 == 0:
        print("Fizz")
        i = i + 1
    elif i % 5 == 0:
        print("Buzz")
        i = i + 1
    else:
        print(i)
        i = i + 1



calculate=(2^8 - 156)/8

print(calculate)





