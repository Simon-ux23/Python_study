#Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).
a = []
n = int(input())
for i in range(n):
    a.append(int(input()))
print(a[::2])