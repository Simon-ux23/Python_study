#Дан двумерный массив и два числа: i и j. Поменяйте в массиве столбцы с номерами i и j и выведите результат.
#Пограмма получает на вход размеры массива n и m, затем элементы массива, затем числа i и j.
n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()]for i in range(n)]
i, j = [int(i) for i in input().split()]
for s in range(n):
    for k in range(m):
