#Даны три целых числа. Выведите значение наименьшего из них.
a = int(input("введите число"))
b = int(input("введите число"))
c = int(input("введите число"))
if a < b and a < c:
    print(a)
if b < a and b < c:
    print(b)
if c < a and c < b:
    print(c)