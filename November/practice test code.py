##def f(n,m):
##    if n >= m:
##        return n + m
##    else:
##        return 1 + f(n + 1, m - 2)
##
##print(f(3,7))

##L = [3,2,4,1]
##for i in range(len(L)):
##    total = L[i] - L[i - 1]
##    print(total)

##def mixed(b,c,d,e):
##    print(e,d,c,b)
##    return
##
##y = mixed(5,4,e=3,d=6)

##list1 = [4,6,8]
##list2 = [3,7,9,12]
##for m in list2:
##    list1 = [m] + list1
##print(list1)

##x = [[0,5,2,1],[4,2,4,7],[8,9,1,2],[-2,-3,6,7]]

##print(x[3][1])
##print(x[1][0])

##for j in range(2,3):
##    for k in range(2):
##        print(x[j][k])

##for j in [3,1]:
##    print(x[j])

fruit = 'orange'

##print(fruit[3])
##print(fruit[2:5])
##print(fruit[1:6:2])

##def f(x):
##    string = '0123456789ABCDEF'
##    if 0 <= x and x <= 15:
##        return string[x]
##    else:
##        return
##
##print(f(11))

##def function1(a):
##        print(a)
##        function2(a)
##
##def function2(b):
##    b = b+1
##    function1(b)
##
##function1(0)



##def f(k):
##    if type(k) != int or k < 1:
##        print('k must be a postive int')
##        return None
##
##    if k == 1:
##        return 1
##    else:
##        
##        return k ** 2 + f(k - 1)
##
##print(f(3))


##def g(x):
##    if x == 0:
##        return 5
##    elif x == 1:
##        return 3
##    elif x >= 2:
##        return g(x-2) - g(x-1)
##
##print(g(5))


def get_valid_input():
    user_input = ''
    while user_input != 'e':
        user_input = input('choose i, d,m,e: ')
        if user_input == 'i':
            print('i')
        elif user_input == 'd':
            print('d')
        elif user_input == 'm':
            print('m')
        elif user_input == 'e':
            print('e')
            exit
        else:
            print('error: wrong choice try again')

get_valid_input()











