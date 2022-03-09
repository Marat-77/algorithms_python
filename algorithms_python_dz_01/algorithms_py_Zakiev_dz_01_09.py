# Урок 1. Введение в алгоритмизацию и реализация простых алгоритмов на Python
# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

def average_num(x, y, z):
    if x < y < z or z < y < x:
        print(f'Число {y} - среднее из этих трёх чисел')
    elif x < z < y or y < z < x:
        print(f'Число {z} - среднее из этих трёх чисел')
    else:
        print(f'Число {x} - среднее из этих трёх чисел')


def main():
    print('Необходимо ввести три разных числа')
    num_a = input('Введите первое число: ')
    num_b = input('Введите второе число: ')
    num_c = input('Введите третье число: ')
    try:
        num_a, num_b, num_c = float(num_a), float(num_b), float(num_c)
        if num_a == num_b or num_b == num_c or num_a == num_c:
            print('Числа должны быть разными!')
        else:
            average_num(num_a, num_b, num_c)
    except ValueError:
        print('Необходимо ввести числовые значения!')


if __name__ == '__main__':
    main()
#
