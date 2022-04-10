# Алгоритмы и структуры данных на Python. Базовый курс
# Урок 6. Работа с динамической памятью
# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
# уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду.
# Также укажите в комментариях версию Python и разрядность вашей ОС.

# Версия Python: 3.10.2
# Операционная система: Windows-10-10.0.19044-SP0
# Информация об архитектуре: ('64bit', 'WindowsPE')
# Информация о машине: AMD64
# Объем установленной RAM:
# 17118003200 bytes (B)
# 16325 MB
# (Реальное) имя процессора: Intel64 Family 6 Model 60 Stepping 3, GenuineIntel
# Тактовая частота процессора: scpufreq(current=3300.0, min=0.0, max=3501.0)
# Текущая тактовая частота процессора: 3300.0 MHz
# Базовая тактовая частота процессора: 3501.0 MHz
# Количество ядер в системе: 4
# Версия Python: 3.10.2.final.0 (64 bit)
# Информация о процессоре: Intel(R) Core(TM) i5-4690 CPU @ 3.50GHz

# algorithms_py_Zakiev_dz_06_01.py   Размеры в байтах:
# =============================================
# матрица 5 x 5, максимальный размер чисел: 100, минимальный: 0
# Исходная матрица:
# 120 bytes
# память используемая матрицей с нолями: 120 bytes
#
# Максимальный элемент среди минимальных элементов столбцов матрицы:  25
# память используемая матрицей с нолями: 120 bytes
# Размер результата: 28 bytes
# =============================================
#
# матрица 10 x 10, максимальный размер чисел: 100, минимальный: 10
# Исходная матрица:
# 184 bytes
# память используемая матрицей с нолями: 184 bytes
#
# Максимальный элемент среди минимальных элементов столбцов матрицы:  34
# память используемая матрицей с нолями: 184 bytes
# Размер результата: 28 bytes
# =============================================
#
# матрица 10 x 10, максимальный размер чисел: 1000, минимальный: 100
# Исходная матрица:
# 184 bytes
# память используемая матрицей с нолями: 184 bytes
#
# Максимальный элемент среди минимальных элементов столбцов матрицы:  363
# память используемая матрицей с нолями: 184 bytes
# Размер результата: 28 bytes
# =============================================
#
# матрица 10 x 10, максимальный размер чисел: 10000, минимальный: 1000
# Исходная матрица:
# 184 bytes
# память используемая матрицей с нолями: 184 bytes
#
# Максимальный элемент среди минимальных элементов столбцов матрицы:  3483
# память используемая матрицей с нолями: 184 bytes
# Размер результата: 28 bytes
# =============================================
#
# матрица 100 x 100, максимальный размер чисел: 10000, минимальный: 1000
# Исходная матрица:
# 920 bytes
# память используемая матрицей с нолями: 920 bytes
#
# Максимальный элемент среди минимальных элементов столбцов матрицы:  1457
# память используемая матрицей с нолями: 920 bytes
# Размер результата: 28 bytes
# =============================================
#
# матрица 100 x 100, максимальный размер чисел: 10000, минимальный: 10000
# Исходная матрица:
# 920 bytes
# память используемая матрицей с нолями: 920 bytes
#
# Максимальный элемент среди минимальных элементов столбцов матрицы:  10000
# память используемая матрицей с нолями: 920 bytes
# Размер результата: 28 bytes
# =============================================
#
# матрица 1000 x 1000, максимальный размер чисел: 10000, минимальный: 10000
# Исходная матрица:
# 8856 bytes
# память используемая матрицей с нолями: 8856 bytes
#
# Максимальный элемент среди минимальных элементов столбцов матрицы:  10000
# память используемая матрицей с нолями: 8856 bytes
# Размер результата: 28 bytes


import sys
import random


# Информация о системе:
def my_system_info():
    import platform
    import psutil
    import cpuinfo

    print('Версия Python:', platform.python_version())  # 3.10.2
    print('Операционная система:', platform.platform())  # Windows-10-10.0.19044-SP0
    print('Информация об архитектуре:', platform.architecture())  # ('64bit', 'WindowsPE')
    print('Информация о машине:', platform.machine())  # AMD64
    print('Объем установленной RAM:')
    print(psutil.virtual_memory().total, 'bytes (B)')  # 17118003200 bytes (B)
    print(psutil.virtual_memory().total // 1024**2, 'MB')  # 16325 MB
    print('(Реальное) имя процессора:', platform.processor())  # Intel64 Family 6 Model 60 Stepping 3, GenuineIntel
    print('Тактовая частота процессора:', psutil.cpu_freq())  # scpufreq(current=3300.0, min=0.0, max=3501.0)
    print('Текущая тактовая частота процессора:', psutil.cpu_freq().current, 'MHz')  # 3300.0
    print('Базовая тактовая частота процессора:', psutil.cpu_freq().max, 'MHz')  # 3501.0
    print('Количество ядер в системе:', psutil.cpu_count())  # 4 - количество ядер в системе

    print('Версия Python:', cpuinfo.get_cpu_info()['python_version'])  # 3.10.2.final.0 (64 bit)
    print('Информация о процессоре:', cpuinfo.get_cpu_info()['brand_raw'])  # Intel(R) Core(TM) i5-4690 CPU @ 3.50GHz


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
    print('память используемая матрицей с нолями:', sys.getsizeof(new_array), 'bytes')
    for i in range(len(input_array)):
        for j in range(len(input_array[0])):
            new_array[j][i] = input_array[i][j]
    fifth_row = []
    for _ in new_array:
        fifth_row.append(min(_))
    return max(fifth_row)


def dz_03_09(n, m, max_range, min_range):
    # print('Найти максимальный элемент среди минимальных элементов столбцов матрицы.\n')

    print('Исходная матрица:')
    random_array = create_random_array(n, m, max_range, min_range)
    print(sys.getsizeof(random_array), 'bytes')
    # for _ in random_array:
    #     print(_)
    #
    print(
        '\nМаксимальный элемент среди минимальных элементов столбцов матрицы: ',
        max_num_column(random_array)
    )
    print('Размер результата:', sys.getsizeof(max_num_column(random_array)), 'bytes')


def main():
    # my_system_info()
    print('=' * 45)
    n, m, max_range, min_range = 5, 5, 100, 0
    print(f'матрица {n} x {m}, максимальный размер чисел: {max_range}, минимальный: {min_range}')
    dz_03_09(n, m, max_range, min_range)
    #
    print('=' * 45)
    n, m, max_range, min_range = 10, 10, 100, 10
    print(f'\nматрица {n} x {m}, максимальный размер чисел: {max_range}, минимальный: {min_range}')
    dz_03_09(n, m, max_range, min_range)
    #
    print('=' * 45)
    n, m, max_range, min_range = 10, 10, 1000, 100
    print(f'\nматрица {n} x {m}, максимальный размер чисел: {max_range}, минимальный: {min_range}')
    dz_03_09(n, m, max_range, min_range)
    #
    print('=' * 45)
    n, m, max_range, min_range = 10, 10, 10000, 1000
    print(f'\nматрица {n} x {m}, максимальный размер чисел: {max_range}, минимальный: {min_range}')
    dz_03_09(n, m, max_range, min_range)
    #
    print('=' * 45)
    n, m, max_range, min_range = 100, 100, 10000, 1000
    print(f'\nматрица {n} x {m}, максимальный размер чисел: {max_range}, минимальный: {min_range}')
    dz_03_09(n, m, max_range, min_range)
    #
    print('=' * 45)
    n, m, max_range, min_range = 100, 100, 10000, 10000
    print(f'\nматрица {n} x {m}, максимальный размер чисел: {max_range}, минимальный: {min_range}')
    dz_03_09(n, m, max_range, min_range)
    #
    print('=' * 45)
    n, m, max_range, min_range = 1000, 1000, 10000, 10000
    print(f'\nматрица {n} x {m}, максимальный размер чисел: {max_range}, минимальный: {min_range}')
    dz_03_09(n, m, max_range, min_range)


if __name__ == '__main__':
    main()
#

