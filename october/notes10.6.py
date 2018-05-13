###James Galante
###10.6.15
##
#####for loops###
##
##for n in [1,2,3,4,5]:
##    print(n)
##
##
###temperature conversion table
def convertFtoC(fahrenheit):
        c = (fahrenheit - 32.) *5.0/9.0
        return c
##
##for temp_f in [0, 10, 20, 30, 40, 50 ,60, 70, 80, 90, 100]:
##    temp_c = convertFtoC(temp_f)
##    print(format(temp_f, '3d'), '   ', format(temp_c, '6.1f'))
####
##Range function
#a convieniet way to create a list of ints
# Range(start, stop, step)
# ex: Range(0,10,1) = [0,1,2,3,4,5,6,7,8,9]
#The stop value is NOT included
##
##print(list(range(1,6,1)))
##print(list(range(1,6)))
##print(list(range(5)))
##print(list(range(3,-10,-3)))

##
###for loops  with range
##for k in range(1, 6, 1):
##    print(k)
##
##for k in range(5):
##    print(k)
##
##for k in range(3, -10, -3):
##    print(k)
##
##for temp_f in range(0, 101, 10):
##    temp_c = convertFtoC(temp_f)
##    print(format(temp_f, '3d'), '   ', format(temp_c, '6.1f'))

##total = 0
##for n in range(100, 500001, 5):
##    total = total + n
##print(format(total, ',d'))
##

###saving Pennies
##total = 0
##for n in range(0, 31, 1):
##    total = total + 2 ** n
##print("saved $", format(total/100, ',.2f'), sep = '')
##
##s = 0
##total = 0
##while s < 30:
##    total = total + 2 ** s
##    s = s + 1
##print("saved $", format(total/100, ',.2f'), sep = '')
##
##
##
##

from math import *

#seed()
seed(10)
for n in range(5):
    print(random())












