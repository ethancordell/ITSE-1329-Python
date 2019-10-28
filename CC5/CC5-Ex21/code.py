input_file = input('Enter file name: ')
file = open(input_file)
count = {}
for line in file:
    if line.startswith('From '):
        line_list = line.split()
        email = line_list[1]
        email_part = email.split('@')
        where = email_part[1]
        count[where] = count.get(where, 0) + 1
print(count)