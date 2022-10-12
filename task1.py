# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc

def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding


def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode

print('1. RLE архивирование')
print('2. RLE извлечение')
option = int(input('Выберите вариант: '))

with open('task1input.txt') as file:
    infile = file.read()
with open('task1deode.txt') as file:
    decodFile = file.read()

if option == 1 or option == 2:
    if option == 1:
        result = rle_encode(infile)
        with open('task1result.txt', 'w') as out:
            out.write(result)
            print(result)
    elif option == 2:
        resdecode = rle_decode(decodFile)
        with open('task1result.txt', 'a') as decod:
            decod.write('\n' + resdecode)
            print(resdecode)
else: #option != 1 or option != 2:
    print('Введен не правильный вариант')
