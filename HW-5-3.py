with open('test_3.txt', 'r') as file:
    test_3 = []
    low = []
    my_list =  file.read().split('\n')
    for thief in my_list:
        i = thief.split()
        if int(i[1]) < 20000:
           low.append(i[0])
        test_3.append(i[1])

print(f'Доход меньше 20.000 {low}, средняя добыча {sum(map(int, test_3)) / len(test_3)}')
