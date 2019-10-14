#Ethan Crain

def greeter():
    """This function takes input about a person's name and the time of day, 
    and returns a greeting based on that input, it also counts the number of greetings"""
    import random as rand
    count = 1 #this gives the code a base number for the number of greetings
    while True: #this while loop allows the code to ask for multiple greetings
        #these are the main variables
        first = input('What is your first name?: ')
        last = input('What is your last name?: ')
        initial = last[:1]
        time = rand.randint(1,25)
        print('The current hour is', time)
        #this part of the code determines what the output will be, based on the variable inputs
        if 5 <= time <= 10:
            print('Have a good breakfast,',first,initial)
        elif 11 <= time <=15:
            print('Have a good lunch,',first,initial)
        elif 16 <= time <= 20:
            print('Have a good dinner,',first,initial)
        else:
            print('Have a good night,',first,initial)
        #this part determines whether or not the loop restarts or ends, based on the input
        answer = input('would you like another greeting?: ')
        if answer == 'yes':
            count = count +1 #this updates the number of greetings received
            continue
        elif answer == 'no':
            break
    #this simply states how many greetings the code ran
    return 'You received '+ str(count)+ ' greetings'
    
print(greeter())