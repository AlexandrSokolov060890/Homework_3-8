my_file = open('test.txt', 'w')
line_v = input('Введите текст \n')
strs = []
while line_v:
    strs.append(my_file.writelines(line_v + '\n'))
    line_v = input('Введите текст \n')
    if not line_v:
        break
my_file.close()
my_file = open('test.txt', 'r')
for line in my_file:
    print(line)
my_file.close()
