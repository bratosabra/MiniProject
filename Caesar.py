eng_low = 'abcdefghijklmnopqrstuvwxyz'
eng_upp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_low = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upp = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def shifr(key):
    x = ''
    for i in range(len(phrase)):
        s = phrase[i]
        if s in eng_low + eng_upp:
            x += (eng_low[(eng_low.find(s) + key) % 26], eng_upp[(eng_upp.find(s) + key) % 26])[s.isupper()]
        elif s in rus_low + rus_upp:
            x += (rus_low[(rus_low.find(s) + key) % 32], rus_upp[(rus_upp.find(s) + key) % 32])[s.isupper()]
        else:
            x += s
    return x


method = input('Выберите метод: шифрование - Ш, дешифрование - Д\n').lower()
while method not in ['ш', 'д']:
    print('Некорректный ввод!')
    method = input('Введите метод:: шифрование - Ш, дешифрование - Д\n').lower()

key = input('Введите ключ шифрования\n'
            'Примечание: если ключ неизвестен, задайте его пределы через пробел и будет выведен список расшифровок\n')

flag = True
while flag:
    if key.isdigit():
        key = int(key)
        if method == 'д':
            key = -key
        flag = False
        phrase = input('Введите фразу\n')
        print('\n', shifr(key), sep='')
    else:
        key = key.split()
        if all([all([i.isdigit() for i in key]), len(key) == 2]):
            if int(key[0]) <= int(key[1]):
                flag = False
                phrase = input('Введите фразу\n')
                for i in range(int(key[0]), int(key[1]) + 1):
                    print(f'Ключ {i}: {shifr(i)}')
            else:
                print('Некорректный ввод!')
                key = input('Введите ключ\n')
        else:
            print('Некорректный ввод!')
            key = input('Введите ключ\n')
