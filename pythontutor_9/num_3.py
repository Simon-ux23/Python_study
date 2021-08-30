#Даны два числа n и m. Создайте двумерный массив размером n×m и заполните его символами "." и "*" в шахматном порядке.
# В левом верхнем углу должна стоять точка.
n, m = [int(i) for i in input().split()]
s = 1
a = []
for i in range(n):
    a.append(["."] * m)

for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 0:
            a[i][j] = "."
        else:
            a[i][j] = "*"




for i in a:
    for s in i:
        print("".join(s), end = " ")
    print()