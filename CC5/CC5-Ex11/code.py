input_file = input('Enter a file name: ')
with open(input_file, 'r') as file:
    count = 0
    for lines in file:
        if lines.startswith('From'):
            count += 1
            line_list = lines.split()
            print(line_list[1])
    print('There were', count, 'lines in the file with From as the first word')