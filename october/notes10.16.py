#James Galante
#10.15.15

#boolean flags
word_list = ['cat', 'dog', 'pig', 'horse', 'zebra', 'cow']

##zebra = False   # <---- bool flag
##for word in word_list:
##    if word == 'zebra':
##        zebra =  True
##
##if zebra == True:
##    print('zebra is true')
##else:
##    print('not true')

n = int(input('enter int greater than one: '))
prime = True
for k in range(2, int(n ** 0.5) + 1,):
    if n % k == 0:
        prime = False

if prime:
    print(n, 'is prime')
else:
    print(n, 'is not prime')
