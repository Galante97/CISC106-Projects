#James Galante
#10.8.15

convert_calls = 0

#nested for loop
for i in range(4):
    print('\n')
    for j in range(3):
        print (i, '*', j, '=', i * j, '\t', end = '')
        #global convert_calls + 1
        print(convert_calls)

x = 5
if type(x) == int:
    print('you good its a int')
else:
    print('nah man')
