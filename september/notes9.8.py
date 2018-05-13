num = '12'

print(num)
print(int('12'))
print(12 // 3)

#we typically use int(), Float(), and str() like this
num = '12'
num = int(num)

#operator precedence and associativity
print(2 + 3 * 5 - 4 / 2)
print(2 + 3 * (5 - 4) / 2)
print(2 + 3 ** 2 * 5 - 4 / 2)
print((2 + 3) ** 2 * 5 - 4 / 2)

#division
print(4 / 3)
print (4 // 3)

#remainder
print(5 % 2)
print(-5 % 3)
print(-5 % -3)
print(5 % -3)

#type of convesion (implicit, coercion)
print(1+2)
print(type(1.+2))

#formatting numbers with format()
#floating point format
fraction = 5/3
print(fraction)
print(format(fraction, 'f'))
print(format(fraction, '.2f'))
print(format(fraction, '15.2f'))
print(format(100000 + fraction, '15,.2f'))

#exponential format
print(format(100000 + fraction, 'e'))
print(format(100000 + fraction, '18.3e'))

#pecentage format
print(format(fraction, "%"))
print(format(100000 + fraction, "18,.0%"))

#integer format
print(format(9189, 'd'))
print(format(9189, '8d'))
print(format(9189, ',d'))
print(format(9189, '8,d'))

print(1)
print(2)
print(3)


