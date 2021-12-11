my_file = open('test_2.txt', 'r')
print(f'Содержимое файла:\n{my_file.read()}')
my_file = open('test_2.txt', 'r')
print(f'Количество строк в файле - {len(my_file.readlines())}')
my_file = open('test_2.txt', 'r')
content = my_file.readlines()

for i in range(len(content)):
    print(f'Количество символов в {i + 1}-ой строке {len(content[i])}')
my_file.close()
