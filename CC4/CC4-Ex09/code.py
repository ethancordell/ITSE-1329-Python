file = input('Enter the file name: ')
if file == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    quit()
else:
    try:
        if file == 'mbox-short.txt':
            with open('mbox-short.txt', 'r') as file1:
                for line in file1:
                    line = line.rstrip()
                    print(line.upper())
        else:
            quit()
    except:
        print('File cannot be opened:', file)
        quit()