#Ethan Crain

def greeter():
    """This function takes input about a person's name and the time of day, 
    and returns a greeting based on that input, it also counts the number of greetings"""
    import random as rand
    time = rand.randint(1,24)
    print('The current hour is', time)
    if 5 <= time <= 10:
        print('Have a good breakfast,', first, initial)
    elif 11 <= time <=15:
        print('Have a good lunch,', first, initial)
    elif 16 <= time <= 20:
        print('Have a good dinner,', first, initial)
    else:
        print('Have a good night,', first, initial)
count=1
while True:
    first = input('What is your first name?: ')
    last = input('What is your last name?: ')
    initial = last[:1]
    print(greeter())
    answer = input('would you like another greeting?: ')
    if answer == 'yes':
        count = count +1
        continue
    elif answer == 'no':
        break
print('You received ', str(count), ' greetings')