 # -*- coding: utf-8 -*-

 

# CS1202
# Expressions, input and output



# read the name, surname and title of a person and print title surname,name

name = input(' what is your given name?   ' )

sur = input(' what is your family name? ')

title = input (' what is your title? ')


print(' Welcome ', title, ' ',sur,', ',name)

input(' holding for formatted printing - Press enter')


# another way of printing (formatted)

print(' Welcome  %s  %s, %s'%(title,sur,name))




'''
In Python, these are the most common operations for maths:
    
    *  multiplication
    - subtraction
    + sum
    / division
    // integer division
    ** power
    % rest of the integer division
    
    
 '''   

# calculate and store: (2^8 - 156)/8 (yes Python allows round brackets in expressions). Print the result

# calculate and store the expression (var1*3.6  - var2/2)/3

input(' holding for expressions - Press enter')

var1 = 30
var2 = 19

express = (var1*3.6  - var2/2)/3

print (express)

input('holding ...')
# other printing  (formatted)
print(' %3.2f' % express)

input('holding ...')
# Multiply each variable by 2 and calculate expression again.

var1 = var1*2
var2 = var2*2

express = (var1*3.6  - var2/2)/3

# other printing  (formatted)
print(' %3.2f' % express)

# Now read from the user values for the variables and  calculate the expression again

input('holding ... you will be asked to enter some values - Press enter')

var1=int(input(' next value for var1 (integer) : '))

var2=int(input(' next value for var2 (integer) : '))

express = (var1*3.6  - var2/2)/3


print(' %3.2f' % express)


# repeat the process above, now with floating point variables

var1=float(input(' next value for var1 : '))
var2=float(input(' next value for var2 : '))

express = (var1*3.6  - var2/2)/3


print(' %3.2f' % express)


# rounding and flattening a floating point number


num = 23.565

input('holding...  truncating and rounding - Press enter')

num_int = int(num)

num_round = round(num)


print('number = ',num,'\n integer part is ', num_int, '\n and rounded it is ',num_round)


num = 23.444
input('holding...  truncating and rounding - Press enter')

num_int = int(num)

num_round = round(num)


print('number = ',num,'\n integer part is ', num_int, '\n and rounded it is ',num_round)
