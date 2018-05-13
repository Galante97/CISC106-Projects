#notes 9.22

from cisc106_34 import assertEqual

def reverseDigits(number):
    '''
    Reverse the digits of a non-negative 2 digit int
    parameters:
      number (int) - 2 digit int
    Returns:
      newNumber (int) reverses number      
    '''
    onesDigit = number % 10
    tensDigit = number // 10

    newNumber = onesDigit * 10 + tensDigit

    return newNumber
    
assertEqual(reverseDigits(37), 73)    


## if staments
if 5 < 8:
    print("truuuuuu")

age = int(input('how old are you? '))
if age < 21: 
    print('im sorry you cannot be served')
else:
    print('what would u like to drink')

def can_vote(age):
    if age >= 18:
        decision = 'yes'
    else:
        decision = 'no'
    return decision

assertEqual(can_vote(17), 'no')
assertEqual(can_vote(18), 'yes')

        
