# Урок 3. Массивы. Кортежи. Множества. Списки.
# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

def divisible_num(divisible, divisor):
    if divisible % divisor == 0:
        return 1


def divisible_count():
    div_count = 0
    for i in range(2, 100):
        for j in range(2, 10):
            if divisible_num(i, j) == 1:
                div_count += 1
    return div_count


def main():
    print(
        'В диапазоне натуральных чисел от 2 до 99 определить, '
        'сколько из них кратны каждому из чисел в диапазоне от 2 до 9.'
    )
    print(f'Всего кратных: {divisible_count()}')


if __name__ == '__main__':
    main()
#
