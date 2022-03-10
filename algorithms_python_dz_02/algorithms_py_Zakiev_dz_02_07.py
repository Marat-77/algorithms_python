# Урок 2. Циклы. Рекурсия. Функции.
# 7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

def input_number():
    x = input('Введите целое число: ')
    try:
        x = int(x)
        return x
    except ValueError:
        return False


def main():
    print('Проверим равенство "1+2+...+n = n(n+1)/2"')
    input_num = input_number()
    if input_num is False:
        print('Необходимо ввести целое число!')
    else:
        print(f'n = {input_num}')
        sum_numbers = 0
        for i in range(input_num + 1):
            sum_numbers += i
        print(f'Сумма арифметической прогрессии 1+2+...+n = {sum_numbers}')
        sum_formula = int(input_num * (input_num + 1) / 2)
        print(f'n(n+1)/2 = {sum_formula}')
        print(f'1+2+...+n = n(n+1)/2: {sum_numbers == sum_formula}')


if __name__ == '__main__':
    main()
#
