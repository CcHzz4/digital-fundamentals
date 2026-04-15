array = list(map(int, input('Введите ваши числа: ').split()))

res = 0
summa = 0

for i in range(len(array)):
    summa += array[i]

res = summa / len(array)

print(res)
