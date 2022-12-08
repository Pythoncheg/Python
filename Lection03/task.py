
def inputing():
    with open('lection03/file.txt', 'r') as input:
        for sumbol in input.readlines(1):
            spisok = sumbol.split()
            a = list(map(int, spisok))
            return a

finish = lambda x: [(i, i**2) for i in x if i%2==0]

a = inputing()
print(finish(a))


