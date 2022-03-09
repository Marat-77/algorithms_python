# Урок 1. Введение в алгоритмизацию и реализация простых алгоритмов на Python
# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

def main():
    input_number = 34
    if input_number in range(7):
        print(f'Буква русского алфавита: "{chr(input_number + 1071)}".\n'
              f'Буква английского алфавита: "{chr(input_number + 96)}".')
    elif input_number == 7:
        print(f'Буква русского алфавита: "{chr(1105)}".\n'
              f'Буква английского алфавита: "{chr(input_number + 96)}".')
    elif input_number in range(8, 27):
        print(f'Буква русского алфавита: "{chr(input_number + 1070)}".\n'
              f'Буква английского алфавита: "{chr(input_number + 96)}".')
    elif input_number in range(27, 34):
        print(f'Буква русского алфавита: "{chr(input_number + 1070)}".')
    else:
        print('В английском алфавите 26 букв, в русском - 33. Вероятно Вы ввели неверное число.')


if __name__ == '__main__':
    main()
#
