array = list(map(int, input('Введите ваши числа: ').split()))

res = 0

for i in range(len(array)):
    if array[i] > 0:
        res += 1

print(res)
