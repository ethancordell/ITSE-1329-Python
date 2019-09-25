grades = [98, 79, 85, 75, 93, 63, 82, 90, 82, 84, 74]

lowest_so_far = 100
for grade in grades:
    if grade < lowest_so_far:
        lowest_so_far = grade

print('Lowest grade is', lowest_so_far)
