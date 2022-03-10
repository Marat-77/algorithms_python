# Урок 2. Циклы. Рекурсия. Функции.
# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.


def input_number(nums=False, max_n=None):
    x = input('')
    try:
        int(x)
        if max_n is not None:
            if int(x) not in range(max_n):
                return False
            else:
                if nums:
                    return int(x)
                else:
                    return x
        else:
            if nums:
                return int(x)
            else:
                return x
    except ValueError:
        return False


def main():
    print('Для создания последовательности необходимо ввести количество элементов последовательности,'
          ' затем ввести каждый элемент')
    n = False
    while n is False:
        print('Введите количество элементов:', end=' ')
        n = input_number(True)
        if n is False:
            print('Необходимо ввести целое число! Повторите ввод')
        elif n <= 0:
            print(f'Последовательность не может состоять из "{n}" элементов, попробуйте ввести значение больше 0')
            n = False
    print(f'Теперь необходимо ввести {n} числовых значений (целые числа) последовательности')
    str_nums = ''
    for i in range(n):
        element_i = False
        while element_i is False:
            print(f'{i + 1}: ', end='')
            print('Введите числовое значение:', end=' ')
            element_i = input_number()
            if element_i is False:
                print('Необходимо ввести целое число! Повторите ввод')
        str_nums += element_i
    search_digit = False
    while search_digit is False:
        print('Введите цифру (0...9), которую хотите найти в этой последовательности:', end=' ')
        search_digit = input_number(False, 10)
        if search_digit is False:
            print('Необходимо ввести цифру (0...9)! Повторите ввод')
    print(search_digit)
    print(f'Цифра "{search_digit}" встречается {str_nums.count(search_digit)} раз.')


if __name__ == '__main__':
    main()
#
