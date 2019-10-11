with open(input('Enter the file name: '), 'r') as file:
    count = 0
    total = 0
    for line in file:
        if line.startswith('X-DSPAM-Confidence:'):
            count = count + 1
            linenum = float(line[20:])
            total = total + linenum
print('Average spam confidence:', total/count)