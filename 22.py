def completion (l):
    m = [0] * l
    for i in range(l):
       m[i] = float(input("Введите число: "))
    print("Массив:", m)
    return (m)
a = int(input("Введите размер массива 1: "))
A = completion (a)
print()
b = int(input("Введите размер массива 2: "))
B = completion (b)
print()
c = list(set(A) & set(B))
if len(c) > 0:
     print("Общие элементы:", c)
else:
     print("Общих элементов не найдено")
input()