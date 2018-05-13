#James Galante, Mike Malloy

first_name = 0
last_name = 1
section = 2
grade = 3

list1 = []
list2 = []
sorted_list = []

import matplotlib.pyplot as plt


def delete():
    '''
    This program finds a record and then deletes based
    on last name
    parameters:
      N/a
    returns:
      N/a
    '''
    print('Delete')

    contains_record = False
    x = 0
    
    delete_this = input('Enter last name of person on record (case sensitive): ')

    for i in range(len(sorted_list)):
        if delete_this == sorted_list[i][last_name]:
            x = i
            contains_record = True
            break
        else:
            continue

    if contains_record == True:
        sorted_list.remove(sorted_list[x])
        print(sorted_list)
        contains_record = False
        
    else:
        print('Error: Record does not exist')

    
def find_record():
    '''
    Query the user for a last name then verifies that a record
    containing last name exists in the database and prints the record,
    If not it prints a meaningful error message
    parameters:
      N/a
    returns:
      N/a
    '''

    find_this = input('Enter last name of person on record (case sensitive): ')

    x = ''

    for i in range(len(sorted_list)):
        if find_this == sorted_list[i][last_name]:
            print('The record is: ', sorted_list[i])
            x = sorted_list[i]
            break
        else:
            continue
    if x == '':
        print('Error: record not found')
    
def insert_record():
    '''
    This program promts the user to input a new record
    and adds it to the list and sorts it
    parameter:
     N/A
    returns:
     N/A
    '''
    global sorted_list
    temp_list = sorted_list
    
    new_record = []
    last = input('Enter last name of new person: ')
    for i in range(len(sorted_list)):
        if last == sorted_list[i][last_name]:
            print('Error: Last name already exists')
            return        

    first = input('Enter first name of new person: ')
    n_section = input('Enter section number of new person (20-23): ')
    n_section = int(n_section)
    if n_section > 23 or n_section < 20:
        print('Error: section out of range')
        return
    
    n_grade = input('Enter grade of new person (0-100): ')
    n_grade = float(n_grade)
    if n_grade > 100 or n_grade < 0:
        print('Error: grade out of range')
        return
         
    new_record.append(first)
    new_record.append(last)
    new_record.append(n_section)
    new_record.append(n_grade)

    temp_list.append(new_record)
    
    sorted_list = []
    #sort the lists
    while temp_list:
        minimum = temp_list[0] # arbitrary number in list 
        for x in temp_list:
            if x[last_name] < minimum[last_name]:
                minimum = x
        sorted_list.append(minimum)
        temp_list.remove(minimum)

    print("your new record is: ", new_record)

    
    
def print_database():
    '''
    prints the database one record at a time
    parameters:
      N/a
    returns:
      N/a
    '''
    for elem in sorted_list:
        print(elem)
    

def read_merge():
    '''
     This function takes two files that the user inputs
    and creates two seperate databases in list form
    '''

    file1 = input('Input the name of your first file: ')
    file2 = input('Input the name of your second file: ')

    a = open(file1, 'r')
    b = open(file2, 'r')

    #split the people apart in each list
    for person in a:
        person = person.rstrip('\n')
        personRecord = person.split(' ')
        personRecord[2] = str(personRecord[2])
        personRecord[3] = str(personRecord[3])

        list1.append(personRecord)

    for person in b:
        person = person.rstrip('\n')
        personRecord = person.split(' ')
        personRecord[2] = str(personRecord[2])
        personRecord[3] = str(personRecord[3])

        list2.append(personRecord)

    #merge the lists
    list_merged = list1 + list2

    #sort the lists
    while list_merged:
        minimum = list_merged[0] # arbitrary number in list 
        for x in list_merged:
            if x[last_name] < minimum[last_name]:
                minimum = x
        sorted_list.append(minimum)
        list_merged.remove(minimum)  

    print('List has been merged and sorted') 
           
    
   
def query_grades_section():
    '''
    This program asks for user input and queries the list for
    records higher the the grade/section thresehold
    parameters:
     N/A
    returns:
     N/A
    '''
    print('Query Grades and Section')
    user_input = input('Please enter query type (g or s): ')
    if user_input == 'g':

        g_input = input('enter a grade threshold from [0.0-100.0]: ')
        if float(g_input) > 100 or float(g_input) < 0.0:
            print('error: grade threshold out of range')
            return

        for item in sorted_list:
            if float(item[grade]) >= float(g_input):
                print(item)
            else:
                continue
                
    elif user_input == 's':
        s_input = input('enter a grade threshold from [20-23]: ')
        if int(s_input) > 23 or int(s_input) < 20: 
            print('error: section threshold out of range')
        for item in sorted_list:
            if int(item[section]) == int(s_input):
                print(item)
            else:
                continue
    else:
        print('error invalid input')

def chart_grades():
    '''
    This program takes the grades in the database and graphs them
    on a pie chart
    paramters:
     N/A
    returns:
     N/A
    '''
    print('chart grades')
    grades_list = []
    for i in range(len(sorted_list)):
        x = sorted_list[i][grade]
        grades_list.append(x)

    A = 0
    B = 0
    C = 0
    D = 0
    F = 0
    for i in range(len(grades_list)):
        if float(grades_list[i]) >= 90.:
            A = A+1
        if 80. <= float(grades_list[i]) < 90.:
            B = B+1
        if 70. <= float(grades_list[i]) < 80.:
            C = C+1
        if 60. <= float(grades_list[i]) < 70.:
            D = D+1
        if 0. <= float(grades_list[i]) < 60.:
            F = F+1

    labels1 = 'A','B','C','D','F'
    list_letter_grades = [A,B,C,D,F]
    plt.pie(list_letter_grades, labels =labels1, autopct='%1.1f%%')
    plt.title('Grades')
    plt.show()
            

    
    #plt.pie(sorted_list[3])

def exit_program():
    '''
    This exits the program
    parameters:
     N/A
    Returns
     N/A
    '''
    print('Thank you and goodbye!')
    exit


def menu():
    print('''
    First enter 'r' for read and merge then pick another choice:
        d: delete a record
        f: find a record
        i: insert a record
        p: print the database
        r: read and merge
        q: query grades and section
        c: chart grades
        e: exit the program
        ''')


def main():
    user_input = ''
    while user_input != 'e':
        menu()
        user_input = input('choice: ')
        if user_input == 'd':
            delete()
            
        elif user_input == 'f':
            find_record()
            
        elif user_input == 'i':
            insert_record()
            
        elif user_input == 'p':
            print_database()
            
        elif user_input == 'r':
            read_merge()
            
        elif user_input == 'q':
            query_grades_section()

        elif user_input == 'c':
            chart_grades()
            
        elif user_input == 'e':
            exit_program()
            
        else:
            print('Error invalid choice')        

main()








