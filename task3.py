# 2. Создайте программу для игры с конфетами человек против человека.
# Правила: На столе лежит 150 конфет.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

import random

message = ['Хватай и беги', 'хватай больше, спаси диабетика', 'Хватай больше', 'Оооо Конфетки!',
           'Одну тебе, а все мне!', 'Попа слипнется!']


def player_vs_bot():
    candies_total = 150
    max_take = 28
    player1 = input('\n Введи своё имя: ')
    player2 = 'Ботяра'
    players = [player1, player2]
    print(f'\nСладкоежка {player1} и  Сладкоежка {player2} приготовтесь!\n')
    print('\nПодкинем монетку\n')

    lucky = random.randint(-1, 0)

    print(f'{players[lucky + 1]} ты ходишь первым !')

    while candies_total > 0:
        lucky += 1

        if players[lucky % 2] == 'Ботяра':
            print(
                f'\nХодит {players[lucky % 2]} \nНа кону {candies_total}. \n{random.choice(message)}: ')

            if candies_total < 29:
                step = candies_total
            else:
                div = candies_total // 28
                step = candies_total - ((div * max_take) + 1)
                if step == -1:
                    step = max_take - 1
                if step == 0:
                    step = max_take
            while step > 28 or step < 1:
                step = random.randint(1, 28)
            print(step)
        else:
            step = int(input(f'\nБери,  {players[lucky % 2]} \nНа кону {candies_total} \n{random.choice(message)}:  '))
            while step > max_take or step > candies_total:
                step = int(input(f'\nЖулик! За один ход можно взять {max_take} конфет, попробуй еще раз: '))
        candies_total = candies_total - step

    print(f'На кону осталось {candies_total} \nПобедил {players[lucky % 2]}')


player_vs_bot()
