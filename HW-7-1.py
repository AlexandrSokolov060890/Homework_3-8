class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __str__(self):
        matr = [[1, 0, 1],
                [0, 1, 0],
                [1, 0, 1],
                [0, 1, 0]]

        for i in range(len(self.list_1)):
            for j in range(len(self.list_2[i])):
                # return str(' '.join([' '.join([str(j) for j in i]) for i in matr])) #Для строки str, типа вся матрица превратилась в строку
                return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr])) #Для матрицы, если она есть привычный вид

    def __add__(self):
        matr = [[1, 0, 1],
                [0, 1, 0],
                [1, 0, 1],
                [0, 1, 0]]
        for i in range(len(self.list_1)):
            for j in range(len(self.list_2[i])):
                matr[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))


my_matrix = Matrix([[10, 1, 33],
                    [15, 26, 38],
                    [20, 51, 43],
                    [17, 31, 64]],
                   [[49, 78, 36],
                    [77, 54, 98],
                    [99, 60, 95],
                    [81, 18, 69]])

print(my_matrix.__str__())
print(my_matrix.__add__())
