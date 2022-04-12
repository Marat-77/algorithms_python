# Алгоритмы и структуры данных на Python. Базовый курс
# Урок 7. Алгоритмы сортировки
# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random
import time
import tracemalloc


def merge(left_list: list, right_list: list) -> list:
    """
    Функция слияния списков
    :param left_list: list
    :param right_list: list
    :return: list
    """
    sorted_list = []
    left_list_idx = right_list_idx = 0
    len_left_list, len_right_list = len(left_list), len(right_list)
    for _ in range(len_left_list + len_right_list):
        if left_list_idx < len_left_list and right_list_idx < len_right_list:
            if left_list[left_list_idx] <= right_list[right_list_idx]:
                sorted_list.append(left_list[left_list_idx])
                left_list_idx += 1
            else:
                sorted_list.append(right_list[right_list_idx])
                right_list_idx += 1
        elif left_list_idx == len_left_list:
            sorted_list.append(right_list[right_list_idx])
            right_list_idx += 1
        elif right_list_idx == len_right_list:
            sorted_list.append(left_list[left_list_idx])
            left_list_idx += 1

    return sorted_list


def merge_sort(input_list: list) -> list:
    """
    Функция сортировки слиянием
    :param input_list: list
    :return: list
    """
    # условие выхода из рекурсии merge_sort:
    if len(input_list) <= 1:
        return input_list
    # mid_idx - индекс середины списка
    mid_idx = len(input_list) // 2
    # рекурсивно проходим по левому и правому спискам:
    left_list = merge_sort(input_list[:mid_idx])
    right_list = merge_sort(input_list[mid_idx:])
    # производим слияние списков с помощью функции merge:
    return merge(left_list, right_list)


def time_test(random_list):
    start_time = time.time_ns()
    merge_sort(random_list)  # 100: 0 ms; 1000: 3 ms; 10000: 42 ms; 100000: 434 ms; 1000000: 5.2 s
    res_time = time.time_ns() - start_time
    print('merge_sort: время исполнения = ', res_time / 1000000, 'ms')


def memory_test(random_list):
    tracemalloc.start()
    merge_sort(random_list)  # проверяемая функция
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')
    # lineno - filename and line number
    current, peak = tracemalloc.get_traced_memory()  # Получение текущего размера и пикового размера блоков памяти
    print(f'Текущий размер блоков памяти = {current}(Б), пиковый размер блоков памяти = {peak}(Б)')
    #
    for stat in top_stats:
        print(stat)
    tracemalloc.clear_traces()
    tracemalloc.stop()


def main():
    n = 10
    print('n=', n)
    random_list = [round(random.uniform(0, 50), 2) for n in range(n)]
    print('Исходный массив:\n', random_list)
    print('\nОтсортированный массив (merge_sort):\n', merge_sort(random_list))

    # ******************************************************************************************
    # # анализ времени выполнения:
    # time_test(random_list)  # 100: 0 ms; 1000: 3 ms; 10000: 42 ms; 100000: 434 ms; 1000000: 5.2 s
    # ******************************************************************************************

    # ******************************************************************************************
    # # анализ использования памяти:
    # memory_test(random_list)
    # ******************************************************************************************


if __name__ == '__main__':
    main()
#
# анализ времени выполнения:
# n= 100
# merge_sort: время исполнения =  0 ms
# n= 1000
# merge_sort: время исполнения =  3 ms
# n= 10000
# merge_sort: время исполнения =  42 ms
# n= 100000
# merge_sort: время исполнения =  434 ms
# n= 1000000
# merge_sort: время исполнения =  5.2 s

# анализ использования памяти:
# n= 1000
# Текущий размер блоков памяти = 7883(Б), пиковый размер блоков памяти = 23311(Б)
# algorithms_py_Zakiev_dz_07_02.py:52: size=4456 B, count=11, average=405 B
# algorithms_py_Zakiev_dz_07_02.py:54: size=480 B, count=1, average=480 B
# algorithms_py_Zakiev_dz_07_02.py:60: size=440 B, count=1, average=440 B
# algorithms_py_Zakiev_dz_07_02.py:18: size=336 B, count=6, average=56 B
# algorithms_py_Zakiev_dz_07_02.py:39: size=195 B, count=2, average=98 B
# algorithms_py_Zakiev_dz_07_02.py:51: size=56 B, count=1, average=56 B

# n= 1000000
# Текущий размер блоков памяти = 13628(Б), пиковый размер блоков памяти = 16795168(Б)
# algorithms_py_Zakiev_dz_07_02.py:52: size=8856 B, count=21, average=422 B
# algorithms_py_Zakiev_dz_07_02.py:18: size=1456 B, count=26, average=56 B
# algorithms_py_Zakiev_dz_07_02.py:54: size=480 B, count=1, average=480 B
# algorithms_py_Zakiev_dz_07_02.py:60: size=440 B, count=1, average=440 B
# algorithms_py_Zakiev_dz_07_02.py:39: size=195 B, count=2, average=98 B
# algorithms_py_Zakiev_dz_07_02.py:11: size=193 B, count=2, average=96 B
# algorithms_py_Zakiev_dz_07_02.py:51: size=56 B, count=1, average=56 B
#
# Process finished with exit code 0
