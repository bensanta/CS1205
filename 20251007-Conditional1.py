# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 11:07:14 2025

@author: rosane
"""

# import math


# a = int(input('type an integer number: '))

# """
# if you want to read in two steps:
    
    
# a = input('type an integer number: ')

# a = int(a)

# """


# sq = math.sqrt(a)


# print('the square root of %5d is %7.2f'%(a,sq))
# print('the square root of %d is %.2f'%(a,sq))


x = float(input('please type x coordinate of a point in cartesian space: '))

y = float(input('please type y coordinate of a point in cartesian space: '))

print('The point in Cartesian space that you typed is (%.1f,%.1f)'%(x,y))


if x != 0.0 and y!=0.0:

    if x > 0.0:
        if y > 0.0:
            q = 1
        else:
            q = 4
    else:
        if y > 0.0:
            q = 2
        else:
            q = 3

else:
    q = 0

if q==0:
    print('The point is not on a quadrant')
else:
    print('The quadrant of the point is ', q)

     























