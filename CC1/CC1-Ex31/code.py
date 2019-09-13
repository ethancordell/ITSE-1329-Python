str = 'X-DSPAM-Confidence:0.8475'
pos = str.find('0')
new = str[pos:]
print(float(new))