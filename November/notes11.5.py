#James Galante
#Notes 11.5

####2-dimensionsl lists####
my_list = [99,['a',[6,16,3],4.44],[True,['1','b']],'k']
print(my_list)
print()
print('mylist[1]', my_list[0])
print('mylist[2]', my_list[1])
print('mylist[3]', my_list[2])
print('mylist[4]', my_list[3])
print()
print('mylist[1][0]', my_list[1][0])
print('mylist[1][1]', my_list[1][1])
print('mylist[1][2]', my_list[1][2])
print()
print('mylist[1][1][0]', my_list[1][1][0])
print('mylist[1][1][1]', my_list[1][1][1])
print('mylist[1][1][2]', my_list[1][1][2])

###Databases###
'''
- an organized collection of data
-ex:
    library
    bank
    business
    university
'''

#using global varibles for field names
'''
TITLE = 0
AUTHOR = 1
YEAR = 2
CALL = 3

print(book[3][AUTHOR])
print(book[0][CALL])
'''
#read files and create dog database
dog_db= []

NAME = 0
BREAD = 1
AGE = 2
WEIGHT = 3

def initalize_dog_db(filename):
    dog_file = open(filename, 'r')
    #dog_db = []
    for dog in dog_file:
        dog = dog.rstrip('\n')
        dog_record = dog.split(',')
        dog_record[2] = int(dog_record[2])
        dog_record[3] = float(dog_record[3])
        #print(dog_record)
        dog_db.append(dog_record)

    #return dog_db

def main():
    dog_DB = initalize_dog_db('dog_into_list.txt')

    print('the database contains the following breads: ')
    for dog in dog_DB:
        print(dog[BREAD])

main()






