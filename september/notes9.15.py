#James Galante
#9.15.15

#sytax and semantics
    #a compiler will awlays find a sytax error
    #almost never will find a semantic error
#syntax: and invalid python statement that stops the code from running
#semantic: a logic error that causes the program to behave differently that intended
#runtime error: an error that occurs duing mid process

#syntax error
#print(input('error') #one paran

#semantic errors
#print(x)

#functions
      #a group of python statements identified by a name

            #below is argument #below is paremeter #####on midterm
      #def <functio name> (parameters...):
              #<python statement>
             #<python statement>
      #indentation defines the block

#funcitons
# a simple function
#print('***********')
#print('*IMPORTANT*')
#print('***********')

#convert to function
def important():
    print('***********')
    print('*IMPORTANT*')
    print('***********')

important()
##def convertFtoC():
##    fahrenheit = float(input('enter temp in f: '))
##    celsius = (fahrenheit - 32.0) * 5.0 / 9.0
##    print(celsius, "C")
##
##convertFtoC()    
##
##def convertFtoC(fahrenheit):
## #  fahrenheit = float(input('enter temp in f: '))
##    celsius = (fahrenheit - 32.0) * 5.0 / 9.0
##    print(celsius, "C")

##convertFtoC(-32)
##
##def convertFtoC(fahrenheit):
## #  fahrenheit = float(input('enter temp in f: '))
##    celsius = (fahrenheit - 32.0) * 5.0 / 9.0
##    print(celsius, "C")
##    return celsius
##
##print(convertFtoC(-32))
##temp = convertFtoC(-32)
##print(temp)
##
##
##
##temp_f = float(input('enter temp in f: '))
##temp_c = convertFtoC(temp_f)
##print(temp_c)
##
##
##def avg_grade(grade1, grade2):
##    avg = (grade1 + grade2) / 2
##    print('average is', avg)
##    return avg
##
##avg_grade(90, 80)

def gravity(mass1, mass2, r):
    G = 6.673 * (10**-11) #gravity constant
    force = G * ((mass1*mass2) / r**2)
    return force

earth = 5.972e24
sun = 1.989e30
distance = 1.5e11

print(gravity(earth, sun, distance))





