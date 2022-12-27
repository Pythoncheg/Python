
# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)



n = int(input('\nВведите число из которого хотите получить факториал: '))
# # fact = 1
# # final = list()
# # revision = list()
# # for i in range(1, n+1):
# #     fact *= i
# #     final.append(fact)
# #     temp = i-1,'*',i     # Не понимаю как отобразить запись как в круглых скобках.
# #     revision.append(temp)
    
# # print("Пусть N = ",n, ", тогда ", final, revision)


import math

# def revision(n: int) -> str:
#     list = '1'
#     for i in range(2, n+1):
#         list += f'*{i}'
#     return list

# print(f"\nФакториал числа {n} = {[math.factorial(i) for i in range(1, n+1)]} {[revision(i) for i in range(1, n+1)]}\n")

print(f"\nФакториал числа {n} = {[math.factorial(i) for i in range(1, n+1)]} {[revision(i) for i in range(1, n+1)]}\n")
