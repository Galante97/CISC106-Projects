#James Galante, Mike Malloy

def delete():
    print('Delete')
def find_record():
    print('Find Record')
def insert_record():
    print('Insert Record')
def print_database():
    print('Print Database')


first_name = 0
last_name = 1
section = 2
grade = 3

list1 = []
list2 = []

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

    #print out the list
    for x in list1:
        print(x)
    for x in list2:
        print(x)

           
    
   
def query_grades_section():
    print('Query Grades and Section')
def exit_program():
    print('Exit Program')


def menu():
    print('''
    First enter 'r' for read and merge then pick another choice:
        d: delete a record
        f: find a record
        i: insert a record
        p: print the database
        r: read and merge
        q: query grades and section
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
            
        elif user_input == 'e':
            exit_program()
            
        else:
            print('Error invalid choice')        

main()









