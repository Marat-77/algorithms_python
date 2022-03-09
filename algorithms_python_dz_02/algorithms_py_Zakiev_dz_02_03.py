# Урок 2. Циклы. Рекурсия. Функции.
# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

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
    print(number)
    if number is False:
        print('Необходимо ввести натуральное число!')
    else:
        for i in reversed(number):
            print(i, end='')


if __name__ == '__main__':
    main()
#
