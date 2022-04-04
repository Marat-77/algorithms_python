# Алгоритмы и структуры данных на Python. Базовый курс
# Урок 4. Эмпирическая оценка алгоритмов на Python
#
# 1. Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
# Проанализировать скорость и сложность алгоритмов.
# Результаты анализа сохранить в виде комментариев в файле с кодом.
# ------------------------------------------------------------------------------------

# взял для анализа algorithms_py_Zakiev_dz_03_01.py

# divisible_count и divisible_count2 отличаются порядком перебора:
# divisible_count: элемент из (2 - 99) проверяется на кратность элементу из (2 - 9),
# divisible_count2: элемент из (2 - 9) проверяет наличие кратных ему элементов из (2 - 99).
#
# divisible_count2 и divisible_count3:
# в divisible_count3 список (2 - 99) уменьшается за счет исключения чисел меньших чем элемент из (2 - 9)
#
# в divisible_count4 элемент из (2 - 99) проверяется на наличие в списке кратных чисел (range с шагом i)
#
# divisible_count5 - используется пересечение множеств
#
# divisible_count6 - без использования пересечения множеств,
# так как пересечение множеств по сути будет множество с шагом i
# #########################################################################################
# divisible_count   divisible_count2   divisible_count3   divisible_count4
#       O(n*m)            O(m*n)          O(m*(n-m))            O(m*n)
# так как m от 2 до 9, то макс(m) = 9, а n увеличивается, то можно привести эти 4 варианта к O(n).
#
# divisible_count5   divisible_count6
#       O(m)               O(m)           * перебор ведется только по элементам (2 - 9)
# #########################################################################################
#
# Скорость:
# после нескольких тестов выбрал максимальные значения в виде целых мс:
# dc1 - divisible_count; dc2 - divisible_count2; dc3 - divisible_count3; dc4 - divisible_count4;
# dc5 - divisible_count5; dc6 - divisible_count6
#        n       dc1    dc2    dc3    dc4    dc5    dc6
#      1 000      1      2      2      2      1      0
#     10 000     15     13     14     25      8      2
#    100 000    148    132    137    270     66     10
#  1 000 000   1507   1302   1308   2475    602    103
# 10 000 000  14755  13225  13281  24960   5863   1026

# algorithms_py_Zakiev_dz_03_01.py
# Урок 3. Массивы. Кортежи. Множества. Списки.
# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

import time


# def time_of_func(func):
#     def wrapper(*args):
#         start_time = time.time()
#         res = func(*args)
#         res_time = time.time() - start_time
#         print(func.__name__, ': время исполнения = ', res_time)
#         return res
#     return wrapper
def time_of_func(func):
    def wrapper(*args):
        start_time = time.time_ns()
        res = func(*args)
        res_time = time.time_ns() - start_time
        print(func.__name__, ': время исполнения = ', res_time, ' ns', res_time/1000000, ' ms')
        return res
    return wrapper


def divisible_num(divisible, divisor):
    if divisible % divisor == 0:
        return 1


@time_of_func
def divisible_count(n):
    div_count = 0
    for i in range(2, n):
        for j in range(2, 10):
            if divisible_num(i, j) == 1:
                div_count += 1
    return div_count


@time_of_func
def divisible_count2(n):
    div_count = 0
    for i in range(2, 10):
        for j in range(2, n):
            if divisible_num(j, i) == 1:
                div_count += 1
    return div_count


@time_of_func
def divisible_count3(n):
    div_count = 0
    for i in range(2, 10):
        for j in range(i, n):
            if divisible_num(j, i) == 1:
                div_count += 1
    return div_count


@time_of_func
def divisible_count4(n):
    div_count = 0
    for i in range(2, 10):
        for j in range(i, n):
            if j in range(0, n, i):
                div_count += 1
    return div_count


@time_of_func
def divisible_count5(n):
    div_count = 0
    for i in range(2, 10):
        test_set = set(range(i, n))
        y_set = set(range(0, n, i))
        div_count += len(test_set & y_set)
    return div_count


# так как пересечение множеств по сути будет множество с шагом i:
@time_of_func
def divisible_count6(n):
    div_count = 0
    for i in range(2, 10):
        div_count += len(set(range(i, n, i)))
    return div_count


def test_alg():
    n = 10
    for i in range(1, 5):
        print('№ ', i)
        m = n * 10 ** i
        print(m)
        divisible_count(m)
        divisible_count2(m)
        divisible_count3(m)
        divisible_count4(m)
        divisible_count5(m)
        divisible_count6(m)


#
def main():
    print(time.ctime())
    for t in range(3):
        print('\nпроход № ', t+1)
        test_alg()
    print(time.ctime())


if __name__ == '__main__':
    main()
