

# Задайте список из n чисел последовательности (1+1/n)^n 
# и выведите на экран их сумму.

# *Пример:*

# - Для n = 6: [2.0, 2.25, 2.37037037037037, 2.44140625, 2.4883199999999994, 2.5216263717421135]


n = int(input("Введите число N: "))
if n==0:
    print("Для нуля не будет последовательности.")
else:
    # final = list()
    # for i in range(1, n+1):
    #     sum = (1+1/i)**i
    #     final.append(sum)
    final = [(1+1/i)**i for i in range(1, n+1)] #Короткий вариант родился после длинного :)
    # final = [round((1+1/i)**i, 4) for i in range(1, n+1)] #Вариант с округлением до четырех знаков после запятой.
    print(f'- Для N =',n,':',final)
