# Урок 2. Циклы. Рекурсия. Функции.
# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.

def input_nums():
    x = input('Введите первое число: ')
    y = input('Введите второе число: ')
    try:
        x, y = float(x), float(y)
        return x, y
    except ValueError:
        print('Необходимо ввести числовые значения!')
    #


def main():
    print('Необходимо ввести два числа')
    while True:
        print('\n----- основное меню: -----')
        user_choice = input(
            '"+" - Найти сумму чисел\n'
            '"-" - Найти разность чисел\n'
            '"*" - Найти произведение чисел\n'
            '"/" - Найти частное чисел\n'
            '0 - Выход\nВведите: '
        )
        print(f'\nВы выбрали: {user_choice}')
        if user_choice == '+':
            print('введите ....')
            print(f' Сумма чисел = {sum(input_nums())}')
        elif user_choice == '-':
            print('введите ....')
            num_a, num_b = input_nums()
            print(f' Разность чисел = {num_a - num_b}')
        elif user_choice == '*':
            print('введите ....')
            num_a, num_b = input_nums()
            print(f' Произведение чисел = {num_a * num_b}')
        elif user_choice == '/':
            print('введите ....')
            num_a, num_b = input_nums()
            if num_b != 0:
                print(f' Частное чисел = {num_a / num_b}')
            else:
                print('Второе число не может быть = 0, так как на 0 делить нельзя!')
        elif user_choice == '0':
            print('Вы вышли из программы')
            break
        else:
            print(f'Вы ввели: {user_choice} - в этом меню не используется')


if __name__ == '__main__':
    main()
#