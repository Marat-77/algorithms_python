# Урок 1. Введение в алгоритмизацию и реализация простых алгоритмов на Python
# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.

# equation of the function
def equation(first_x, first_y, second_x, second_y):
    print(f'Координаты первой точки: ({first_x}; {first_y})')
    print(f'Координаты второй точки: ({second_x}; {second_y})')

    # k - угол наклона прямой
    # k = (first_y - second_y) / (first_x - second_x)
    # b = first_y - k * first_x

    if first_x == second_x and first_y == second_y:
        print(
            f'В данном случае не получим прямую (на плоскости XY), так как обе точки имеют одинаковые координаты: '
            f'({first_x}; {first_y})'
        )
    elif first_x == second_x:
        # Если это вертикальная прямая, то получим деление на "0":
        # k = (first_y - second_y) / 0
        print(f'Вертикальная прямая: x = {first_x}')
    else:
        k = (first_y - second_y) / (first_x - second_x)
        b = first_y - k * first_x
        # print(f'Уравнение прямой: y = {k}x + {b}')  # ---------------
        if k == 0 and b != 0:
            # случай, когда k=0, т.е. first_y = second_y
            print(f'Горизонтальная прямая: y = {b}')
        elif k == 1:
            if b < 0:
                print(f'Уравнение прямой: y = x - {abs(b)}')
            elif b == 0:
                print(f'Уравнение прямой: y = x')
            else:
                print(f'Уравнение прямой: y = x + {b}')
        elif k == -1:
            if b < 0:
                print(f'Уравнение прямой: y = -x - {abs(b)}')
            elif b == 0:
                print(f'Уравнение прямой: y = -x')
            else:
                print(f'Уравнение прямой: y = -x + {b}')
        elif b == 0:
            print(f'Уравнение прямой: y = {k}x')
        elif b < 0:
            print(f'Уравнение прямой: y = {k}x - {abs(b)}')
        else:
            print(f'Уравнение прямой: y = {k}x + {b}')


def main():
    x1 = input('Введите координату X первой точки: ')
    y1 = input('Введите координату X первой точки: ')
    x2 = input('Введите координату X первой точки: ')
    y2 = input('Введите координату X первой точки: ')
    try:
        x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)
        print(f'{x1}, {y1}, {x2}, {y2}')
        equation(x1, y1, x2, y2)
    except ValueError:
        print('Необходимо ввести числовые значения!')


if __name__ == '__main__':
    main()
