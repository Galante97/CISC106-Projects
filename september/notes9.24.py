###James Galante 
##
####askey code value
##print(ord('a'))
##print(ord('b'))
##print(ord('c'))
##print(ord('d'))
##print(ord('e'))
##print(ord('f'))
##print(ord('g'))
##print(ord('h'))
##print(ord('i'))
##print(ord('j'))
##print(ord('k'))
##print(ord('l'))
##print(ord('m'))
##print(ord('n'))
##print(ord('o'))
##print(ord('p'))
##print(ord('q'))
##print(ord('r'))
##print(ord('s'))
##print(ord('t'))
##print(ord('u'))
##print(ord('v'))
##print(ord('w'))
##print(ord('x'))
##print(ord('y'))
##print(ord('z'))
##help(ord)
text.unicode('utf-8')

####how do u round a float to the nearest in?
####int() trucates float
##print(int(5.4)) #5
##print(int(5.999)) #5
##
####add 0.5 before converting to an int
##print(int(5.999 + 0.5)) #6
##print(int(5.3 + 0.5)) #5
##
#### not - highest precedence
#### and - next hightest precedence
##    #associativity is left to right
#### or - lowest precedence
##    #associativity is left to right
##    
#### logical operators
##a = True
##b = True
##c = True
##d = True
##a and not b or c
###associativity
##a and b and c and d
##a or b or c or d
##
###does this work
##x = 6
##
##if  x == (2 or 4 or 6):   #no it can only equal 2
##    print('x is 2, 4, or 6')
##else:
##    print('x is not those things')
##
###this is the correct way
##if x == 2 or x == 4 or x == 6:
##    print('x is 2, 4, or 6')
##else:
##    print('x is not those things')
##
#### if else review
##age = int(input("how old are you: "))
##if age < 21:
##    print("i cant serve you")
##else:
##    print("continue processing ")
##
##
##def is_teenager(age):
##    if (13 <= age < 20):  #short hand for age >= 13 and age <= 19:
##        decision = 'YES, you are a teenager'
##    else:
##        decision = 'NO, youre not a teen'
##    return decision
##
##print(is_teenager(19.9))
##
##


#if-elif statment
#score = float(input('enter score:'))
##score = 85
##if score >= 90:
##    print('grade A')
##elif score >= 80:
##    print('grade B')
##elif score >= 70:
##    print('grade C')
##elif score >= 60:
##    print('grade D')
##else:
##    print('your grade is an F')
##
##language = 'python'
##def get_language():
##    print('this language is', language)
##get_language()
##
##
##






    
