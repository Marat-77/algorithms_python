# Урок 3. Массивы. Кортежи. Множества. Списки.
# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random


def random_array(num_elements, min_range, max_range):
    random_list = []
    for i in range(num_elements):
        # randint
        random_list.append(random.randint(min_range, max_range))
    return random_list


# max negative number
def max_negative(input_list):
    f_set = set(input_list)
    negative_list = []
    for i in f_set:
        if i < 0:
            negative_list.append(i)
    return max(negative_list), input_list.index(max(negative_list))


def main():
    m_array = (random_array(20, -1000, 1000))
    print('В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.')
    print('Исходный массив:')
    print(m_array)
    print(f'Максимальный отрицательный элемент: {(max_negative(m_array))[0]}, его индекс: {(max_negative(m_array))[1]}')


if __name__ == '__main__':
    main()
#
