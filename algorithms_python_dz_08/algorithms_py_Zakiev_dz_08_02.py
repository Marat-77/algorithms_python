# Алгоритмы и структуры данных на Python. Базовый курс
# Урок 8. Деревья. Хэш-функция
#
# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.

from sys import getsizeof
from collections import Counter


# class Node (вершина/узел)
# описывает элемент дерева.
class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value


# генерация кода (создание ключей шифрования)
def get_code(head, codes=dict(), code=''):
    if head is None:
        return None
    if isinstance(head.value, str):
        codes[head.value] = code
        return codes
    get_code(head.left, codes, code + '0')
    get_code(head.right, codes, code + '1')

    return codes


# создание дерева
def get_tree(string):
    # подсчет частоты
    string_count = Counter(string)
    if len(string_count) <= 1:
        node = Node(None)
        if len(string_count) == 1:
            node.left = Node([key for key in string_count][0])
            node.right = Node(None)
        string_count = {node: 1}
    while len(string_count) != 1:
        node = Node(None)
        spam = string_count.most_common()[:-3:-1]
        if isinstance(spam[0][0], str):
            node.left = Node(spam[0][0])
        else:
            node.left = spam[0][0]
        if isinstance(spam[1][0], str):
            node.right = Node(spam[1][0])
        else:
            node.right = spam[1][0]
        del string_count[spam[0][0]]
        del string_count[spam[1][0]]
        string_count[node] = spam[0][1] + spam[1][1]
    return [key for key in string_count][0]


# шифрование
def coding(string, codes):
    res = ''
    for symbol in string:
        res += codes[symbol]
    return res


# дешифрование
def decoding(string, codes):
    res = ''
    i = 0
    while i < len(string):
        for code in codes:
            if string[i:].find(codes[code]) == 0:
                res += code
                i += len(codes[code])
    return res


# loremipsumdolorsitamet
my_string = 'loremipsumdolorsitamet'
print('Исходная строка:\n', my_string, '\nРазмер:', getsizeof(my_string), 'байт.')
tree = get_tree(my_string)

codes = get_code(tree)
print('Ключи шифра:', codes)

coding_str = coding(my_string, codes)
print('Закодированная строка:\n', coding_str, '\nРазмер:', getsizeof(coding_str), 'байт.')

print('=' * 45)
decoding_str = decoding(coding_str, codes)
print('Раскодированная строка:\n', decoding_str)

if my_string == decoding_str:
    print('Раскодированная строка равна исходной строке!')
