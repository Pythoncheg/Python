

from random import randint as rnd
import keyboard
from progress.bar import Bar
import time



def start_rnd(p1, p2):
    tic1 = rnd(1, 6)
    tic2 = rnd(1, 6)
    if tic1 > tic2:
        print(f"Игрок {p1} ходит первым.")
        gamer = p1
        time.sleep(0.5)
    else:
        print(f"Игрок {p2} ходит первым.")
        gamer = p2
        time.sleep(0.5)
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
        time.sleep(0.5)
        player2 = input('\nВведите имя второго игрока: ')
        time.sleep(0.5)
    else:
        player1 = input("\nВведите имя первого игрока: ")
        time.sleep(0.5)
        player2 = "Бот Аркадий"

    print(f'\nПервый игрок - {player1}, Второй игрок - {player2}')
    current_gamer = start_rnd(player1, player2)
    time.sleep(0.7)
    bar = Bar('Конфеты', max=candy, suffix='%(remaining)d конфет осталось')
    for i in range(candy):
        for i in range(0, candy):
            print(f'\nХодит {current_gamer}')
            if bool == True and current_gamer != player1:
                ent = rnd(1, 29)
                print(f'Аркадий хапнул {ent} конфет')
                candy -= ent
                print('\n')
                bar.next(ent)
                
                time.sleep(0.7)
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
                    bar.next(ent)
                    time.sleep(0.7)
                if candy <= 0:
                    print(f'\nПобеда за {current_gamer} !!!')
                    bar.finish()
                    break
                else:
                    print('\n')
                    if current_gamer == player1:
                        current_gamer = player2
                    else:
                        current_gamer = player1
from progress.bar import Bar

bar = Bar('Загрузка',fill='*', max=100)
for i in range(100):
    time.sleep(0.1)
    bar.next()
bar.finish()
a = int(input('\nДля игры с ботом напишите "1", для игры в двоем напишите "2": '))
time.sleep(0.7)
if a == 1: b=True
else:
    b=False
game(b)
j = 1
print("\nДля выхода нажмите Enter...")
while j != 2:
    if keyboard.is_pressed('enter'):
        break
