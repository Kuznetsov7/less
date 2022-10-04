from multiprocessing.sharedctypes import Value


N = int(input('Введите число N: '))
value = 1
list = []
for i in range(1, N+1):
    value *= i
    list.append(value)
print(list)
