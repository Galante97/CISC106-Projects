###James Galante
###9.10.15
##
###more on the print() functions
###end-of-line character, replaces the next paragraph, enter, into wahtever you want
##print(1)
##print(2)
##print(3)
##
##print(1, end = ' $ ')
##print(2, end = ' $ ')
##print(3)
##
### item seperator, changes the space into somthing else
##print(1,2,3)
##print(1,2,3, sep='')
##print(1,2,3, sep='$')
##
###multi-line statements
##        #this has backslashes
##totalEnergy = 0.5 * mass1 * velocity1 ** 2 + \
##              mass1 * height1 + \
##              0.5 * mass2 * velocity3 ** 2 + \
##              mass2 * height2 + \
##              0.5 * mass3 * velocity3 ** 2 + \
##              mass3 * height1
##
##        #this has parens
##totalEnergy = (0.5 * mass1 * velocity1 ** 2 + 
##              mass1 * height1 + 
##              0.5 * mass2 * velocity3 ** 2 + 
##              mass2 * height2 + 
##              0.5 * mass3 * velocity3 ** 2 + 
##              mass3 * height1)
##
##print("this is a super long string and im super",
##     "hungry and really waht to get an omlet after this its gonna be good")
##
###strings
##print("hello" + " " +"world")
##
##style = 's'+'t'+'y'+'l'+'e'
##print(style)
##
##first = 'James'
##last = 'Galante'
##full = first + ' ' + last
##print(full)
##
###repitition (mulitication)
##atmark = '@'
##print(atmark * 5)


#escape characters
#new line char
print(1, end = '\n')
print(2, end = '\n')
print(3, end = '\n')

print(1, end = '\n\n')
print(2, end = '\n\n')
print(3, end = '\n\n')

#tap char
print('1\t2\t3')

###escape quotes
##print('Don\'t use a contration')
##print("I \"like\" code")
##
###escape backslash
##print("pyton is installed in usrs james\dev\\")
##
##
###convert Farenhiet to Celcius
##f = input('Enter the farenhiet temp:')
##c = (float(f) - 32.0) * (5.0/9.0)
##print(c, 'degrees celcius')
##
###asks grades and output average
##grade1 = input("enter your first grade percantage: ")
##grade2 = input("enter your second grade percantage: ")
##average = (float(grade1) + float(grade2)) / 2
##print("your average grade is", average)
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##

