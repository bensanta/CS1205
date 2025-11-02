# -*- coding: utf-8 -*-
"""
First coding file for CS1205

20250916

@author: Benjamin Santa
"""

a = "hello world"
print(a)

def hello():
    print("Hello world!")
    

hello()

print (1)
print (1+ int("1"))
print (1,1,"1")

print("this is just a message.")

#text in coding is called istrings

#\n is a new line - it's called a control sequence
print("\nThis is just \na message...\nwith a control sequence")

print('another msg\n')
print("I'm embedding a quote into this message which is 'life is cool'\n")
print(1,2,4,5,"this is another msg","more numbers",5.7,"\n")

#number list up to 14 - bc we start 14
i=0
for i in range(15):
    print(i)
    i=i+1
    
#collections
##touples
print ((1,2,3,4,5))
##lists
print ([1,2,3,4,5])

print(int("12")+3)
print(12+3)

name = input("What's your name: ")
print ("your name is: " + name)



# fizbuzz attempt - everything divisible by 3 is Fizz
# divisible by 5 is Buzz
# divisible by both is FizzBuzz
