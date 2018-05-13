# Worksheet on strings, lists

# String slices
# What is the output of the following statements?

x = 'mnopqrstuv'
print(x)
## 'mnopqrstuv' ---
print(x[1])
## 'n'---
print(x[1:2])
## 'n' 
print(x[1:2:1])
## 'n'
print(x[1:5:1])
## 'nopq'
print(x[1:6:2])
## 'npr'
print(x[0::2])
## 'moqsu'
print(x[::2])
## 'moqsu'
print(x[5:])
## 'rstuv'
print(x[:5])
## 'mnopqr'
print(x[:6:])
## 'mnopqr'

# Using the "in" operator with strings and lists
# What is printed?
food = 'marshmallow'

##for i in food:
##    print(i)
#m
#a
#r
#s
#h
#m
#a
#l
#l
#o
#w   

#What is printed?	
for i in range(len(food)):
    print(food[i])
#m
#a
#r
#s
#h
#m
#a
#l
#l
#o
#w    

#What is printed?  What does x represent semantically?
##x = 0
##for i in food:
##    if i == 'm':
##        x = x + 1
##print(x)
##
###2


#What does the following function do?  Does it remind you of anything?
def convert(remainder):
    Table = '0123456789ABCDEF'
    if 0 <= remainder <= 15:
        return Table[remainder]
    else:
        return None
convert(13)

##It convents the remainder of a number into bit format


#What is printed?
fruits = ['apple', 'pear', 'orange', 'banana', 'tomato', 'melon']
for x in fruits:
    for i in x:
        if i == 'a':
            print(i)

#a
#a
#a
#a
#a
        

#What is printed?			
fruits = ['apple', 'pear', 'orange', 'banana', 'tomato', 'melon']
for x in fruits:
    for i in x:
        if i == 'a':
            print(x)
#apple
#pear
#orange
#banana
#banana
#banana
#tomato			
			
#Given a list of first names:
names = ['Sam', 'Steve', 'Ann', 'Sue']

# Write code that will print out all names that contain the letter 's'.
for x in names:
    for i in x:
        if i == 'S':
            print(x)

# Write code that will print out the number of names that contain the
# letter 's'.
amount = 0
for x in names:
    for i in x:
        if i == 'S':
            amount = amount + 1
print(amount)

# Write code that will print out the total number of times the letter
# 's' occurs in all of the names.


