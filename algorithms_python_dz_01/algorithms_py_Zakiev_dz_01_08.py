# Урок 1. Введение в алгоритмизацию и реализация простых алгоритмов на Python
# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.

def bissextus(year):
    # високосный год
    # год, номер которого кратен 400, — високосный;
    # остальные годы, номер которых кратен 100, — невисокосные (например, годы 1800, 1900, 2100, 2200, 2300);
    # остальные годы, номер которых кратен 4, — високосные.
    # все остальные годы — невисокосные.
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def main():
    print('Проверим год: високосный или нет?')
    input_year = input('Введите год: ')
    try:
        input_year = int(input_year)
        if bissextus(input_year) is False:
            print(f'Год "{input_year}" невисокосный')
        else:
            print(f'Год "{input_year}" високосный')
    except ValueError:
        print('Необходимо ввести число!')


if __name__ == '__main__':
    main()
#
