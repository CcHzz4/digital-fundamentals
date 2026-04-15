a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a > b:
    max_ab = a
else:
    max_ab = b

if c > max_ab:
    max_c = c
else:
    max_c = max_ab

if d > max_c:
    max_d = d
else:
    max_d = max_c

print('Максимум:', max_d)
