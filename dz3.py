num = int(input('введите целое положительное число: '))
list = []
for i in range(1, num + 1):
    elem = round(((1 +1/i)**i),2)
    list.append(elem)
print(list)
print(f'сумма равна: {sum(list)}')
