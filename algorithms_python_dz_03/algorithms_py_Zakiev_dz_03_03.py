# Урок 3. Массивы. Кортежи. Множества. Списки.
# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random


def random_array(num_elements, max_range):
    random_list = []
    for i in range(num_elements):
        random_list.append(random.randrange(max_range))
    return random_list


def swap_min_max(list_n):
    max_n = max(list_n)
    min_n = min(list_n)
    max_i = list_n.index(max_n)
    min_i = list_n.index(min_n)
    list_n[max_i] = min_n
    list_n[min_i] = max_n
    return list_n


def main():
    print('В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.')
    m_array = (random_array(8, 1000))
    print('Исходный массив случайных целых чисел:', m_array)
    print(f'Максимальное число: {max(m_array)}')
    print(f'Минимальное число: {min(m_array)}')
    print(f'Измененный массив: {swap_min_max(m_array)}')


if __name__ == '__main__':
    main()
#
