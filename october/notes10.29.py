#notes 10.29
#james Galante

##my_file = open('test.txt', 'r')
##for line in my_file:
##    line = line.rstrip('\n')
##    print(line)
##
##my_file.close()


##def read_and_make_list(my_file):
##    a = open(my_file, 'r')
##    intList = []
##    for line in a:
##        line = line.rstrip('\n')
##        intList.append(int(line))
##
##        print(intList)
##
##    a.close()
##    return intList
##
##read_and_make_list('test.txt')

'''
pypi.python.org/pypi is a really good website for
third party code
'''

##using zlib##
from zlib import compress, decompress

##data = 'the quick brown fox jumps over the lazy dog'
##
##data = data.encode()
##
##compressed = compress(data)
##print(compressed)
##
##uncompressed = decompress(compressed)
##original = uncompressed.decode()
##print()
##print(original)


#write a func to compress a file###
def comp106():
    file = input('Enter name of file to compress: ')
    in_file = open(file, 'r')
    contents = in_file.read()
    in_file.close()
    contents = contents.encode()
    compressed = compress(contents)
    out_file = open(file + '.comp', 'wb')
    out_file.write(compressed)
    out_file.close()
    
    
comp106()

def decomp106():
    file = input('Enter name of a comp file: ')
    in_file = open(file, 'rb')
    contents = in_file.read()
    in_file.close()
    uncompressed = decompress(contents)
    original = uncompressed.decode()
    out_file = open('new_' + file.rstrip('.comp'), 'w')
    out_file.write(compressed)
    out_file.close()

decomp106()
     


