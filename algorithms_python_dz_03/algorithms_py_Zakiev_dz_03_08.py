# Урок 3. Массивы. Кортежи. Множества. Списки.
# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

# Матрица 5x4 - 5 сток, 4 столбца

def input_array(n, m):
    output_array = []
    for i in range(n):
        row_list = []
        for j in range(m):
            print(f'Введите целое число в ячейку {j + 1} строки {i + 1}', end=' ')
            x = int(input(': '))
            row_list.append(x)
        output_array.append(row_list)
    return output_array


def sum_row_array(z_array):
    for z_row in z_array:
        z_row.append(sum(z_row))
    return z_array


def sum_column_array():
    my_array = [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34], [41, 42, 43, 44]]
    new_array = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(len(my_array)):
        for j in range(len(my_array[0])):
            new_array[j][i] = my_array[i][j]
    fifth_row = []
    for _ in new_array:
        fifth_row.append(sum(_))
    my_new_array = my_array + [fifth_row]
    return my_array, my_new_array


def main():
    print('Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.')
    print('Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку '
          'строки.')
    print('В конце следует вывести полученную матрицу.')
    print()
    test_array = input_array(5, 4)
    # test_array = [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34], [41, 42, 43, 44], [51, 52, 53, 54]]
    print('\nВведённая матрица:')
    for _ in test_array:
        print(_)
    print()
    result_array = sum_row_array(test_array)
    print('Полученная матрица:')
    for _ in result_array:
        print(_)
    print()
    print('_' * 30)
    print('* Новая строка матрицы - сумма столбцов:')
    for _ in sum_column_array():
        print(_)


if __name__ == '__main__':
    main()
#
