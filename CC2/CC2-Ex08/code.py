h = input("What is your height in inches? ")
try :
    if int(h) >= 42:
        print('Welcome aboard, enjoy the ride!')
    else:
        print('Sorry, you are not tall enough for this ride')
except :
    print('That is not a valid number')