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

##
##def convertFtoC(fahrenheit):
##        c = (fahrenheit - 32.) *5.0/9.0
##        return c
##
##print(convertFtoC(32))
##
###checks to see if the value converted is correct
##assertEqual(convertFtoC(-40), -40.0)
##assertEqual(convertFtoC(32), 0.0)
##assertEqual(convertFtoC(212), 100.0)
##assertEqual(convertFtoC(212), 100.0)
##
###round() function
##print(2 / 3)
##print(round(2/3, 2))
##print(round(2/3, 5))
##
##assertEqual(round(convertFtoC(75), 2), 23.89)
##
##
###observations on representing decimal numbers in
### a binary system
##print(format(0.075, '.2f'),
##      format(0.05 + 0.025, '.2f'))
##
##from decimal import Decimal
##print(Decimal(0.075))
##print(Decimal(0.05))
##print(Decimal(0.025))
##print(Decimal(0.05 + 0.025))
##
##
##def avg_grade(grade1, grade2):
##        avg  = (grade1 + grade2) / 2.0
##        return avg
##assertEqual(avg_grade(0, 100), 50)
##assertEqual(avg_grade(0, 0), 0)
##assertEqual(avg_grade(50, 80), 65)
##assertEqual(avg_grade(75, 94), 84.5)
##assertEqual(avg_grade(70.1, 70.0), 70.05)

# Doc String
def convertFtoC(fahrenheit):
        '''
        convert temperature from f to c
        parameters:
           fahrenheit (number) - temp in f
        returns:
            celsius (float) - temperature in C
        '''    
        celcius = (fahrenheit - 32.) *5.0/9.0
        return celcius
convertFtoC(34)

def avg_grade(grade1, grade2):
        '''
        calculate the average of two grades.
        parameters:
            grade1 (number) - 1st grade
            grade2 (number) - second grade
        returns:
            average(flooat) - average of grade1 and grade2
        '''
        avg  = (grade1 + grade2) / 2.0  
        return avg

avg_grade(34, 53)

import math
help(math.sqrt)
help(math.acos)
help(math.log)


    
