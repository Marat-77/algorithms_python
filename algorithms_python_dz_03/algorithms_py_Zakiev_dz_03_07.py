# Урок 3. Массивы. Кортежи. Множества. Списки.
# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random


def random_array(num_elements, min_range, max_range):
    random_list = []
    for i in range(num_elements):
        random_list.append(random.randint(min_range, max_range))
    return random_list


def two_min_numbers(input_list):
    min_first = min(input_list)
    input_list.remove(min_first)
    min_second = min(input_list)
    return min_first, min_second


def main():
    m_array = (random_array(20, 0, 1000))
    print('В одномерном массиве целых чисел определить два наименьших элемента.'
          ' Они могут быть как равны между собой (оба являться минимальными), так и различаться.')
    print('Исходный массив:')
    print(m_array)
    min_1, min_2 = two_min_numbers(m_array)
    print(f'Два наименьших элемента: {min_1}, {min_2}')


if __name__ == '__main__':
    main()
#
