count = 0
sum = 0
while True:
    numbers = input('Enter a number: ')
    if numbers == 'done' :
            break
    try:
        number_int = int(numbers)
        count = count + 1
        sum = sum + number_int
    except:
        print('Invalid input')
average = sum/count
print(sum, count, average)