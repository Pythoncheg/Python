
# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.
# * 6 -> [2,3]
# * 144 -> [2,3]

def multipl_num(x):
    factors =[]
    i = 2
    while x!=1:
        while x%i ==0:
            factors.append(i)
            x//=i
        i+=1
    return list(set(factors))

a = int(input("\nВведите число: "))
print(f'\n * {a} -> {multipl_num(a)}\n')