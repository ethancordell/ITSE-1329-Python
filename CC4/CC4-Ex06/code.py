#   open mbox-short.txt, print lines that startwith
#   From: and print out result with right-hand whitespace
#   removed
with open('mbox-short.txt', 'r') as file:
    for line in file:
        line = line.rstrip()
        if line.startswith('From:'):
            print(line)