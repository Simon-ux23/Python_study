#Дано N чисел: сначала вводится число N, затем вводится ровно N целых чисел.
# Подсчитайте количество нулей среди введенных чисел и выведите это количество. Вам нужно подсчитать количество чисел, равных нулю, а не количество цифр.
n = int(input("введите число"))
s = 0
for i in range(n):
    number = int(input("введите число"))
    if number == 0:
        s += 1
    else:
        s += 0
print(s)

