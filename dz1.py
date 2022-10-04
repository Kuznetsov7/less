chislo = input('Введите число: ')
sum = 0
for i in list(chislo):
    if i != '.':
      sum += int(i)

print(sum)



