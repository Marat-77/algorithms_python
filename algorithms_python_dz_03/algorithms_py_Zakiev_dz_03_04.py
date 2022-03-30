# Урок 3. Массивы. Кортежи. Множества. Списки.
# 4. Определить, какое число в массиве встречается чаще всего.

def popular_num(input_list):
    mlist = [2, 3, 5, 6, 9, 2, 3, 5, 0, 1, 2, 2, 0]
    mset = set(input_list)
    max_count = 0
    max_count_idx = 0
    for i in mset:
        if mlist.count(i) > max_count:
            max_count = mlist.count(i)
            max_count_idx = i
    return max_count_idx


def main():
    print('Определить, какое число в массиве встречается чаще всего.')
    test_list = [2, 3, 5, 6, 9, 2, 3, 5, 0, 1, 2, 2, 0]
    'В проверяемом массиве чаще всего встречается число: '
    print(popular_num(test_list))
    print(f'В проверяемом массиве чаще всего встречается число: {popular_num(test_list)}')


if __name__ == '__main__':
    main()
#
