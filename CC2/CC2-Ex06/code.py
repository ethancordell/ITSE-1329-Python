G = input("Grade? ")
if 0.9<=float(G)<=1.0:
    print('A')
if 0.8<=float(G)<0.9:
    print('B')
if 0.7<=float(G)<0.8:
    print("C")
if 0.6<=float(G)<0.7:
    print('D')
if 0.0<float(G)<0.6:
    print('F')
if 0.0>float(G):
    print("Bad Score")
if 1.0<float(G):
    print("Bad Score")