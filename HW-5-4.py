russian = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
file = []
with open('test_4.txt', 'r') as file_o:
    for i in file_o:
        i = i.split()
        file.append(russian[i[0]] + ' - ' + i[2] + '\n')
    print(file)

with open('test_4_new.txt', 'w+') as file_o_2:
    file_o_2.writelines(file)
