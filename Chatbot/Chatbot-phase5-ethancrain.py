#Ethan Crain

def greeter():
    """This function takes input about a person's name and the time of day, 
    and returns a greeting based on that input, it also counts the number of greetings"""
    import random as rand
    time = rand.randint(1,24)
    print('The current hour is', time)                          #Lines 6,7,and 8 use randint to determine the time of day.
    if 5 <= time <= 10:                                         #Lines 9 through 24 determine the greeting and add to the histogram based on the time of day.
        meal = 'Breakfast'
        count[meal] = count.get(meal, 0) +1
        return 'Have a good breakfast,'+' '+first+' '+initial
    elif 11 <= time <=15:
        meal = 'Lunch'
        count[meal] = count.get(meal, 0) +1
        return 'Have a good lunch,'+' '+first+' '+initial
    elif 16 <= time <= 20:
        meal = 'Dinner'
        count[meal] = count.get(meal, 0) +1
        return 'Have a good dinner,'+' '+first+' '+initial
    else:
        meal = 'Night'
        count[meal] = count.get(meal, 0) +1
        return 'Have a good night,'+' '+first+' '+initial

count = {}                                                      #This creates the dictionary for the histogram.
while True:                                                     #This loop creates the variables, calls the greeter function, and prints the histogram.
    first = input('What is your first name?: ')
    last = input('What is your last name?: ')
    initial = last[:1]
    print(greeter())
    answer = input('would you like another greeting?: ')
    if answer == 'yes':
        continue
    elif answer == 'no':
        for k,v in count.items():
            print(k,v)
        break