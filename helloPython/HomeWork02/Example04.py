
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
# (для продвинутых - с файлом, вариант минимум - ввести позиции в консоли)

# -2 -1 0 1 2
# Позиции: 0,1 -> 2

n = int(input("Введите N: "))
list1 = [i for i in range(-n, n+1)]
print(f'\nСформирован список из промежутка -N до N: {list1}.')
temp = list()
with open("helloPython/HomeWork02/file.txt", "r") as f:
    for line in f.readlines(2):
        temp.append(int(line))

multipl = list1[temp[0]]*list1[temp[1]]
print(f'\nПроизведения чисел из списка по позициям {temp[0]} и {temp[1]}, указанным в file.txt равны: {multipl}\n')


