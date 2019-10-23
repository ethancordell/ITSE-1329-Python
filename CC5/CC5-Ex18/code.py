input_file = input('Enter file name: ')
file = open(input_file)
count = {}
for line in file:
    if line.startswith('From '):
        line_list = line.split()
        day = line_list[2]
        count[day] = count.get(day, 0) + 1
print(count)