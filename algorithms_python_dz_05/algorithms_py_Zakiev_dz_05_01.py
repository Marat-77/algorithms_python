# Алгоритмы и структуры данных на Python. Базовый курс
# Урок 5. Коллекции. Список. Очередь. Словарь.

# 1. Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий,
# чья прибыль ниже среднего.

# O(n)
#  10 000   =>   2 сек.
# 100 000   =>  27 сек.

import random
import time


def timetest():
    # print()
    n_companies = 100000
    max_pr = 1000
    dict_companies = {}
    sum_profits = 0
    for i in range(n_companies):
        dict_i = {}
        # name = ''
        name = 'company_' + str(i)
        # print(name)
        profit_lst = [0] * 5
        # 4 элемента - прибыль по кварталам
        # 5-й элемент - годовая прибыль
        for j in range(4):
            profit_lst[j] = random.randrange(max_pr)
            # profit_lst[j] = int(input(': '))
        profit_lst[-1] = sum(profit_lst[:-1])
        # print(profit_lst)
        dict_i[name] = profit_lst
        # print(dict_i)
        for val in dict_i.values():
            sum_profits += val[-1]
        dict_companies.update(dict_i)
    average = sum_profits / n_companies
    low_profit = []
    high_profit = []

    # *********************************************************************
    # проверка скорости фильтрации:
    start_time = time.time_ns()
    for key in dict_companies:
        if dict_companies[key][-1] < average:
            low_profit.append(key)
        else:
            high_profit.append(key)

    res_time = time.time_ns() - start_time

    print('time (ms):', res_time/1000)
    # *********************************************************************
    # print('\nГодовая прибыль выше средней у компаний:\n', *high_profit)
    # print('Годовая прибыль ниже средней у компаний:\n', *low_profit)


def main():
    n_companies = int(input('Введите количество компаний: '))
    dict_companies = {}
    sum_profits = 0
    for i in range(n_companies):
        dict_i = {}
        flag = False
        name = ''
        while flag is False:
            # проверка уникальности названия компании
            name = input('\nВведите название компании: ')
            if name in dict_companies:
                print('Данные о компании "', name, '" уже добавлены. Введите другую компанию')
            else:
                flag = True
        profit_lst = [0] * 5
        # 4 элемента - прибыль по кварталам
        # 5-й элемент - годовая прибыль
        for j in range(4):
            print(f'Введите прибыль компании за {j + 1} квартал', end='')
            profit_lst[j] = int(input(': '))
        profit_lst[-1] = sum(profit_lst[:-1])
        dict_i[name] = profit_lst
        for val in dict_i.values():
            sum_profits += val[-1]
        dict_companies.update(dict_i)
    average = sum_profits / n_companies
    low_profit = []
    high_profit = []
    for key in dict_companies:
        if dict_companies[key][-1] < average:
            low_profit.append(key)
        else:
            high_profit.append(key)
    print('\nГодовая прибыль выше средней у компаний:\n', *high_profit)
    print('Годовая прибыль ниже средней у компаний:\n', *low_profit)


if __name__ == '__main__':
    main()
    # timetest()
#
