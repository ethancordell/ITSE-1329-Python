count = 0
sum = 0
while True:
    numbers = [input('Enter a number: ')]
    try:
        if numbers == 'done' :
            break
    except:
        print('Invalid input')
for number in numbers:
        count = count + 1
        sum = sum + number
print(count, sum, sum/count)