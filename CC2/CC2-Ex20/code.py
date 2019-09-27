smallest = None
largest = None
while True:
    numbers = input('Enter a number: ')
    if numbers == 'done' :
            break
    try:
        number_int = int(numbers)
        if smallest is None:
            smallest = number_int
        elif number_int < smallest:
            smallest = number_int
        elif largest is None:
            largest = number_int
        elif largest < number_int:
            largest = number_int
    except:
        print('That is not a number')
print(smallest, largest)