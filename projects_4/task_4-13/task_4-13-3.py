N = int(input('Введите число: '))
fact = 1

for i in range(1, N + 1):
    fact = fact * i

print('Факториал: ', fact)
