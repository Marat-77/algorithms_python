# Урок 1. Введение в алгоритмизацию и реализация простых алгоритмов на Python
# 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.


def main():
    print('Побитовый "И" - Bitwise "AND" - "&"')
    print(f'5 & 6 = {5 & 6}')
    print(f'{bin(5)} - binary 5')
    print(f'{bin(6)} - binary 6')
    print(f'{bin(4)} - binary 4')

    print('\nПобитовый "ИЛИ" - Bitwise "OR" - "|"')
    print(f'5 | 6 = {5 | 6}')
    print(f'{bin(5)} - binary 5')
    print(f'{bin(6)} - binary 6')
    print(f'{bin(7)} - binary 7')

    print('\nПобитовый "Исключающее ИЛИ" - Bitwise "XOR" - "^"')
    print(f'5 ^ 6 = {5 ^ 6}')
    print(f'{bin(5)} - binary 5')
    print(f'{bin(6)} - binary 6')
    print(f'{bin(3)} - binary 3')

    print('\nПобитовый "НЕ" - Bitwise "NOT" - "~"')
    print(f'~5 = {~5}')
    print(f'{bin(5)} - binary 5')
    print(f'{bin(-6)} - binary -6')
    print(f'~6 = {~6}')
    print(f'{bin(6)} - binary 6')
    print(f'{bin(-7)} - binary -7')

    print('-' * 30)

    print('\nПобитовый сдвиг вправо - Bitwise right shift - ">>"')
    print(f'5 >> 2 = {5 >> 2}')
    print(f'{bin(5)} - binary 5')
    print(f'{bin(1)} - binary 1')

    print('\nПобитовый сдвиг влево - Bitwise left shift - "<<"')
    print(f'5 << 2 = {5 << 2}')
    print(f'{bin(5)} - binary 5')
    print(f'{bin(20)} - binary 20')


if __name__ == '__main__':
    main()
