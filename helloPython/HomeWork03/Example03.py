
#  Задайте список из вещественных чисел. Напишите программу, 
#  которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

def separation (num:float) -> float:
    temp = str(num).split('.')
    return float('0.'+temp[1])

def finalResult (listNum: list[float]) -> float:
    finalList = [separation(i) for i in listNum if int(i) != float(i)]
    return max(finalList) - min(finalList)

firstDate= [1.1, 1.2, 3.1, 5, 10.01]

print(f'\nРазница между макс и мин значением дробной части элементов {firstDate} = {finalResult(firstDate)}.\n')
        