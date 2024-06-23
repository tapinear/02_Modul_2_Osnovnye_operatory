# Задание "Слишком древний шифр":

def password(number):   # Функция возвращает строку, содержащую все натуральные числа от 1 до number, делящиеся на сумму всех предыдущих
    result = ''         # пустая строка
    for i in range(1, number):  # Перебираем все числа от 1 до number
        for j in range(i + 1, number):  # Перебираем все числа от i + 1 до number
            if number % (i + j) == 0:   # Если число делится на сумму всех предыдущи
                result += str(i) + str(j)   # Добавляем в строку числа i и j
    return result   # Возвращаем строку

print('Введите число n (от 3 до 20):')
print(password(int(input())))
