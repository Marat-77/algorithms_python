# Урок 2. Циклы. Рекурсия. Функции.
# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

def input_num():
    x = input('Введите целое число: ')
    try:
        x = int(x)
        return x
    except ValueError:
        return False


def main():
    print('Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...')
    print('Необходимо ввести Количество элементов (n)')
    number = input_num()
    print(f'кол-во: {number}')
    if number is False:
        print('Необходимо ввести натуральное число!')
    else:
        x = 1
        sum_n = 0
        for _ in range(number):
            sum_n += x
            x *= -0.5
        print(f'Сумма {number} элементов = {sum_n}')


if __name__ == '__main__':
    main()
#
