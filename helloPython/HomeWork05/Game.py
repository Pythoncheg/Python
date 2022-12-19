

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


def game():
    candy = 117

    print(
        f"\nПривет!\nНа столе лежит {candy} конфет.\n"
        f"За один ход ты можешь взять не больше 28 конфет.\n"
        f"Побеждает тот, кто возьмет последние конфеты со стола."
        )
    player1 = input("\nВведите имя первого игрока: ")
    player2 = input('\nВведите имя второго игрока: ')

    print(f'\nПервый игрок - {player1}, Второй игрок - {player2}')
    current_gamer = start_rnd(player1, player2)

    for i in range(0, candy):
        print(f'\nХодит {current_gamer}')
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

game()
j = 1
print("\nДля выхода нажмите Enter...")
while j!=2:
    if keyboard.is_pressed('enter'):
        j+=1
        break
