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

    print(sorted_list) 
