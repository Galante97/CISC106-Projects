#James Galante, Mike Malloy

from cisc106_34 import *
from math import pi

def calculate_grade(lab_score, test_score):
    '''
    Calculate astudent's grade.
    Parameters:
        lab_score (number)
        test_score (number)
    Returns:
        grade (number)
    '''

    # calculate and return the grade
    grade = (lab_score + test_score) / 200
    return grade

assertEqual(calculate_grade(47.3, 122.5), 0.849)
assertEqual(calculate_grade(42.5, 142.7), 0.926)
assertEqual(round(calculate_grade(46.6, 131.5), 2), 0.89)
print('')


print('Problem 1')
def calculate_grade(lab_score, test_score):
     '''
    Calculate astudent's grade.
    Parameters:
        lab_score (number)
        test_score (number)
    Returns:
        grade (number)
    '''
     grade = (lab_score + test_score) / 200
     return grade



assertEqual(calculate_grade(35.1, 105.3), 0.702)
assertEqual(calculate_grade(49.9, 149.9), 0.999)
assertEqual(round(calculate_grade(40.7, 75.3), 2), 0.58)
print('')

print('Problem 2')
def calculate_trapezoid_area(base_1, base_2, height):
    '''
    calc the area of a trapazoid
    Parameters:
            base_1 (number)
            base_2 (number)
            height (number)
        Returns:
            area (number)
      '''
    trapArea = ((base_1 + base_2) / 2) * height
    return trapArea

assertEqual(calculate_trapezoid_area(1, 3, 2), 4)
assertEqual(calculate_trapezoid_area(32.0, 0.0, 4.0), 64.0)
assertEqual(round(calculate_trapezoid_area(0.14, 15.07,21.20), 2), \
161.23)

assertEqual(calculate_trapezoid_area(5, 10, 3), 22.5)
assertEqual(calculate_trapezoid_area(49.2, 10.3, 22.2), 660.45)
assertEqual(round(calculate_trapezoid_area(21.34, 17.92, 6.64), 2), \
130.34)
print('')

print('Problem 3')
def calculate_cylinder_volume(radius, height):
     '''
     this program claculates the volume of a cylinder
     parameters:
        radius
        height
     returns:
        cylinder_volume
     '''
     cylinder_volume = (pi * radius ** 2) * height

     return cylinder_volume

assertEqual(round(calculate_cylinder_volume(5 , 3), 2), \
            235.62)
assertEqual(round(calculate_cylinder_volume(13 , 5), 2), \
            2654.65)
assertEqual(round(calculate_cylinder_volume(3.1, 2.2), 2), \
            66.42)
print('')

print('Problem 4')
def make_string_strata(string1, string2):
    '''
    function takes two strings first one, bar character, second string,
    another bar character, and the first string again
    Parameters:
      string1
      string2
    Returns:
      newString
    '''
    newString = string1 + '|' + string2 + '|' + string1
    
    return newString

assertEqual(make_string_strata('bbb','a'), 'bbb|a|bbb')
assertEqual(make_string_strata('1', '23'), '1|23|1')
assertEqual(make_string_strata('Z', ''), 'Z||Z')

assertEqual(make_string_strata('x', 'B'), 'x|B|x')
assertEqual(make_string_strata('Jamba', 'Juice'), 'Jamba|Juice|Jamba')
assertEqual(make_string_strata('?', '!'), '?|!|?')
print('')

print('Problem 5')
def bill_amount(megabytes):
    '''
     This function calculates the charge for the amount of data used
     Parameteres:
        megabytes
     Return:
        charge
'''
    base = 10.00
    if 500<megabytes<2500:
        charge = (base * 1.25) + ((megabytes - 500) * 0.01)
    elif megabytes<500:
        charge = base
    elif 2500<megabytes<12500:
        charge = (base * 3.75) + (2000 * 0.01) + ((megabytes - 2500) * 0.025)

    else:
        charge = 30 * base
    return charge

assertEqual(round(bill_amount(145),2), 10)
assertEqual(round(bill_amount(920.8), 2), 16.71)
assertEqual(round(bill_amount(8607),2), 210.18)
assertEqual(round(bill_amount(15025),2), 300)

assertEqual(round(bill_amount(490),2), 10)
assertEqual(round(bill_amount(1590),2), 23.40)
assertEqual(round(bill_amount(16507),2), 300)
print('')

print('Problem 6')
def time_calculator(seconds):
     '''
     This program calculates the number of days, hours, minutes
     and seconds from a user inputed amount of seconds
     parameters:
        seconds
     returns:
        none
     '''
     days = seconds // 86400
     hours = (seconds % 86400) // 3600
     minutes = ((seconds % 86400) % 3600) // 60
     leftOverSeconds = (((seconds % 86400) % 3600) % 60) 
 
     print(days, 'days,', hours, 'hours,', minutes,
           'minutes,', leftOverSeconds,'seconds')

time_calculator(int(input('how many seconds? ')))
print('')

print('Problem 7')
def swap_2_of_3(number):
     '''
     This program takes a number between 0 and 999 and
     swaps the tens digit and the hundreds digit
     parameters:
        number
     returns:
        newNumber
     '''
     oneDigit = number % 10
     tensDigit = (number // 10) % 10
     hundredsDigit = number // 100

     newNumber = (tensDigit * 100) + (hundredsDigit * 10) + oneDigit

     return newNumber

assertEqual(swap_2_of_3(326), 236)
assertEqual(swap_2_of_3(20), 200)   
assertEqual(swap_2_of_3(7), 7)
assertEqual(swap_2_of_3(930), 390)

assertEqual(swap_2_of_3(492), 942)
assertEqual(swap_2_of_3(30), 300)   
assertEqual(swap_2_of_3(8), 8)
assertEqual(swap_2_of_3(101), 11)






     

    
