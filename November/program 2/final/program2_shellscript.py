Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 23 2015, 02:52:03) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 

    First enter 'r' for read and merge then pick another choice:
        d: delete a record
        f: find a record
        i: insert a record
        p: print the database
        r: read and merge
        q: query grades and section
        c: chart grades
        e: exit the program
        
choice: r
Input the name of your first file: sample-r1.txt
Input the name of your second file: sample-r2.txt
List has been merged and sorted

    First enter 'r' for read and merge then pick another choice:
        d: delete a record
        f: find a record
        i: insert a record
        p: print the database
        r: read and merge
        q: query grades and section
        c: chart grades
        e: exit the program
        
choice: i
Enter last name of new person: Galante
Enter first name of new person: James
Enter section number of new person (20-23): 22
Enter grade of new person (0-100): 97
your new record is:  ['James', 'Galante', 22, 97.0]

    First enter 'r' for read and merge then pick another choice:
        d: delete a record
        f: find a record
        i: insert a record
        p: print the database
        r: read and merge
        q: query grades and section
        c: chart grades
        e: exit the program
        
choice: i
Enter last name of new person: Clinton
Error: Last name already exists

    First enter 'r' for read and merge then pick another choice:
        d: delete a record
        f: find a record
        i: insert a record
        p: print the database
        r: read and merge
        q: query grades and section
        c: chart grades
        e: exit the program
        
choice: d
Delete
Enter last name of person on record (case sensitive): Clinton
[['Bud', 'Abbott', '21', '92.3'], ['Don', 'Adams', '21', '90.4'], ['Mary', 'Boyd', '22', '91.4'], ['Jill', 'Carney', '23', '76.3'], ['James', 'Galante', 22, 97.0], ['Diane', 'Keaton', '20', '61.1'], ['Randy', 'Newman', '20', '41.2']]

    First enter 'r' for read and merge then pick another choice:
        d: delete a record
        f: find a record
        i: insert a record
        p: print the database
        r: read and merge
        q: query grades and section
        c: chart grades
        e: exit the program
        
choice: d
Delete
Enter last name of person on record (case sensitive): Smith
Error: Record does not exist

    First enter 'r' for read and merge then pick another choice:
        d: delete a record
        f: find a record
        i: insert a record
        p: print the database
        r: read and merge
        q: query grades and section
        c: chart grades
        e: exit the program
        
choice: f
Enter last name of person on record (case sensitive): Galante
The record is:  ['James', 'Galante', 22, 97.0]

    First enter 'r' for read and merge then pick another choice:
        d: delete a record
        f: find a record
        i: insert a record
        p: print the database
        r: read and merge
        q: query grades and section
        c: chart grades
        e: exit the program
        
choice: f
Enter last name of person on record (case sensitive): Smith
Error: record not found

    First enter 'r' for read and merge then pick another choice:
        d: delete a record
        f: find a record
        i: insert a record
        p: print the database
        r: read and merge
        q: query grades and section
        c: chart grades
        e: exit the program
        
choice: q
Query Grades and Section
Please enter query type (g or s): g
enter a grade threshold from [0.0-100.0]: 75
['Bud', 'Abbott', '21', '92.3']
['Don', 'Adams', '21', '90.4']
['Mary', 'Boyd', '22', '91.4']
['Jill', 'Carney', '23', '76.3']
['James', 'Galante', 22, 97.0]

    First enter 'r' for read and merge then pick another choice:
        d: delete a record
        f: find a record
        i: insert a record
        p: print the database
        r: read and merge
        q: query grades and section
        c: chart grades
        e: exit the program
        
choice: q
Query Grades and Section
Please enter query type (g or s): g
enter a grade threshold from [0.0-100.0]: 110
error: grade threshold out of range

    First enter 'r' for read and merge then pick another choice:
        d: delete a record
        f: find a record
        i: insert a record
        p: print the database
        r: read and merge
        q: query grades and section
        c: chart grades
        e: exit the program
        
choice: q
Query Grades and Section
Please enter query type (g or s): s
enter a grade threshold from [20-23]: 22
['Mary', 'Boyd', '22', '91.4']
['James', 'Galante', 22, 97.0]

    First enter 'r' for read and merge then pick another choice:
        d: delete a record
        f: find a record
        i: insert a record
        p: print the database
        r: read and merge
        q: query grades and section
        c: chart grades
        e: exit the program
        
choice: q
Query Grades and Section
Please enter query type (g or s): s
enter a grade threshold from [20-23]: 25
error: section threshold out of range

    First enter 'r' for read and merge then pick another choice:
        d: delete a record
        f: find a record
        i: insert a record
        p: print the database
        r: read and merge
        q: query grades and section
        c: chart grades
        e: exit the program
        
choice: p
['Bud', 'Abbott', '21', '92.3']
['Don', 'Adams', '21', '90.4']
['Mary', 'Boyd', '22', '91.4']
['Jill', 'Carney', '23', '76.3']
['James', 'Galante', 22, 97.0]
['Diane', 'Keaton', '20', '61.1']
['Randy', 'Newman', '20', '41.2']

    First enter 'r' for read and merge then pick another choice:
        d: delete a record
        f: find a record
        i: insert a record
        p: print the database
        r: read and merge
        q: query grades and section
        c: chart grades
        e: exit the program
        
choice: e
Thank you and goodbye!
>>> 
