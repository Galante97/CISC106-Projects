#James Galante
#9.17.15

#DIFFERENT WAYS TO IMPORT LIBRARIES

#import library
#usage: library.function(arguements)
#example:
##    import math
##    math.sqrt(49)

#import library import* <- import every function
##    -usage: function(arguments)
##    -ex:
##        -from math import*
##        -sqrt(64)

#import library import<function_name, function_name2
##        usage: function(arguments)
##        ex:
##            from math import sqrt
##            sqrt(64)

#method 1
##import math
##print(math.sqrt(49))
##print(math.acos(0.49))
##print(math.log2(49))    #log base 2
##print(math.log10(49)) #log base 10        
##print(math.log(49))   #natural log

###method 2
##from math import sqrt, log
##print(sqrt(49))
##print(log(49))   #natural log
##
###method 3
##from math import *
##print(sqrt(49))
##print(log(49))

from cisc106_34 import assertEqual


def convertFtoC(fahrenheit):
        c = (fahrenheit - 32.) *5.0/9.0
        return c

print(convertFtoC(32))

assertEqual(convertFtoC(-40), -40.0)
    
