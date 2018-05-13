def get_valid_input():
    user_input = ''
    while user_input != 'e':
        user_input = input('choice: ')
        if user_input == 'i':
            return 'i'
            
        elif user_input == 'd':
            return 'd'
            
        elif user_input == 'm':
            return 'm'
            
        elif user_input == 'e':
            return 'e'
            
        else:
            print('Error invalid choice')        


print(get_valid_input())
