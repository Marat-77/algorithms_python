# Урок 3. Массивы. Кортежи. Множества. Списки.
# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random


def random_array(num_elements, min_range, max_range):
    random_list = []
    for i in range(num_elements):
        # randint
        random_list.append(random.randint(min_range, max_range))
    return random_list


# эта функция находит сумму всех элементов кроме максимального и минимального
def sum_elements(input_list):
    m_set = set(input_list)
    min_num = min(m_set)
    max_num = max(m_set)
    while input_list.count(min_num) != 0:
        input_list.remove(min_num)
    while input_list.count(max_num) != 0:
        input_list.remove(max_num)
    return min_num, max_num, sum(input_list)


def sum_between_min_max(input_list):
    m_set = set(input_list)
    min_ind = input_list.index(min(m_set))
    max_ind = input_list.index(max(m_set))
    if min_ind > max_ind:
        min_ind, max_ind = max_ind, min_ind
    return min(m_set), max(m_set), sum(input_list[min_ind + 1:max_ind])


def main():
    m_array = (random_array(20, 0, 1000))
    print('В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. '
          'Сами минимальный и максимальный элементы в сумму не включать.')
    print('Исходный массив:')
    print(m_array)
    min_el, max_el, sum_between = sum_between_min_max(m_array)
    print(f'\nМежду минимальным элементом ({min_el}) и максимальным элементом'
          f' ({max_el}) сумма элементов равна: {sum_between}')

    # не ту сумму посчитал! Надо сделать срез между индексами мин и мах.
    # min_el, max_el, sum_between = sum_elements(m_array)
    # print(f'\nМежду минимальным значением ({min_el}) и максимальным значением'
    #       f' ({max_el}) сумма элементов равна: {sum_between}')


if __name__ == '__main__':
    main()
#
