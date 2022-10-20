a = int(input("Введите число: "))
n = int(input("Введите целевую систему счисления: "))

b = ''

while a > 0:
    b = str(a % n) + b
    a //= n


print("Вывод: ", b)
input()