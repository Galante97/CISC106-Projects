###James Galante###
###10.22.15###


####List content comparison##
list1 = [1,2,3]
list2 = [1,2,3]
##
if list1 == list2:
    print('equal')
else:
    print('not equal')


####list vs strings##
###strings can be indexed and sliced
###'symbolic'
### 01234567
###'symbolic'[4]  -> symb
###'o'#'symbolic'[0:3]  -> 'sym'
##
####string are immutable
##name = 'Reed'
###name[2] = 'a'
###will output a runtime error5
##
###this technically creates a new string
##name += ' Skillman'
##print(name)
##
###using if/for and in with strings
##string = 'this is the end.'
##
##for char in string:
##    print(char)


##def is_vowel(string):
##    vowel = ['a','e','i','o','u']
##    
##    if string in vowel:
##        print('it is a vowel')
##        Return True
##    else:
##        print('not a vowel')
##        return False
##
##is_vowel('a')
##

##sting methods
#returns true/false
#isalmun()
#isalpha()
#isdigit()
#islower()
#isspace()
#isupper()


string = 'hv383xx'

print('string', string)
print('isalmun', string.isalnum())
string = '       \n\t\t    \n\n '
print('isspace', string.isspace())



##string modification
#returns a new strong
#lower()
#lstrip()
#rstrip()
#rstrip(char)
#strip()
#strip(char)
#upper()
##
##string = "ABC, 123, do Re Me"
##print(string.lower())

## string methods
#endswith(substring)
#find(substring)
#replace(old, new)
#startswitch(substring)


##def count_vowels(string):
## #   vowel = ['a','e','i','o','u']
## #   numberOfVowels = 0
## #   string = string.lower()
##    for q in string:
##       if is_vowel(q):
##           numberOfVowels += 1
##
##    print(numberOfVowels)
##    return numberOfVowels
##    
##
##count_vowels('the dog is a dog')
##


##pluck third word
string = '     this is the end.   '
n = 0

for k in range(3):
    while string[n].isspace():
        n = n + 1
        
    start = n
   # print(start, string[start])

    while n <len(string) and not string[n].isspace():
        n = n + 1

    stop = n
   # print(stop, string[stop])

print(string[start:stop])












































