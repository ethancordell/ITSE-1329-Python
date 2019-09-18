hours = input('Hours? ')
if hours > 40:
    rate = input('Rate? ')*1.5
    pay = int(hours)*int(rate)
    print("Pay:", float(pay))
else:
    rate = input('Rate? ')
    pay = int(hours)*int(rate)
    print("Pay:", float(pay))