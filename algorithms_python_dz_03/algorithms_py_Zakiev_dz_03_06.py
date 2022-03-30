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


def sum_elements(input_list):
    m_set = set(input_list)
    min_num = min(m_set)
    max_num = max(m_set)
    while input_list.count(min_num) != 0:
        input_list.remove(min_num)
    while input_list.count(max_num) != 0:
        input_list.remove(max_num)
    return min_num, max_num, sum(input_list)


def main():
    m_array = (random_array(20, 0, 1000))
    print('В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. '
          'Сами минимальный и максимальный элементы в сумму не включать.')
    print('Исходный массив:')
    print(m_array)
    min_el, max_el, sum_between = sum_elements(m_array)
    print(f'Между минимальным значением ({min_el}) и максимальным значением'
          f' ({max_el}) сумма элементов равна: {sum_between}')


if __name__ == '__main__':
    main()
#
