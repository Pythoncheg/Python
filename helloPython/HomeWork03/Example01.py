
# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
def printing(a):
    print(*a, sep= ' и ')
a: int = [random.randint(0, 9) for i in range(5)]
sum = 0
rev = []
for i in range(len(a)):
    if i%2!=0:
        sum += a[i]
        rev.append(a[i])
print(f"\n - {a} -> на нечетных позициях элементы {a[1]} и {a[3]}, ответ: {sum}\n")




