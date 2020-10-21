"""
Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
"""
import time

t = time.time()
i = 1
sum = 0

while i<1000:
    if i*3<1000:
        sum = sum + i*3
    if i*5<1000:
        sum = sum + i*5
    i = i+1

t = time.time() - t
print (sum)
print (t)
input('Press ENTER to exit')
