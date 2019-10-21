input_file = input('Enter the file name: ')
with open(input_file, 'r') as file:
    word_list = list()
    for line in file:
        words = line.split()
        for word in words:
            if not word in word_list:
                word_list.append(word)
word_list.sort()
print(word_list)