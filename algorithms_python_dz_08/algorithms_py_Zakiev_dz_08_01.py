# Алгоритмы и структуры данных на Python. Базовый курс
# Урок 8. Деревья. Хэш-функция
# 1. Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.

import hashlib


def substring_count(input_string):
    input_string = str(input_string).lower()
    length = len(input_string)
    hash_set = set()
    for i in range(length + 1):
        for j in range(i + 1, length + 1):
            h = hashlib.sha1(input_string[i:j].encode('utf-8')).hexdigest()
            hash_set.add(h)
    return len(hash_set)


def main():
    some_string = 'loremipsumdolorsitamet'
    print('Исходная строка:\n', some_string)
    print('Количество различных подстрок в этой строке:', substring_count(some_string))  # 14


if __name__ == '__main__':
    main()
#
