##record = [[10, 'tom', 14.7, True],
## [14, 'sue', 37.5, False],
## [15, 'joe', 55.3, False],
## [16, 'james', 55.3, True],
## [17, 'matt', 55.3, False],
## [18, 'stephan', 55.3, False],
## [19, 'cathlean', 55.3, False],
## [20, 'cassandra', 55.3, True],
## [100, 'chris', 55.3, False],
## [22, 'poop', 55.3, False],
## [23, 'bob', 55.3, True],
## [24, 'quad', 55.3, False],
## [25, 'de', 55.3, True],
## [26, 'jule', 55.3, False],
## [27, 'apples', 55.3, False],
## [28, 'peasnuts', 55.3, True],
## [29, 'dietlin', 55.3, False],
## [33, 'qud', 46.2, False],
## [48, 'er', 37.5, True]]
##
####
########1#####
####for i in record:
####    print(i[0], i[1])
####
####print()
####
#########2#####
####for i in record:
####    i = [i[0], i[1]]
####    print(i)
####
####print()
####
#########3#####
####for i in record:
####    if i[3] == False:
####        print(i)
####
#########4#####
####for i in record:
####    if i[3] == False:
####        i = [i[0], i[1], i[3]]
####        print(i)
##
###print()
#######5#####
##record = sorted(record, key=lambda x: x[1])
##print(record)


student_record = [['Brooks', 'Kim', 718337185, 18, 0.0, 'Christopher', 'Dhristopher', 'freshman'],
  ['Daniels', 'Chester', 797701002, 18, 8220.01, 'Charlie', 'Beverly', 'freshman'],
  ['Daniels', 'Chris', 810199144, 20, 0.0, 'Jack', 'Clair', 'senior'],
  ['Jones', 'Joe', 700157834, 19, 17395.57, 'Daniel', 'Susan', 'junior'],
  ['Jowenstern', 'Ike', 877377100, 21, 813.3, 'Jacob', 'Laura', 'senior'],
  ['Updegrave', 'Douglas', 711922910, 19, 0.0, 'Philip', 'Leticia', 'sophomore']]



##1##
#for i in student_record:
#    print(i)

##2##
##for i in student_record:
##    if i[7] == 'senior':
##        print(i)

####3##
##for i in student_record:
##    if i[3] > 19 and i[0][0] == 'J':
##        print(i)        

###4###

for i in student_record:
    if i[4] > 0.0:
        print(i[2])

##5##
for i in student_record:
    if i[3] < 20:
        print(i[1], i[0])

##6#
for i in student_record:
    if i[7] == 'freshman' and len(i[1]) == 3:
       if i[5] < i[6]:
            print(i[5])
       else:
            print(i[6])
        









    








