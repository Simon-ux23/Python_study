# Определите количество четных элементов в последовательности, завершающейся числом 0.
s = 0
n = int(input())
while n != 0:
    if n % 2 == 0:
        s += 1
    n = int(input())
print(s)