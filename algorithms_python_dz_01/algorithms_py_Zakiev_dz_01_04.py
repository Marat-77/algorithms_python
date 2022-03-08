# # Урок 1. Введение в алгоритмизацию и реализация простых алгоритмов на Python
# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random
# пригодится для генерации случайных значений


def generate_int(int_a, int_b):
    # генерирует в указанных пользователем границах случайное целое число
    if int_a > int_b:
        int_a, int_b = int_b, int_a
    print(f'{int_a} - {int_b}')
    print(random.randint(int_a, int_b))


def generate_float(fl_a, fl_b):
    # генерирует в указанных пользователем границах случайное вещественное число
    if fl_a > fl_b:
        fl_a, fl_b = fl_b, fl_a
    print(f'{fl_a} - {fl_b}')
    print(random.uniform(fl_a, fl_b))


def generate_symbol(eng_a, eng_b):
    # генерирует в указанных пользователем границах случайный символ
    eng_a = ord(eng_a.lower())
    eng_b = ord(eng_b.lower())
    if eng_a > eng_b:
        eng_a, eng_b = eng_b, eng_a
    print(chr(random.randint(eng_a, eng_b)))


def generate_rus_symbol(rus_a, rus_b):
    # генерирует в указанных пользователем границах случайный символ
    print('random generator russian symbol')
    rus_a = ord(rus_a.lower())
    rus_b = ord(rus_b.lower())
    if rus_a > rus_b:
        rus_a, rus_b = rus_b, rus_a

    if rus_a in range(1072, 1077):
        if rus_b in range(1072, 1077):
            print(random.randint(rus_a, rus_b))  # -------------------------
            print(chr(random.randint(rus_a, rus_b)))
        elif rus_b == 1105:
            r = random.randint(rus_a, 1078)
            if r == 1078:
                r = 1105
            print(r)  # -------------------------
            print(chr(r))
        else:
            r = random.randint(rus_a, 1105)
            if r == 1104:
                r = 1105
            print(r)  # -------------------------
            print(chr(r))
    elif rus_a == 1105:
        r = random.randint(1077, rus_b)
        if r == 1077:
            r = 1105
        print(r)  # -------------------------
        print(chr(r))
    else:
        print(random.randint(rus_a, rus_b))  # -------------------------
        print(chr(random.randint(rus_a, rus_b)))


def main():
    #
    print('1. Получение случайного целого числа из диапазона')
    first = input('Введите первое число диапазона: ')
    last = input('Введите второе число диапазона: ')
    # first, last = int(first), int(last)
    try:
        first, last = int(first), int(last)
        generate_int(first, last)
    except ValueError:
        print('Необходимо ввести числовые значения!')
    #
    print('2. Получение случайного вещественного числа из диапазона')
    first = input('Введите первое число диапазона: ')
    last = input('Введите второе число диапазона: ')
    try:
        first, last = float(first), float(last)
        generate_float(first, last)
    except ValueError:
        print('Необходимо ввести числовые значения!')
    #
    print('3. Получение случайного символа английского алфавита')
    first = input('Введите первый символ английского алфавита: ')
    last = input('Введите второй символ английского алфавита: ')
    if len(first) != 1 and len(last) != 1:
        print('Необходимо ввести один символ английского алфавита')
    elif not first.isalpha() or not last.isalpha():
        print('Необходимо ввести символ английского алфавита')
    else:
        generate_symbol(first, last)
    #
    print('4. Получение случайного символа русского алфавита')
    first = input('Введите первый символ русского алфавита: ')
    last = input('Введите второй символ русского алфавита: ')
    if len(first) != 1 and len(last) != 1:
        print('Необходимо ввести один символ русского алфавита')
    elif not first.isalpha() or not last.isalpha():
        print('Необходимо ввести символ русского алфавита')
    else:
        generate_symbol(first, last)


if __name__ == '__main__':
    main()
#
