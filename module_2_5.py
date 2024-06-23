# Задача "Матрица воплоти":

def get_matrix(n, m, value):            # Объявляем матрицу размером n на m и заполняя ее value
    matrix = []                         # Создаем пустой список
    for i in range(n):                  # Создаем цикл for для кол-ва строк матрицы, n повторов
        matrix.append([])               # В первом цикле добавляйте пустой список в список matrix
        for j in range(m):              # Создаем цикл for для кол-ва столбцов матрицы, m повторов
            matrix[i].append(value)     # Во втором цикле добавляйте value в список matrix[i]
    return matrix                       # Возвращаем матрицу matrix

print(get_matrix(2, 2, 10))
print(get_matrix(3, 5, 42))
print(get_matrix(4, 2, 13))
