#Факториалом числа n называется произведение 1 × 2 × ... × n. Обозначение: n!.
#По данному натуральному n вычислите значение n!. Пользоваться математической библиотекой math в этой задаче запрещено.
sum = 1
n = int(input("введите число"))
for i in range(n):
    number = int(input("введите число"))
    sum *=number
print(sum)