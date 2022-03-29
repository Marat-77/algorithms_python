# Урок 2. Циклы. Рекурсия. Функции.
# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

def check_max(num_list):
    dict_sy = {
        i: sum([int(j) for j in i]) for i in num_list if i.isdigit()
    }
    max_val = max(dict_sy.values())

    # еще вариант:
    # print('=' * 40)
    # out_keys = (k for k, v in dict_sy.items() if v == max_val)
    # print(f'Максимальная сумма цифр = {max_val} в числах: ')
    # for _ in out_keys:
    #     print(_)
    # print('=' * 40)

    out_dict = {k: v for k, v in dict_sy.items() if v == max_val}
    if len(out_dict) == 1:
        for k, v in out_dict.items():
            print(f'Максимальная сумма цифр = {v} в числе "{k}"')
    else:
        print(f'Максимальная сумма цифр = {max_val} в числах: ', end=' ')
        for k in out_dict:
            print(f'{k}', end=' ')


def main():
    user_input = input('Введите через пробел несколько целых чисел: ')
    input_list = user_input.split()
    # input_list = ['23', '65543', '213', '99', '3154', '99', '', '', '3', '', '', '553550']  # для теста
    try:
        check_max(input_list)
    except ValueError:
        print('В введенных данных нет целых чисел')


if __name__ == '__main__':
    main()
# Захотелось вспомнить генераторы списков и словарей
