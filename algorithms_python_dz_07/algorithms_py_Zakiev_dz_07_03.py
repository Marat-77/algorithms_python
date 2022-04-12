# Алгоритмы и структуры данных на Python. Базовый курс
# Урок 7. Алгоритмы сортировки
# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива.
import random
import time
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


# можно сделать эту функцию и с рекурсией, но я решил использовать цикл while
# @time_of_func
def search_median(random_list: list, m: int) -> int:
    """
    Функция удаляет максимальные элементы пока длина списка больше m+1
    :param random_list: list
    :param m: int
    :return: int
    """
    while len(random_list) > m + 1:
        random_list.remove(max(random_list))
    return max(random_list)


def memory_test(random_list, m):
    tracemalloc.start()
    search_median(random_list, m)  # проверяемая функция
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
    m = 10
    print('m =', m)
    print('2m + 1', 2 * m + 1)
    random_list = [random.randrange(100) for _ in range(2 * m + 1)]
    # list_for_test = sorted(random_list)  # отсортированный список для проверки
    print('Исходный массив:\n', random_list)
    median = search_median(random_list, m)
    print('Медиана =', median)

    # # проверка
    # print(list_for_test)
    # print(
    #     f'индекс медианы: {list_for_test.index(median)} в отсортированном списке из {len(list_for_test)} элементов'
    # )

    # # анализ времени выполнения:
    # search_median(random_list, m)

    # # анализ использования памяти:
    # memory_test(random_list, m)


if __name__ == '__main__':
    main()
#
# анализ времени выполнения:
# 101
# search_median : время исполнения =  0 ms
# 1001
# search_median : время исполнения =  9 ms
# 10001
# search_median : время исполнения =  804 ms
# 100001
# search_median : время исполнения =  67.2 s

# анализ использования памяти:
# 101
# Текущий размер блоков памяти = 6000(Б), пиковый размер блоков памяти = 6072(Б)
# algorithms_py_Zakiev_dz_07_03.py:33: size=512 B, count=1, average=512 B
# algorithms_py_Zakiev_dz_07_03.py:39: size=424 B, count=1, average=424 B
# algorithms_py_Zakiev_dz_07_03.py:40: size=416 B, count=1, average=416 B
# 1001
# Текущий размер блоков памяти = 10448(Б), пиковый размер блоков памяти = 10520(Б)
# algorithms_py_Zakiev_dz_07_03.py:33: size=4960 B, count=1, average=4960 B
# algorithms_py_Zakiev_dz_07_03.py:39: size=424 B, count=1, average=424 B
# algorithms_py_Zakiev_dz_07_03.py:40: size=416 B, count=1, average=416 B
# 10001
# Текущий размер блоков памяти = 53392(Б), пиковый размер блоков памяти = 53464(Б)
# algorithms_py_Zakiev_dz_07_03.py:33: size=46.8 KiB, count=1, average=46.8 KiB
# algorithms_py_Zakiev_dz_07_03.py:39: size=424 B, count=1, average=424 B
# algorithms_py_Zakiev_dz_07_03.py:40: size=416 B, count=1, average=416 B
