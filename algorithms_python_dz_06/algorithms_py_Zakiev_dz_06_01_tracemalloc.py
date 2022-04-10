# Результаты после кода в конце файла (стр.111)

# algorithms_py_Zakiev_dz_03_09.py
# Урок 3. Массивы. Кортежи. Множества. Списки.
# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

# import sys
import random


# создание случайной матрицы
import tracemalloc


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
    # print('память используемая матрицей с нолями:', sys.getsizeof(new_array), 'bytes')
    for i in range(len(input_array)):
        for j in range(len(input_array[0])):
            new_array[j][i] = input_array[i][j]
    fifth_row = []
    for _ in new_array:
        fifth_row.append(min(_))
    return max(fifth_row)


def dz_03_09(n, m, max_range, min_range):
    # print('Найти максимальный элемент среди минимальных элементов столбцов матрицы.\n')

    # print('Исходная матрица:')
    random_array = create_random_array(n, m, max_range, min_range)
    # print(sys.getsizeof(random_array), 'bytes')
    # for _ in random_array:
    #     print(_)
    #
    print(
        '\nМаксимальный элемент среди минимальных элементов столбцов матрицы: ',
        max_num_column(random_array)
    )
    # print(sys.getsizeof(max_num_column(random_array)), 'bytes')


def main():
    print('=' * 45)
    n, m, max_range, min_range = 5, 5, 100, 0
    print(f'матрица {n} x {m}, максимальный размер чисел: {max_range}, минимальный: {min_range}')
    tracemalloc.start()
    dz_03_09(n, m, max_range, min_range)
    snapshot = tracemalloc.take_snapshot()
    # print('snapshot:', snapshot)
    top_stats = snapshot.statistics('lineno')
    # lineno - filename and line number
    print()
    current, peak = tracemalloc.get_traced_memory()  # Получение текущего размера и пикового размера блоков памяти
    print(f'Текущий размер блоков памяти = {current}(Б), пиковый размер блоков памяти = {peak}(Б)')
    #
    print()
    for stat in top_stats:
        print(stat)
    print()

    tracemalloc.clear_traces()
    print('=' * 45)
    n, m, max_range, min_range = 100, 100, 1000, 0
    print(f'матрица {n} x {m}, максимальный размер чисел: {max_range}, минимальный: {min_range}')
    tracemalloc.start()
    dz_03_09(n, m, max_range, min_range)
    snapshot = tracemalloc.take_snapshot()
    # print('snapshot:', snapshot)
    top_stats = snapshot.statistics('lineno')
    # lineno - filename and line number
    print()
    current, peak = tracemalloc.get_traced_memory()  # Получение текущего размера и пикового размера блоков памяти
    print(f'Текущий размер блоков памяти = {current}(Б), пиковый размер блоков памяти = {peak}(Б)')
    #
    print()
    for stat in top_stats:
        print(stat)
    print()

    tracemalloc.clear_traces()
    tracemalloc.stop()


if __name__ == '__main__':
    main()
#
# algorithms_py_Zakiev_dz_06_01_tracemalloc.py
# =============================================
# матрица 5 x 5, максимальный размер чисел: 100, минимальный: 0
#
# Максимальный элемент среди минимальных элементов столбцов матрицы:  14
#
# Текущий размер блоков памяти = 8370(Б), пиковый размер блоков памяти = 8738(Б)
#
# C:\python310\lib\random.py:370: size=512 B, count=1, average=512 B
# C:\project\algorithms_python\algorithms_python_dz_06\
# algorithms_py_Zakiev_dz_06_01_tracemalloc.py:54: size=496 B, count=1, average=496 B
# C:\project\algorithms_python\algorithms_python_dz_06\
# algorithms_py_Zakiev_dz_06_01_tracemalloc.py:39: size=472 B, count=1, average=472 B
# C:\project\algorithms_python\algorithms_python_dz_06\
# algorithms_py_Zakiev_dz_06_01_tracemalloc.py:61: size=464 B, count=1, average=464 B
# C:\python310\lib\random.py:352: size=432 B, count=1, average=432 B
# C:\project\algorithms_python\algorithms_python_dz_06\
# algorithms_py_Zakiev_dz_06_01_tracemalloc.py:72: size=416 B, count=1, average=416 B
# C:\project\algorithms_python\algorithms_python_dz_06\
# algorithms_py_Zakiev_dz_06_01_tracemalloc.py:59: size=34 B, count=1, average=34 B
#
# =============================================
# матрица 100 x 100, максимальный размер чисел: 1000, минимальный: 0
#
# Максимальный элемент среди минимальных элементов столбцов матрицы:  41
#
# Текущий размер блоков памяти = 6505(Б), пиковый размер блоков памяти = 394989(Б)
#
# C:\project\algorithms_python\algorithms_python_dz_06\
# algorithms_py_Zakiev_dz_06_01_tracemalloc.py:30: size=4424 B, count=79, average=56 B
# C:\python310\lib\random.py:292: size=1180 B, count=2, average=590 B
# C:\python310\lib\random.py:239: size=61 B, count=2, average=30 B
# C:\python310\lib\tracemalloc.py:558: size=56 B, count=1, average=56 B
#
#
# Process finished with exit code 0

# ---------------------------------------------------------------------------------------------
# В случае с матрицей 5 х 5 и числами до 100:
# Текущий размер блоков памяти = 8370(Б), пиковый размер блоков памяти = 8738(Б)
# В коде максимальный размер памяти (496 Байт) в строке 54:
# random_array = create_random_array(n, m, max_range, min_range)
# строка 39: new_array = create_empty_array(len(input_array), len(input_array[0]))
# строка 61: max_num_column(random_array)
# - код создания матриц

# ---------------------------------------------------------------------------------------------
# В случае с матрицей 100 х 100 и числами до 1000:
# Текущий размер блоков памяти = 6505(Б), пиковый размер блоков памяти = 394989(Б)  = 385(КБ)
# В коде максимальный размер памяти (4424 Байт) в строке 30:
# row_list = []
