#   open alice.txt, print lines that startwith
#   'Alice' and print out result with right-hand whitespace
#   removed
with open('alice.txt', 'r') as file:
    for line in file:
        line = line.rstrip()
        if line.startswith('Alice'):
            print(line)