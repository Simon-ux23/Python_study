#Дано несколько чисел. Вычислите их сумму.
# Сначала вводите количество чисел N, затем вводится ровно N целых чисел. Какое наименьшее число переменных нужно для решения этой задачи?
n = int(input("введите число"))
sum = 0
for i in range(n):
    number = int(input("введите число"))
    sum += number
print(sum)