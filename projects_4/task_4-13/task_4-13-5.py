array = list(map(int, input('Введите числа: ').split()))
maxi = 0 

for i in range(len(array)):
    if array[i] > maxi:
        maxi = array[i]

print('Максимум: ', maxi)
