def total():
    try:
        with open('test_5.txt', 'w+') as file:
            num = input('Введите числа через пробел \n')
            file.writelines(num)
            my_numb = num.split()
            print(sum(map(int, my_numb)))
    except IOError:
        print('Error.')
    except ValueError:
        print('Ну просили числа же, в крайнем случае цифры. В следующий раз получится!')
total()

