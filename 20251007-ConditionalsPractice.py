import math
import struct

# to be able to do a xor operation on floats we need a custom method - https://stackoverflow.com/questions/14461011/xor-between-floats-in-python
"""def xor_float(f1, f2):
    f1 = int(''.join(hex(ord(e))[2:] for e in struct.pack('d',f1)),16)
    f2 = int(''.join(hex(ord(e))[2:] for e in struct.pack('d',f2)),16)
    xor = f1 ^ f2
    xor = "{:016x}".format(xor)
    xor = ''.join(chr(int(xor[i:i+2],16)) for i in range(0,len(xor),2))
    return struct.unpack('d',xor)[0]

xor_float(10.25,10.25)

xor_float(10.25,0.00)
"""

# What Quadrant is it in
x = float(input("Enter a x-coordinate: "))
y = float(input("Enter a y-coordinate: "))

print("You entered x:%f and y:%f" % (x, y))

# Q1 = +x +y
if x > 0.0 and y > 0.0:
    print("you are in Quadrant 1")

# Q2 = -x +y
elif x < 0.0 and y > 0.0:
    print("You are in Quadrant 2")

# Q3 = -x -y
elif x < 0.0 and y < 0.0:
    print("You are in Quadrant 3")

# Q4 = +x -y
elif x > 0.0 and y < 0.0:
    print("You are in Quadrant 4")

# The Origin: (0,0) / qudrant check -- meaning x=0 or y=0
elif int(x == 0) ^ int(y == 0): #fix later
    print("The point is not on one specific quadrant")
else:
    print("You are at the origin")



# Exceptions / error handling

try:
    x = int(input("input integer: "))

except:
    x = 0
    print("Please enter an integer (whole number)")

print("your output is", x)




