# Урок 1. Введение в алгоритмизацию и реализация простых алгоритмов на Python
# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.


# detach digit
def detach_digit(number: int) -> list:
    """
    Function gets integer number, detaches a number into digits and return list of digit
    :param number: int
    :return: list
    """
    digits = []
    while number > 0:
        digits.append(number % 10)
        number //= 10
    return digits


# multiplication of numbers
def multiplication_numbers(num_list: list) -> int:
    """
    Function gets list of digits and multiplies them
    :param num_list: list of digits
    :return: int
    """
    mult_num = 1
    for i in num_list:
        mult_num *= i
    return mult_num


def main():
    # получить трехзначное число
    input_number = ''
    # проверка введенных данных
    # ############################################################
    # проверка "является ли числом":
    # while not input_number.isdigit():
    #     input_number = input('Введите трехзначное число: ')
    #     if not input_number.isdigit():
    #         print('Необходимо ввести число! Попробуйте еще раз:')
    # ############################################################

    # ############################################################
    # еще один вариант проверки:
    # while (not input_number.isdigit()) and (len(input_number) != 3):
    #     input_number = input('Введите трехзначное число: ')
    #     if not input_number.isdigit():
    #         print('Необходимо ввести число! Попробуйте еще раз')
    #     elif len(input_number) != 3:
    #         print('Необходимо ввести трехзначное число! Попробуйте еще раз')
    # ############################################################
    # проверка "трехзначное число?":
    flag = False
    while flag is False:
        input_number = input('Введите трехзначное число: ')
        if not input_number.isdigit():
            print('Необходимо ввести число! Попробуйте еще раз')
        elif int(input_number) not in range(100, 1000):
            print('Необходимо ввести трехзначное число! Попробуйте еще раз')
        else:
            flag = True
    input_number = int(input_number)

    print(f'Сумма цифр числа {input_number} = {sum(detach_digit(input_number))}')
    print(f'Произведение цифр числа {input_number} = {multiplication_numbers(detach_digit(input_number))}')


if __name__ == '__main__':
    main()
