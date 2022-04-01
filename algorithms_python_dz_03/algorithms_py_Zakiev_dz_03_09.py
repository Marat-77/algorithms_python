# Урок 3. Массивы. Кортежи. Множества. Списки.
# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random


# создание случайной матрицы
def create_random_array(n, m, max_range=10, min_range=0):
    output_array = []
    for i in range(n):
        row_list = []
        for j in range(m):
            x = random.randint(min_range, max_range)
            row_list.append(x)
        output_array.append(row_list)
    return output_array


# создание пустой матрицы N x M
def create_empty_array(n, m):
    output_empty_array = []
    for i in range(n):
        row_list = []
        for j in range(m):
            x = 0
            row_list.append(x)
        output_empty_array.append(row_list)
    return output_empty_array


def max_num_column(input_array):
    new_array = create_empty_array(len(input_array), len(input_array[0]))
    for i in range(len(input_array)):
        for j in range(len(input_array[0])):
            new_array[j][i] = input_array[i][j]
    fifth_row = []
    for _ in new_array:
        fifth_row.append(min(_))
    return max(fifth_row)
    

def main():
    print('Найти максимальный элемент среди минимальных элементов столбцов матрицы.\n')

    print('Исходная матрица:')
    random_array = create_random_array(5, 5, 100)
    for _ in random_array:
        print(_)
    #
    print(
        '\nМаксимальный элемент среди минимальных элементов столбцов матрицы: ',
        max_num_column(random_array)
    )


if __name__ == '__main__':
    main()
#
