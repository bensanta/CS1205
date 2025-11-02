# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 15:30:28 2025

First example of Python commands

@OGauthor: rminghim
@secondaryAuthor: bsanta

"""
# this is our first command

#printing a message, twice

print('\nThis is \n just a \nmessage\n\n')

print('This is just a message\n')


# printing strings and numbers

print ("another message",8,190,'\n',5.7)


#printing a tuple

print((1,4,2,3,4))



#printing a list
print([1,4,2,3,4])



print('the value of the expression is',3*275/7)

# floats formatted
print('%.2f'%(3*275/7))


print('%.2f'%(117.85423432))


print('%.2f -- %.2f '%(117.85423432,117.858))

print('%.2f --> %.2f <-- %.2f '%(117.85423432,117.858,1111.789))

# rounding w/ function - loses precision within the variable - meaning
# future maths will be not correct due to rounding
precise=4567.56792379372525268
rounded=round(precise,2) #4567.57
print(precise,rounded)

# round to int = 4568
print(precise,round(precise))











