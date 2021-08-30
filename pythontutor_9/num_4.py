#Дано число n. Создайте массив размером n×n и заполните его по следующему правилу.
# На главной диагонали должны быть записаны числа 0. На двух диагоналях, прилегающих к главной, числа 1.
# На следующих двух диагоналях числа 2, и т.д.
n = int(input())
a = []
for i in range(n):
    a.append([int(i) for i in range(n)])



for i in range(n):
    for j in range(n):
        a[i][j] = abs(i - j)

for i in a:
    for j in i:
        print("".join(str(j)), end = " ")
    print()