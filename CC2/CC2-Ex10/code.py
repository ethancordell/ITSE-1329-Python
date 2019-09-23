G = input("Grade? ")
try:
    if 0.9<=float(G)<=1.0:
        print('A')
    elif 0.8<=float(G)<0.9:
        print('B')
    elif 0.7<=float(G)<0.8:
        print("C")
    elif 0.6<=float(G)<0.7:
        print('D')
    elif 0.0<float(G)<0.6:
        print('F')
    else:
        print("Bad Score")
except:
    print('Please enter numeric input')
    quit()