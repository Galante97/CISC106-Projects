###James Galante
###9.29
##
###global varibles are defined outside of all functions
###global variables are visible every where inside the file
###global variable cannot be changed inside of functionss
###unless they are declared with the global constant
##
###global varibles and the global keyword
##tax_rate = 0.05
##
##def calculate_tax(price):
##
##    #GLOBAL KEYWORD 'global'
##    
##    global tax_rate = 0.10
##    tax = price * tax_rate
##    return tax
##
##cost = 33.0
##total_cost = cost + calculate_tax(cost)
##print('total cost', total_cost)
##print('the tax rate is', tax_rate)
##\
##'''
###program 1
##menu driven program taht
##tests students on basic math skills (see porgram 5-28 in text).
##    - you will need to write many functions
##    - bool expressions
##    - if elif conditionals
##    - while and for loops
##'''
###while statements
##'''
##while <boolean expression>:
##    <python statemet>
##    <python statemet>
##    <python statemet>
##'''
##
###ex:
##count = int(input( 'enter a number '))
##
##while count >= 0:
##    print(count)
##    count = count - 1
##
###ex2:
##answer = 'yes'
##
###while answer == 'yes':
##while answer == 'yes' or answer =='Yes':
##    x = float(input('enter a number '))
##    print('the square of', x, 'is', x * x)
##
##    answer = input('keep going? ')
##
##
##while True:
##    print('inifinte loop')
##
###contrl-c to kill an infinite loop
##
##
##
###collatz c0njecture
##
##
##def sequence(n):
##    while n > 1:
##        print(n)
##        if (n % 2 == 0):
##             n = n / 2
##        else:
##             n = 3*n+1
##   
##    print(n)
##
##n = int(input('enter a number '))
##sequence(n)
##
##
###input testing
##def sequence(n):
##    while n > 1:
##        print(n)
##        if (n % 2 == 0):
##             n = n / 2
##        else:
##             n = 3*n+1
##   
##    print(n)
##
##
####TESTING
##n = int(input('enter a postive number '))
##while n < 1:
##    print(n, 'is not a postive integer')
##    n = int(input('enter a postive number '))
##    
##sequence(n)



answer = 'yes'

while answer == 'yes' or answer =='Yes':
    x = float(input('enter a number '))
    print('the square of', x, 'is', x * x)

    answer = input('keep going? (yes or no) ')

#TESTING
    while answer !='yes' and answer !='no':
        print('please answer yes or no')
        answer = input('keep going? (yes or no) ')





















    
