try:
    with open(input('Enter the file name: '), 'r') as file:
        if  file == "na na boo boo":
            print("NA NA BOO BOO TO YOU - You have been punk'd!")
            quit()
        else:
            for line in file:
                line = line.rstrip()
                print(line.upper())
except:
        print('File cannot be opened:', file)
        quit()