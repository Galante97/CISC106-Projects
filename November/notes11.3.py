#James Galante
#Notes 11.3

#using matplotlib.pyplot as plt
import matplotlib.pyplot as plt

###plotting with pyplot
##plt.plot([1,2,3,4], 'ro')
##plt.show()

###x vs y
##plt.plot([1,2,3,4],[1,4,9,16],'b--')
##plt.show()

###plotting multiple curves
##x = [1,2,3,4,5]
##y1 = x
##y2 = [1,4,9,16,25]
##y3 = [1,8,27,64,125]
##plt.plot(x,y1,'r^-',x,y2,'go-',x,y3,'bs--')
##plt.show()

###setting the axes
##plt.axis([0,6,0,150])
##x = [1,2,3,4,5]
##y1 = x
##y2 = [1,4,9,16,25]
##y3 = [1,8,27,64,125]
##plt.plot(x,y1,'r^-',x,y2,'go-',x,y3,'bs--')
##plt.show()

# other plot types
# plt.semology()
# plt.loglog()

###adding axis labels
##plt.title('THIS IS THE TITLE')
##plt.xlabel('list index')
##plt.ylabel('list value')
##plt.plot([1,2,3,4],'r^-')
##plt.show()

###pie chart
##data = [20,26,17,6,5]
##plt.title('pie chartsss')
##plt.pie(data)
##plt.show()


#####creating a histogram
##data = [20,26,17,6,5]
##plt.hist(data)
##plt.show()

#####creating a histogram with bins specidied
##data = [20,26,17,6,5]
##bins = [0,5,10,15,20,25,30]
##plt.axis([0,30,0,5])
##plt.hist(data,bins)
##plt.show()

#histogram of standard normal distribtuoin
##import random
##n_points = 1000
##x_list = []
##y_list = []
##for n in range(n_points):
##    x_list.append(random.normalvariate(0.0,1.0))
##    y_list.append(random.normalvariate(0.0,1.0))
##
###plt.hist(x_list)
###plt.hist(x_list,250)
###plt.hist(x_list,100, cumulative = True)
###plt.show()
##
###other plot types
###scatter()
###stacked()
###bar()
###barh()
##
##plt.scatter(x_list, y_list)
##plt.show()


###legends
##plt.axis([0,6,0,150])
##x = [1,2,3,4,5]
##y1 = x
##y2 = [1,4,9,16,25]
##y3 = [1,8,27,64,125]
##plt.axis([0,6,0,150])
##plt.xlabel('xlabel')
##plt.ylabel('ylabel')
##plt.plot(x,y1,'r^-',x,y2,'go-',x,y3,'bs--')
##plt.legend(['x','x^2','x^3'], loc = 'best')
##plt.show()

###RECURSION####
##def countdown_nr(n):
##    for count in range(n,0,-1):
##        print(count)
##
##    print('balst offf')
##
##
##
##def countdown(n):
##    #check of base case
##    if n == 0:
##        print('blastoff')
##        return
##
##    #handle the recursive case
##    print(n)
##    countdown(n-1)
##    
##countdown(10)
##
### recursive factorial (n!)
##def factroial(n):
##    #check for the base case
##    if n == 0:
##        return 1
##    #handle the recursive case
##    # n! = n*(n-1)!
##    # n! = n * factroial(n-1)
##    return n * factroial(n-1)
##
##k = 1000
##print(k, '!=', factroial(k), sep = '')
##

#recursive fibonacci sequence
def fibonacci(n):
    #check for base case
    if n == 0:
        return 0
    elif n == 1:
        return 1

    #handle the recursive case
    #F(n) = f(n - 1) + F(n - 2)
    #F(n) = fibonacci(n - 1) + fibonacci(n - 2)
    return fibonacci(n - 1) + fibonacci(n - 2)




for k in range(25):
    print('F(',k,') =', fibonacci(k), sep = '')


















