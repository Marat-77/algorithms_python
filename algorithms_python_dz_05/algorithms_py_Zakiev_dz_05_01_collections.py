# Алгоритмы и структуры данных на Python. Базовый курс
# Урок 5. Коллекции. Список. Очередь. Словарь.

# 1. Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий,
# чья прибыль ниже среднего.

# с применением collections.namedtuple

# O(n) ????????????????????????????
#  10 000   =>   13 сек.


from collections import namedtuple
import random
import time


def timetest():
    n_companies = 100000
    max_pr = 1000
    dict_companies = {}
    sum_profits = 0
    for i in range(n_companies):
        dict_i = {}
        name = 'company_' + str(i)
        profit_lst = [0] * 5
        # 4 элемента - прибыль по кварталам
        # 5-й элемент - годовая прибыль
        CompanyProfit = namedtuple('Company', 'pr1 pr2 pr3 pr4 pr_y')
        for j in range(4):
            profit_lst[j] = random.randrange(max_pr)
        profit_lst[-1] = sum(profit_lst[:-1])
        profit_i = CompanyProfit(profit_lst[0], profit_lst[1], profit_lst[2], profit_lst[3], profit_lst[4])
        dict_i[name] = profit_i
        for val in dict_i.values():
            sum_profits += val[-1]
        dict_companies.update(dict_i)

    average = sum_profits / n_companies

    # *********************************************************************
    # проверка скорости фильтрации:
    start_time = time.time_ns()
    high_pr = [new_key for (new_key, new_value) in dict_companies.items() if dict_companies[new_key].pr_y >= average]
    low_pr = [new_key for (new_key, new_value) in dict_companies.items() if dict_companies[new_key].pr_y < average]
    res_time = time.time_ns() - start_time

    print('time (ms):', res_time / 1000)
    # *********************************************************************


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
        CompanyProfit = namedtuple('Company', 'pr1 pr2 pr3 pr4 pr_y')
        for j in range(4):
            print(f'Введите прибыль компании за {j + 1} квартал', end='')
            profit_lst[j] = int(input(': '))
        profit_lst[-1] = sum(profit_lst[:-1])
        profit_i = CompanyProfit(profit_lst[0], profit_lst[1], profit_lst[2], profit_lst[3], profit_lst[4])
        dict_i[name] = profit_i
        for val in dict_i.values():
            sum_profits += val[-1]
        dict_companies.update(dict_i)

    average = sum_profits / n_companies
    print('* ' * 30)
    print(
        '\nГодовая прибыль выше средней у компаний:\n',
        *[new_key for (new_key, new_value) in dict_companies.items() if dict_companies[new_key].pr_y >= average]
    )
    print(
        'Годовая прибыль ниже средней у компаний:\n',
        *[new_key for (new_key, new_value) in dict_companies.items() if dict_companies[new_key].pr_y < average]
    )


if __name__ == '__main__':
    main()
    # timetest()
#
