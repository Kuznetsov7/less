from array import array
import random
def mixs_list(array):
    array_mix = array
    for i in range(0,len(array)):
        rnd_posich = int(random.randrange(0, len(array)))
        tepm = array[i]
        temp2 = array_mix[rnd_posich]
        array_mix[rnd_posich] = tepm
        array_mix[i] = temp2
    return array_mix
n = int(input('введите размер списка: '))
list_first = list([random.randint(20,40) for i in range(0,n)])
print(f'\ncписок до \t {list_first}')
list_mixs = mixs_list(list_first)
print(f'Cписок после: \t{list_mixs}' )