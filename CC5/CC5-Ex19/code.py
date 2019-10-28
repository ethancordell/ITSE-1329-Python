input_file = input('Enter file name: ')
file = open(input_file)
count = {}
for line in file:
    if line.startswith('From '):
        line_list = line.split()
        email = line_list[1]
        count[email] = count.get(email, 0) + 1
print(count)