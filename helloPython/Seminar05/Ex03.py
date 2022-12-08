
# Напишите программу, удаляющую из текста все слова, содержащие "абв".
# *' 'абвгд гдежз жзе абв ыопыпт' -> ' гдежз жзе ыопыпт'

a = 'абвгд гдежз жзе абв ыопыпт'
# list = a.split()


# def cyt(mas, x):
#     b = mas.find(x)
#     for i in mas:

#     # while b != -1:
#         print(b)
#         # mas.pop(b)
#         # del mas[b]


def ader(list, z):
    key = list.split()
    result = [i for i in key if z not in i]
    print(result)

ader(a, 'абв')