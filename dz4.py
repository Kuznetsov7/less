
import random


N = int(input('введите число N: '))
List =[]
Posishen = 1

with open('file txt' , 'w') as File:
    Count_Number = random.randrange(1,N)
    for i in range(0,Count_Number):
        File.writelines(str(random.randrange(0,N+1))+ '\n')

for i in range(-N,N+1):
    List.append(i)
print(List)

with open('file txt', 'r') as File:
    for line in File:
        Posishen*= List[int(line)]
print(f'произведение элементов на позициях = {Posishen}')
