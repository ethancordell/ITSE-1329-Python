h = input('Hours? ')
r = input('Rate? ')
try:
    if float(h) > 40:
        ot = float(h)-40
        otr = float(r)*1.5
        otpay = 40*float(r)+float(ot)*float(otr)
        print('Pay', float(otpay))
    else:
        pay = float(h)*float(r)
        print("Pay:", float(pay))
except:
    print('Error, please enter numeric input')
    quit()