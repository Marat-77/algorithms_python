# Алгоритмы и структуры данных на Python. Базовый курс
# Урок 7. Алгоритмы сортировки
# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).

import random
import time
import math
import tracemalloc


def time_of_func(func):
    def wrapper(*args):
        start_time = time.time_ns()
        res = func(*args)
        res_time = time.time_ns() - start_time
        print(func.__name__, ': время исполнения = ', res_time, 'ns')
        print(func.__name__, ': время исполнения = ', res_time/1000000, 'ms')
        return res
    return wrapper


# O(n**2)
# сортировка методом "пузырька"
# @time_of_func
def bubble_sort(input_list: list) -> list:
    """
    Функция сортирует по убыванию входной список методом "пузырька" и выдаёт отсортированный список
    :param input_list: list
    :return: list
    """
    swapped = False
    for i in range(len(input_list) - 1, 0, -1):
        for j in range(i):
            if input_list[j] < input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
                swapped = True
        if swapped:
            swapped = False
        else:
            break
    return input_list


# разделение на 2 списка (negative_list и positive_list) - O(n)
# затем сортировка методом "пузырька" поочередно этих списков O((n-m)**2) O(m**2)
# объединение отсортированных списков
# в худшем случае (все элементы положительные или все отрицательные) O(n**2)
# вероятность худшего случая мала
# @time_of_func
def my_bubble_sort(input_list: list) -> list:
    """
    Функция делит входящий список на два - с отрицательными элементами и с положительными,
    затем использует функцию bubble_sort для каждого из получившихся списков,
    потом выдаёт объединенный список из двух отсортированных списков.
    :param input_list: list
    :return: list
    """
    negative_list = []
    positive_list = []
    for i in input_list:
        if i < 0:
            negative_list.append(i)
        else:
            positive_list.append(i)
    return bubble_sort(positive_list) + bubble_sort(negative_list)


# @time_of_func
def insert_sort(input_list: list) -> list:
    """
    Функция сортирует по убыванию входной список по алгоритму сортировки вставками и выдаёт отсортированный список.
    :param input_list: list
    :return: list
    """
    for i in range(1, len(input_list)):
        k = input_list[i]
        j = i - 1
        while input_list[j] < k and j >= 0:
            input_list[j + 1] = input_list[j]
            j -= 1
        input_list[j + 1] = k
    return input_list


# @time_of_func
def selection_sort(input_list: list) -> list:
    """
    Функция сортирует по убыванию входной список по алгоритму сортировки выбором и выдаёт отсортированный список.
    :param input_list: list
    :return: list
    """
    for i in range(len(input_list) - 1):
        min_idx = i
        for j in range(i+1, len(input_list)):
            if input_list[j] > input_list[min_idx]:
                min_idx = j
        input_list[i], input_list[min_idx] = input_list[min_idx], input_list[i]
    return input_list


# алгоритм быстрой сортировки
def quick_sort(input_list: list) -> list:
    """
    Функция сортирует по убыванию входной список по алгоритму быстрой сортировки и выдаёт отсортированный список.
    :param input_list: list
    :return: list
    """
    if len(input_list) < 2:
        return input_list
    pivot = input_list.pop()
    left_lst, equal_lst, right_lst = [], [pivot], []
    for i in input_list:
        if i == pivot:
            equal_lst.append(i)
        elif i < pivot:
            right_lst.append(i)
        else:
            left_lst.append(i)
    return quick_sort(left_lst) + equal_lst + quick_sort(right_lst)


# сортировка Шелла
# @time_of_func
def shell_sort(input_list: list) -> list:
    """
    Функция сортирует по убыванию входной список по алгоритму сортировки Шелла и выдаёт отсортированный список.
    :param input_list: list
    :return: list
    """
    n = len(input_list)
    k = int(math.log2(n))
    interval = 2**k - 1
    while interval > 0:
        for i in range(interval, n):
            temp = input_list[i]
            j = i
            while j >= interval and input_list[j - interval] < temp:
                input_list[j] = input_list[j - interval]
                j -= interval
            input_list[j] = temp
        k -= 1
        interval = 2**k - 1
    return input_list


# метод .sort()
# @time_of_func
def method_sort(input_list):
    input_list.sort(reverse=True)
    return input_list


# функция sorted()
# @time_of_func
def func_sorted(input_list):
    return sorted(input_list, reverse=True)


def memory_test(temps):
    tracemalloc.start()
    bubble_sort(temps)  # проверяемая функция
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
    temps = [random.randrange(-100, 100) for _ in range(n)]
    print('Исходный массив:\n', temps)
    # print('\nОтсортированный список (bubble_sort):')
    # print(bubble_sort(temps))
    print('\nОтсортированный список (my_bubble_sort):')
    print(my_bubble_sort(temps))

    # ******************************************************************************************
    # анализ времени выполнения:
    # bubble_sort(temps)  # 100: 2 ms; 1000: 72 ms; 10000: 7.7 s
    # my_bubble_sort(temps)  # 100: 0 ms; 1000: 35 ms; 10000: 3.7 s

    # insert_sort(temps)  # 100: 0 ms; 1000: 37 ms; 10000: 3.5 s
    # selection_sort(temps)  # 100: 0 ms; 1000: 33 ms; 10000: 3.2 s
    #
    # quick_sort
    # start_time = time.time_ns()
    # quick_sort(temps)  # 100: 0 ms; 1000: 1 ms; 10000: 10 ms; 100000: 101 ms; 1000000: 1.2 s
    # res_time = time.time_ns() - start_time
    # print('quick_sort: время исполнения = ', res_time, 'ns')
    # print('quick_sort: время исполнения = ', res_time / 1000000, 'ms')
    #
    # shell_sort(temps)  # 100: 0 ms; 1000: 2 ms; 10000: 32 ms; 100000: 501 ms; 1000000: 5.7 s

    # method_sort(temps)  # 10000: 1.0 ms; 100000: 13 ms; 1000000: 123 ms; 10000000: 1258 ms
    # func_sorted(temps)  # 10000: 1.0 ms; 100000: 2 ms; 1000000: 33 ms; 10000000: 362 ms
    # ******************************************************************************************

    # анализ использования памяти:
    # memory_test(temps)


if __name__ == '__main__':
    main()

# анализ времени выполнения:
#          n=     100   1000   10000   100000   1000000   10000000
# bubble_sort      2ms   72ms  7.7s     -       -
# my_bubble_sort   0ms   35ms  3.7s     -       -
# insert_sort      0ms   37ms  3.5s     -       -
# selection_sort   0ms   33ms  3.2s     -       -
# quick_sort       0ms   0ms      1ms   101ms    1.3s
# shell_sort       0ms   2ms     32ms   501ms    5.7s
# --------------------------------------------------------------------
# method_sort      0ms   0ms      0ms    13ms      123ms    1.2s
# func_sorted      0ms   0ms      1ms     2ms       33ms      362ms

# анализ использования памяти:
# ------------------------------------------------------------------------------- bubble_sort
# bubble_sort
# n= 100
# Текущий размер блоков памяти = 5312(Б), пиковый размер блоков памяти = 5384(Б)
# algorithms_py_Zakiev_dz_07_01.py:163: size=456 B, count=1, average=456 B
# algorithms_py_Zakiev_dz_07_01.py:164: size=416 B, count=1, average=416 B
#
# n= 10000
# Текущий размер блоков памяти = 5312(Б), пиковый размер блоков памяти = 5384(Б)
# algorithms_py_Zakiev_dz_07_01.py:163: size=456 B, count=1, average=456 B
# algorithms_py_Zakiev_dz_07_01.py:164: size=416 B, count=1, average=416 B
#
# ------------------------------------------------------------------------------ my_bubble_sort
# my_bubble_sort
# n= 100
# Текущий размер блоков памяти = 5480(Б), пиковый размер блоков памяти = 5552(Б)
# algorithms_py_Zakiev_dz_07_01.py:68: size=456 B, count=1, average=456 B
# algorithms_py_Zakiev_dz_07_01.py:163: size=440 B, count=1, average=440 B
# algorithms_py_Zakiev_dz_07_01.py:164: size=416 B, count=1, average=416 B
#
# n= 10000
# Текущий размер блоков памяти = 5480(Б), пиковый размер блоков памяти = 164544(Б)
# algorithms_py_Zakiev_dz_07_01.py:68: size=456 B, count=1, average=456 B
# algorithms_py_Zakiev_dz_07_01.py:163: size=440 B, count=1, average=440 B
# algorithms_py_Zakiev_dz_07_01.py:164: size=416 B, count=1, average=416 B
#
# ------------------------------------------------------------------------------ insert_sort
# insert_sort
# n= 100
# Текущий размер блоков памяти = 4920(Б), пиковый размер блоков памяти = 4992(Б)
# algorithms_py_Zakiev_dz_07_01.py:163: size=448 B, count=1, average=448 B
# algorithms_py_Zakiev_dz_07_01.py:164: size=416 B, count=1, average=416 B
#
# n= 10000
# Текущий размер блоков памяти = 4920(Б), пиковый размер блоков памяти = 4992(Б)
# algorithms_py_Zakiev_dz_07_01.py:163: size=448 B, count=1, average=448 B
# algorithms_py_Zakiev_dz_07_01.py:164: size=416 B, count=1, average=416 B
#
# ----------------------------------------------------------------------------- selection_sort
# selection_sort
# n= 100
# Текущий размер блоков памяти = 4920(Б), пиковый размер блоков памяти = 4992(Б)
# algorithms_py_Zakiev_dz_07_01.py:163: size=448 B, count=1, average=448 B
# algorithms_py_Zakiev_dz_07_01.py:164: size=416 B, count=1, average=416 B
#
# n= 10000
# Текущий размер блоков памяти = 4920(Б), пиковый размер блоков памяти = 4992(Б)
# algorithms_py_Zakiev_dz_07_01.py:163: size=448 B, count=1, average=448 B
# algorithms_py_Zakiev_dz_07_01.py:164: size=416 B, count=1, average=416 B
#
# ------------------------------------------------------------------------------ quick_sort
# quick_sort
# n= 100
# Текущий размер блоков памяти = 7232(Б), пиковый размер блоков памяти = 9792(Б)
# algorithms_py_Zakiev_dz_07_01.py:122: size=5464 B, count=19, average=288 B
# algorithms_py_Zakiev_dz_07_01.py:164: size=456 B, count=1, average=456 B
# algorithms_py_Zakiev_dz_07_01.py:114: size=280 B, count=5, average=56 B
#
# n= 10000
# Текущий размер блоков памяти = 10352(Б), пиковый размер блоков памяти = 399424(Б)
# algorithms_py_Zakiev_dz_07_01.py:122: size=7968 B, count=28, average=285 B
# algorithms_py_Zakiev_dz_07_01.py:114: size=896 B, count=16, average=56 B
# algorithms_py_Zakiev_dz_07_01.py:164: size=456 B, count=1, average=456 B
#
# ------------------------------------------------------------------------------- shell_sort
# shell_sort
# n= 100
# Текущий размер блоков памяти = 4936(Б), пиковый размер блоков памяти = 5008(Б)
# algorithms_py_Zakiev_dz_07_01.py:163: size=464 B, count=1, average=464 B
# algorithms_py_Zakiev_dz_07_01.py:164: size=416 B, count=1, average=416 B
#
# n= 10000
# Текущий размер блоков памяти = 4936(Б), пиковый размер блоков памяти = 5008(Б)
# algorithms_py_Zakiev_dz_07_01.py:163: size=464 B, count=1, average=464 B
# algorithms_py_Zakiev_dz_07_01.py:164: size=416 B, count=1, average=416 B
#
# =================================================================================================
# ------------------------------------------------------------------------------- method_sort
# method_sort
# n= 100
# Текущий размер блоков памяти = 5256(Б), пиковый размер блоков памяти = 5328(Б)
# algorithms_py_Zakiev_dz_07_01.py:164: size=416 B, count=1, average=416 B
# algorithms_py_Zakiev_dz_07_01.py:163: size=400 B, count=1, average=400 B
#
# n= 10000
# Текущий размер блоков памяти = 5256(Б), пиковый размер блоков памяти = 39248(Б)
# algorithms_py_Zakiev_dz_07_01.py:164: size=416 B, count=1, average=416 B
# algorithms_py_Zakiev_dz_07_01.py:163: size=400 B, count=1, average=400 B
#
# ------------------------------------------------------------------------------- func_sorted
# func_sorted
# n= 100
# Текущий размер блоков памяти = 5256(Б), пиковый размер блоков памяти = 5328(Б)
# algorithms_py_Zakiev_dz_07_01.py:164: size=416 B, count=1, average=416 B
# algorithms_py_Zakiev_dz_07_01.py:163: size=400 B, count=1, average=400 B
#
# n= 10000
# Текущий размер блоков памяти = 5256(Б), пиковый размер блоков памяти = 119304(Б)
# algorithms_py_Zakiev_dz_07_01.py:164: size=416 B, count=1, average=416 B
# algorithms_py_Zakiev_dz_07_01.py:163: size=400 B, count=1, average=400 B
# ----------------------------------------------------------------------------------
