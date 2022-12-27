

from random import randint as rnd
import keyboard


def start_rnd(p1, p2):
    tic1 = rnd(1, 6)
    tic2 = rnd(1, 6)
    if tic1 > tic2:
        print(f"Игрок {p1} ходит первым.")
        gamer = p1
    else:
        print(f"Игрок {p2} ходит первым.")
        gamer = p2
    return gamer


def game(bool: False):
    candy = 117

    print(
        f"\nПривет!\nНа столе лежит {candy} конфет.\n"
        f"За один ход ты можешь взять не больше 28 конфет.\n"
        f"Побеждает тот, кто возьмет последние конфеты со стола."
    )
    if bool == False:
        player1 = input("\nВведите имя первого игрока: ")
        player2 = input('\nВведите имя второго игрока: ')
    else:
        player1 = input("\nВведите имя первого игрока: ")
        player2 = "Бот Аркадий"

    print(f'\nПервый игрок - {player1}, Второй игрок - {player2}')
    current_gamer = start_rnd(player1, player2)

    for i in range(0, candy):
        print(f'\nХодит {current_gamer}')
        if bool == True and current_gamer != player1:
            ent = rnd(1, 29)
            print(f'Аркадий хапнул {ent} конфет')
            candy -= ent
            print(f'\nОсталось {candy} конфет')
            if current_gamer == player1:
                current_gamer = player2
            else:
                current_gamer = player1
        else:
            ent = int(input('\nСколько хочешь забрать конфет?: '))
            if ent > 28:
                print('\nНе жадничай! Еще раз возьми.\n')
                ent = int(input('\nСколько хочешь забрать конфет?: '))
            else:
                candy -= ent
            if candy <= 0:
                print(f'\nПобеда за {current_gamer} !!!')
                break
            else:
                print(f'\nОсталось {candy} конфет')
                if current_gamer == player1:
                    current_gamer = player2
                else:
                    current_gamer = player1

a = int(input('\nДля игры с ботом напишите "1", для игры в двоем напишите "2": '))
if a == 1: b=True
else:
    b=False
game(b)
j = 1
print("\nДля выхода нажмите Enter...")
while j != 2:
    if keyboard.is_pressed('enter'):
        break
