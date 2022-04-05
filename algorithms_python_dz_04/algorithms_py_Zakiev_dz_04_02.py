# Алгоритмы и структуры данных на Python. Базовый курс
# Урок 4. Эмпирическая оценка алгоритмов на Python
#
# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена».
# Проанализировать скорость и сложность алгоритмов.
# Результаты анализа сохранить в виде комментариев в файле с кодом.
# ------------------------------------------------------------------------------------
# Как я это понял: Найти в списке простых чисел i-тый элемент, т.е.:
# список простых чисел: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, ........]
# Найдём 5-й элемент (i=5) - это число 11.

# Анализ скорости:
#   n    search_simple   sieve_eratosthenes
#    10         0               0
#   100         1               9
#  1000       222            5531
# 10000     29403            ----
#

import time


def time_of_func(func):
    def wrapper(*args):
        start_time = time.time_ns()
        res = func(*args)
        res_time = time.time_ns() - start_time
        print(func.__name__, ': время исполнения = ', res_time/1000000, ' ms')
        return res
    return wrapper


def test_simple(x, start=2):
    if start < 2:
        start = 2
    flag = False
    for i in range(start, x):
        if x % i == 0:
            flag = True
            break
    if flag:
        return flag
    else:
        return flag


@time_of_func
def search_simple(n):
    count_simple = 1
    number = 2
    while 1:
        if test_simple(number) is False:
            if count_simple == n:
                break
            count_simple += 1
        number += 1
    return number


@time_of_func
def sieve_eratosthenes(n):
    if n == 1:
        return 2
    sieve = set(range(2, (n + 1)**2))
    res = []
    while sieve:
        prime = min(sieve)
        res.append(prime)
        sieve -= set(range(prime, (n + 1)**2, prime))
        if len(res) == n:
            break
    return res[-1]


#
def main():
    test_num = 18
    print('Номер в списке простых числе: ', test_num)

    print(search_simple(test_num))

    print(sieve_eratosthenes(test_num))

    # time test:
    print('\nтест')
    y = 3
    for j in range(1, y + 1):
        m = 10 ** j
        print(m)
        search_simple(m)
        sieve_eratosthenes(m)


if __name__ == '__main__':
    main()
