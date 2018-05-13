# Searching
# linear search
from cisc106_34 import assertEqual

def linear_search(values, target):
##    count = -1
##    for x in values:
##        count += 1
##        if x == target:
##            return count

    # search through entire list from beginning to end
    for n in range(len(values)):
        if values[n] == target:
            return n     # return index if target is found

    return None
        
assertEqual(linear_search(['a', 'b', 'c', 'd', 'e', 'f'], 'c'), 2)
assertEqual(linear_search([0, 1, 2, 3, 4, 6, 7, 8, 9], 7), 6)
assertEqual(linear_search(['a', 'b', 'c', 'd', 'e', 'f'], 'z'), None)


# binary search
def binary_search(values, target):
    # initial low, high and mid
    low = 0
    high = len(values) - 1
    mid = (low + high) // 2

    # Keep looking until target is found or low and high cross
    while low <= high:
        if values[mid] == target:
            return mid              # return index if target is found
        if values[mid] < target:   # target above mid, move low
            low = mid + 1           # mid = (low + high) // 2
        else:                       # target below mid, move high
            high = mid - 1

        mid = (low + high) // 2    # recalculate mid

    return None
    
assertEqual(binary_search(['a', 'b', 'c', 'd', 'e', 'f'], 'c'), 2)
assertEqual(binary_search([0, 1, 2, 3, 4, 6, 7, 8, 9], 7), 6)
assertEqual(binary_search(['a', 'b', 'c', 'd', 'e', 'f'], 'z'), None)
       

# Timing code
# For Mac, linux, and unix, use time.time()
# For Windows, use time.clock()
import time
import random as rnd

# Create a list of size N
#N = 1000
#N = 100000
#N = 10000000
N = 100000000

start = time.time()
big_list = list(range(N))
stop = time.time()
print('Time to create list of size', N, '=', stop - start, 'seconds')

# Randomly pick a value to search for
k = rnd.randint(0, N - 1)

# Time the linear search
start = time.time()
lin_ind = linear_search(big_list, k)
lin_time = time.time() - start
print()
print('Total linear search time =', lin_time, 'seconds')
print('linear =', format(lin_ind, ',d'))

# Time the binary search
start = time.time()
bin_ind = binary_search(big_list, k)
bin_time = time.time() - start
print()
print('Total binary search time =', bin_time, 'seconds')
print('binary =', format(bin_ind, ',d'))

# How much faster is the binary serach?
print()
print('Binary search was', format(int(lin_time/ bin_time), ',d'), 'faster')
