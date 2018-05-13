###James Galante###
###10.27.15###

###file i/o
'''
my_file = open(<filename>, <mode>)
file name is name of the file
mode is 'r', 'w', 'a'
r - read: see contents of file
w - write: will overwrite a file if name already exists
a - append: for appending to an existing file
my_file.close()
####
my_file.write('here is some text')
    - only writes strings
the_entire_file  = my_file.read()
    - reads entire file and stores it in a string
###when writing to a fiele, you need to incllude a newline character
    '\n' at the end of each line
'''

#write mode
my_file = open('test.txt', 'w')
my_file.write('this is a simple test string')
my_file.close()

#read mode
my_file = open('test.txt', 'r')
contents = my_file.read()
print(contents)
my_file.close()

#append mode
my_file = open('test.txt', 'a')
my_file.write('\nadd this text to the end of the file...\n')

my_file = open('test.txt', 'r')
contents = my_file.read()
print(contents)
my_file.close()

#using readline()
my_file = open('test.txt', 'r')
line = my_file.readline()
line = line.rstrip('\n')
print(line)
line = my_file.readline()
line = line.rstrip('\n')
print(line)
line = my_file.readline()
line = line.rstrip('\n')
print(line)

my_file.close()

#reading line in a loop
my_file = open('test.txt', 'r')

line = my_file.readline()
while line != '':
    line = line.rstrip()
    print(line)
    line = my_file.readline()

my_file.close()

#easier way to read line from a file
my_file = open('test.txt','r')
for line in my_file:
    line = line.rstrip('\n')
    print(line)

my_file.close()

def read_and_make_list(my_file):
    line = my_file.readline()
    




























