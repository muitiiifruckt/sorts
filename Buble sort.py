from random import randint # библиотека чтобы заполнить массив рандомными значениями

N = 10
a = []
for i in range(N):
    a.append(randint(1, 99)) #заполняем массив
print(a)

for i in range(N - 1):
    for j in range(N - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)