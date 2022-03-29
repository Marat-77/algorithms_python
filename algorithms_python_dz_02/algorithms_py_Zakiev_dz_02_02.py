# Урок 2. Циклы. Рекурсия. Функции.
# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

def input_num():
    x = input('Введите натуральное число: ')
    try:
        int(x)
        return x
    except ValueError:
        return False
    #


def main():
    number = input_num()
    if number is False:
        print('Необходимо ввести натуральное число!')
    else:
        print(number)
        print(type(number))
        even_nums = []
        odd_nums = []
        for i in number:
            if int(i) % 2 == 1:
                odd_nums.append(i)
            else:
                even_nums.append(i)
        print(f'Нечетных цифр: {len(odd_nums)}')
        print(f'Четных цифр: {len(even_nums)}')
    #


if __name__ == '__main__':
    main()
#
