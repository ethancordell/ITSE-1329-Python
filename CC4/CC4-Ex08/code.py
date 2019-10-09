#   open mbox-short.txt, transform to uppercase
with open('mbox-short.txt', 'r') as file:
    for line in file:
        line = line.rstrip()
        print(line.upper())