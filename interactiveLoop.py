# interactive loop
exit = False

while exit == False:
    user_input = input("Type a, b or quit: ")
    
    if user_input == 'quit':
        exit = True
    elif user_input == 'a':
        print('you entered', user_input)
    elif user_input == 'b':
        print('you entered', user_input)
