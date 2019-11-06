#Ethan Crain

def greeter():
    """This function takes input about a person's name and the time of day, 
    and returns a greeting based on that input, it also counts the number of greetings"""
    import random as rand
    time = rand.randint(1,24)
    print('The current hour is', time)
    if 5 <= time <= 10:
        return 'Have a good breakfast,'+' '+first+' '+initial
    elif 11 <= time <=15:
        return 'Have a good lunch,'+' '+first+' '+initial
    elif 16 <= time <= 20:
        return 'Have a good dinner,'+' '+first+' '+initial
    else:
        return 'Have a good night,'+' '+first+' '+initial

counts = {'breakfast': 0, 'lunch': 0, 'dinner': 0, 'night': 0}
while True:
    first = input('What is your first name?: ')
    last = input('What is your last name?: ')
    initial = last[:1]
    print(greeter())
    answer = input('would you like another greeting?: ')
    if answer == 'yes':
        continue
    elif answer == 'no':
        for key in counts:
            counts[key] = counts.get(key, 0) +1
            print(key, counts[key])
        break
#print('You received ', str(count), ' greetings')