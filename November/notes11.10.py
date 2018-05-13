#Notes 11.10.15


# List funny business
# simple (atomic) variables
x = 5
y = x
print(x, y)

x = 7
print(x, y)

# Need to declare x as global to change the global x from 7 to 9.
def my_function():
    global x
    x = 9

my_function()
print(x, y)

# complex variables (lists, tuples)
list_1 = [1, 2, 3]
list_2 = list_1
print(list_1, list_2)

list_1.append(4)
print(list_1, list_2)

list_1 = ['a', 'b', 'c']
print(list_1, list_2)

list_1.insert(2, '(b + c) / 2')
print(list_1, list_2)

# If we modify list_1 with a list method, we do _NOT_ need to declare list_1
# as global to modify the global list_1 variable.
def my_list_function():
    list_1.append('d')

my_list_function()
print(list_1)

# If we use addition, or augmented addition, we need to declare list_1 as
# global to cahnge the global list_1 variable.
def my_list_function():
    global list_1
    #list_1.append('d')
    list_1 = list_1 + ['e']
    list_1 = [True, False, None]

my_list_function()
print(list_1)
