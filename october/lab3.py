#James Galante, Mike Malloy

from cisc106_34 import *
from math import *

##print('Problem 1')
def count_mult3_ints(theList):
    '''
    This function counts the number of multiples of 3
    within the list and add them all together
    parameter:
        theList (list)
    returns:
        amountOfMult (int)
        None (NoneType)
    '''
    amountOfMult = 0
    for i in theList:
        if int == type(i):
            if i % 3 == 0:
                amountOfMult = amountOfMult + 1                
        else:
            continue
    if amountOfMult == 0:
        return None
    return amountOfMult

intList1 = [12, 'dog', 'the', 27, 19, 'cat', 18.3, 36]
intList2 = ['dog', 'cat']
intList3 = ['dog', 9, 'cat']

assertEqual(count_mult3_ints(intList1), 3)
assertEqual(count_mult3_ints(intList2), None)
assertEqual(count_mult3_ints(intList3), 1)
##
##
##print()
##print('Problem 2')
##def sum_odd_list(theList):
##    '''
##    This program takes all the odd ints in the list
##    and adds them together, while ignoring the other
##    types
##    parameters:
##         theList (list)
##    returns:
##         sum   (int)
##         None  (noneType)
##    
##    '''
##    sum = 0
##    for i in theList:
##        if int == type(i):
##            if i % 2 == 1:
##                sum = sum + i
##        else:
##            continue
##    if sum == 0:
##        return None
##    return sum    
##
##intList1 = [12, 'dog', 'the', 27, 19, 'cat', 18.3, 36]
##intList2 = ['dog', 'cat']
##intList3 = ['dog', 9, 'cat']
##
##
##assertEqual(sum_odd_list(intList1), 46)
##assertEqual(sum_odd_list(intList2), None)
##assertEqual(sum_odd_list(intList3), 9)
##
##print()
##print('Problem 3')
##def insert_list(list1,string1):
##    x=str(string1)
##    if x != type(str) and x != stringList1.sort():
##            print('insert_list: error-value insert must be a string and list must')
##            print('be in increasing order')
##    elif x != type(str):
##            print('insert_list: error-value to be inserted must be a string')
##            return None
##    elif x == type(str) and x == stringList1.sort():
##        if stringList1 != stringList1.sort():
##            print('insert_list: error-list parameter is not in increasing order')
##            return None
##        else:
##            list1.append(x)
##            list1.sort()
##            return list1
##stringList1=['a','b','c']
##stringVar1='string'
##print(insert_list(stringList1,stringVar1))
##
##print()
##print('problem 4')
##def triangle_centroid(x1,y1,x2,y2,x3,y3):
##    '''
##    this program takes in the coordnites of triangle, find the centroid
##    of the triangle anf then calculates the distance from the origin
##    parameters:
##        x1 (number)
##        y1 (number)
##        x2 (number)
##        y2 (number)
##        x3 (number)
##        y3 (number)
##    returns:
##        None (noneType)
##        distance (number)
##    '''
##    coordList = [x1,y1,x2,y2,x3,y3]
##    for i in list(coordList):
##        if int != type(i) and float != type(i):
##            print('triangle_centroid: error - arguments must all be numbers')
##            return None
##        
##    
##    calcCentroid_x = (x1+x2+x3)/3
##    calcCentroid_y = (y1+y2+y3)/3
##    origin_x = 0
##    origin_y = 0
##    distance = sqrt((calcCentroid_x - origin_x)**2 +
##                    (calcCentroid_y - origin_y)**2)
##    print(distance)
##    return distance
##
##assertEqual(round(triangle_centroid(2,4.3,3,1,0,7), 2), 4.43)
##assertEqual(round(triangle_centroid(700,136,7,111,-123,52), 2), 218.7)
##assertEqual(round(triangle_centroid(-2,0,7,5,-3,-2), 2), 1.20)
##
##print()
##print('Problem 5')
##def assert_within_tolerance(float1, float2, tolerance):
##    '''
##    This program determines if two float operators are close together
##    bases on the tolerance provided. All parameters must be floats and
##    tolerance must be postive
##    parameters:
##       float1 (number)
##       float2 (number)
##       tolerance (number)
##    returns:
##       None (noneType)
##       False (bool)
##       True (bool)
##    '''
##    if tolerance <= 0:
##        print('Error: tolerance must be postive')
##        return None
##    if int == type(float1) or int == type(float2) or int == type(tolerance):
##        print('Error: a value entered is not a float')
##        return None
##    
##    closeInValue = float1-float2
##    if tolerance < abs(closeInValue):
##        return False
##    else:
##        return True
##
##
##
##assertEqual(assert_within_tolerance(25.0,51.23, 26.9), True)
##assertEqual(assert_within_tolerance(5.,18., 8.), False)
##assertEqual(assert_within_tolerance(21,5, 8.0), None)
##
##print()
print('Problem 6')
def word_separator(sentence):
    '''
    This program takes a phrase that is run together and
    adds spaces in bewteen each word based on where the upper
    case letters are. and then makes sure only the first letter
    is upper case
    Parameters:
       sentence (string)
    returns:
       newPhrase (string)
    '''
    string_length = len(sentence)
    letter=1
    newPhrase = ' '

    if sentence[0].isupper() == True:
        sentence = sentence[0].lower() + sentence[1:]

    for i in range(0,string_length):
        letter = sentence[i]
        if letter.isupper():
            newPhrase = newPhrase + ' ' + letter
            
        else:
            newPhrase = newPhrase + letter

    newPhrase = newPhrase.lower()
    newPhrase = newPhrase[0].upper() + newPhrase[1:]
    print(newPhrase)
    return newPhrase

'''
assertEqual(word_separator('FourScoreAndSevenYearsAgo'),
            'Four score and seven years ago')
assertEqual(word_separator('PassTheTNT'),
            'Pass the t n t')
assertEqual(word_separator('CodingIsFun'),
            'Coding is fun')
            '''
##
##print()
##print('Problem 7')
##def word_parser(mainString):
##    '''
##    this program turns a phrase with multiple words or characters
##    and takes each word or character and adds them individually in
##    a list. it does this by detecting spaces inbetween words and
##    then takes the characters inbetween them and adds them to the list
##    parameters:
##      mainString (string)
##    returns:
##      listFromPhrase (list)
##    '''
##
##    #adds a space the end of the phrase incase there is none
##    mainString = mainString + ' '
##    #find the length of the string
##    string_length = len(mainString)
##    #empty list
##    listFromPhrase = []
##    #string to be filled with each object from the list
##    addWordToList = ''
##    
##    for i in range(0, string_length):
##        letter = mainString[i]
##        if letter.isspace():
##            #checks to see if string is empty
##            #if it is it doesnt add it to the list
##            if addWordToList == '':
##                continue
##            else:
##                listFromPhrase.append(addWordToList)
##                
##            addWordToList = ''
##        else:
##            addWordToList = addWordToList + letter
##    
##    return listFromPhrase
##
##words = '    hello         world how are you    '
##word_parser(words)
##
##
##
##assertEqual(word_parser('  hello world !!! how are you'),
##            ['hello', 'world', '!!!', 'how', 'are', 'you'])
##assertEqual(word_parser('  spaces before  and   middle and after   '),
##            ['spaces', 'before', 'and', 'middle', 'and', 'after'])
##assertEqual(word_parser(' 1 13 3 3414  4'),
##            ['1', '13', '3', '3414', '4'])
##
##print()
##print('Problem 8')
##def digit_product(string1):
##    '''
##    this program contains a string and then extracts the digits from
##    that string and multiples them together and creates a single product
##    if there are no digits it returns none
##    Parameters:
##       string1 (string)
##    returns
##       product (number)
##       None (noneType)
##    '''
##
##    if str != type(string1):
##        print('Error: value is not a string')
##        return None
##    
##    string_length = len(string1)
##    product = 1
##    contains_a_digit = False
##
##    for i in range(0,string_length):
##        character = string1[i]
##
##        if character.isdigit() == True:
##            product = int(product) * int(character)
##            contains_a_digit = True
##        else:
##            continue
## 
##    if contains_a_digit == False:
##        return None
##    else:        
##       return product
##
##
##assertEqual(digit_product(1234), None)
##assertEqual(digit_product('213'), 6)
##assertEqual(digit_product('@@3!!doenv34f4'), 144)
##
##print()
##print('problem 9')
##def valid_password(computer_password):
##    '''
##    this program checks to see if a password is valid
##    the password must contain a upper and lower cases
##    a digit and a secial character if it does not it
##    will display a error and return None
##    parameters:
##       computer_password (str)
##    returns:
##       None (noneType)
##       True (bool)
##    '''
##    contains_a_uppercase = False
##    contains_a_lowercase = False
##    contains_a_digit = False
##    contains_a_special_char = False
##    
##    pass_length = len(computer_password)
##    if pass_length < 8:
##        print('Error: password to short must be between 8-15 characters')
##        return None
##    if pass_length > 15:
##        print('Error: password to long must be between 8-15 characters')
##        return None
##    
##    for i in range(0, pass_length):
##       character = computer_password[i]
##       if character.isdigit() == True:
##           contains_a_digit = True
##       if character.islower() == True:
##           contains_a_lowercase = True
##       if character.isupper() == True:
##           contains_a_uppercase = True
##
##       specialList = ['@', '$', '%', '^', '&', '*', '+', '=']
##       for x in list(specialList):
##           if character == x:
##               contains_a_special_char = True
##           else:
##               continue
##
##    if contains_a_uppercase == True and \
##    contains_a_lowercase == True and \
##    contains_a_digit == True and \
##    contains_a_special_char == True:
##        return True
##    else:
##        print('Error: not valid, pass must contain a upper \
##              and lower case letter a digit and a special character')
##        return False
##
##        
##
##
##assertEqual(valid_password('fhbd92y3fbCJ@N'), True)
##assertEqual(valid_password('$helloWorld1'), True)
##assertEqual(valid_password('password'), False)
##
##
##
##
##
##
