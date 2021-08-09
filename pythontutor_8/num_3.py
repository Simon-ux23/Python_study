# Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
n = input()
a = [int(n) for n in n.split()]
for i in range(1,len(a)):
    if a[i] > a[i-1]:
        print(a[i])