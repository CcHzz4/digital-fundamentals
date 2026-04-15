array = list(map(int, input('Введите ваши числа: ').split()))

res = 0

for i in range(len(array)):
    if array[i] % 2 != 0:
        res += array[i]

print(res)
