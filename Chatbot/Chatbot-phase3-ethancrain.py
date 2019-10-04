#Ethan Crain

def greeter():
    """This function takes input about a person's name and the time of day, 
    and returns a greeting based on that input, it also counts the number of greetings"""
    count = 1 #this gives the code a base number for the number of greetings
    while True: #this while loop allows the code to ask for multiple greetings
        #these are the main variables
        first = input('What is your first name?: ')
        last = input('What is your last name?: ')
        initial = last[:1]
        time = input('What time of day is it?(Morning, Afternoon, Evening): ')
        #this part of the code determines what the output will be, based on the variable inputs
        if time == 'Morning':
            print('Have a good breakfast,',first,initial)
        elif time == 'Afternoon':
            print('Have a good lunch,',first,initial)
        elif time == 'Evening':
            print('Have a good dinner,',first,initial)
        else:
            print('Have a good one,',first,initial)
        #this part determines whether or not the loop restarts or ends, based on the input
        answer = input('would you like anorher greeting?: ')
        if answer == 'yes':
            count = count +1 #this updates the number of greetings received
            continue
        elif answer == 'no':
            break
    #this simply states how many greetings the code ran
    return 'You received '+ str(count)+ ' greetings'
    
print(greeter())