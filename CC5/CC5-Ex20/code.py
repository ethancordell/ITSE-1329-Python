input_file = input('Enter file name: ')
file = open(input_file)
counts = {}
for line in file:
    if line.startswith('From '):
        line_list = line.split()
        email = line_list[1]
        counts[email] = counts.get(email, 0) + 1
most_count = None
most_email = None
for email , count in counts.items():
    if most_count is None or count > most_count:
        most_email = email
        most_count = count
print(most_email, most_count)