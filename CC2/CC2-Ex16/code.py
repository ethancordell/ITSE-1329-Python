grades = [98, 79, 85, 75, 93, 63, 82, 90, 82, 84, 74]

highest_so_far = -1

for grade in grades:
    if grade > highest_so_far:
        highest_so_far = grade

print('Highest grade is', highest_so_far)
