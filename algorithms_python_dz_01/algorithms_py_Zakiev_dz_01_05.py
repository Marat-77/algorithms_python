# Урок 1. Введение в алгоритмизацию и реализация простых алгоритмов на Python
# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.


def alphabet_number(symb_a, symb_b):
    symb_a = ord(symb_a.lower())
    symb_b = ord(symb_b.lower())
    if symb_a > symb_b:
        symb_a, symb_b = symb_b, symb_a
    if symb_a in range(97, 123):
        if symb_b in range(97, 123):
            print(f'Буквы английского алфавита')
            a_num = symb_a - 96
            b_num = symb_b - 96
            print(f'Буква "{chr(symb_a)}" - № "{a_num}" в английском алфавите')
            print(f'Буква "{chr(symb_b)}" - № "{b_num}" в английском алфавите')
            print(f'Между ними {b_num - a_num - 1} букв')
        else:
            print(f'Обе введенные буквы должны быть буквами английского или русского алфавита')
    elif (symb_a in range(1072, 1106)) and symb_a != 1104:
        if (symb_b in range(1072, 1106)) and symb_b != 1104:
            print(f'Буквы русского алфавита')
            if symb_a < 1078:
                a_num = symb_a - 1071
            elif symb_a == 1105:
                a_num = 7
            else:
                a_num = symb_a - 1070
            print(f'Буква "{chr(symb_a)}" - № "{a_num}" в русском алфавите')

            if symb_b < 1078:
                b_num = symb_b - 1071
            elif symb_b == 1105:
                b_num = 7
            else:
                b_num = symb_b - 1070
            print(f'Буква "{chr(symb_b)}" - № "{b_num}" в русском алфавите')
            print(f'Между ними {b_num - a_num - 1} букв')
        else:
            print(f'Обе введенные буквы должны быть буквами английского или русского алфавита')
    else:
        print(f'Обе введенные буквы должны быть буквами английского или русского алфавита')


def main():
    print('Введите по одной букве английского или русского алфавита (обе буквы должны быть из одного алфавита)')
    inp_a = input('Введите одну букву: ')
    inp_b = input('Введите еще одну букву: ')
    alphabet_number(inp_a, inp_b)


if __name__ == '__main__':
    main()
#
