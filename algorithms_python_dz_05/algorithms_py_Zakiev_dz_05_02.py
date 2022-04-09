# Алгоритмы и структуры данных на Python. Базовый курс
# Урок 5. Коллекции. Список. Очередь. Словарь.
# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля collections

from collections import deque


def list_hex_int(input_list):
    dict_deque = deque([str(i) for i in range(10)] + [chr(j) for j in range(65, 71)], 16)
    a_sum = 0
    for a in input_list:
        x = dict_deque.index(a) * 16 ** (len(input_list) - 1 - input_list.index(a))
        a_sum += x
    return a_sum


def dec_hex_list(y):
    dict_deque = deque([str(i) for i in range(10)] + [chr(j) for j in range(65, 71)], 16)
    dec_list = []
    while y >= 16:
        z_dec = y % 16
        dec_list.append(z_dec)
        y = y // 16
        if y < 16:
            dec_list.append(y)
    #
    out_hex_list = []
    for i in reversed(dec_list):
        out_hex_list.append(dict_deque[i])
    return out_hex_list


def main():
    print('Необходимо ввести 2 шестнадцатеричных числа.')
    print('*Примечание:'
          'шестнадцатеричное число состоит из символов: 0 1 2 3 4 5 6 7 8 9 A B C D E F')
    input_a = input('Введите первое шестнадцатеричное число (например A2): ').upper()
    input_b = input('Введите второе шестнадцатеричное число (например C4F): ').upper()

    # input_a = 'A2'
    # input_b = 'C4F'
    print('\nВы ввели:')
    print(input_a)
    print(input_b)
    #
    list_a = list(input_a)
    list_b = list(input_b)

    print('=' * 35)
    print('Сумма:')
    print(list_a, '+', list_b, '=', dec_hex_list(list_hex_int(list_a) + list_hex_int(list_b)))
    print('Произведение:')
    print(list_a, '*', list_b, '=', dec_hex_list(list_hex_int(list_a) * list_hex_int(list_b)))


if __name__ == '__main__':
    main()
#
