"""
Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-ое простое число - 13.
Какое число является 10001-ым простым числом?
"""
import time

t = time.time()
num = 2
list = [2]

while len(list) < 10001:
    i = 0
    while i < len(list): # проверяю все простые числа по очереди
        if num % list[i] == 0: # если число целое, перехожу к следующему числу
            #print ("Число " + str(num) + " делется на " + str(list[i]) + ". Это не простое число!")
            i = len(list)
            break
        else: # Если число не целое, то делим на следующее простое
            #print ("Число " + str(num) + " не делется на " + str(list[i]) + ". Попробую следующий делитель!")
            i = i + 1
            if i == len(list): # Если список закончен, добавлю новый элемент
                #print ("Новое просто число: " + str(num) + " !")
                list.append(num)
                i = len(list)
    num = num + 1
#print ("Список простых чисел: " + str(list))


sum = list[len(list) - 1]
t = time.time() - t
print (sum)
print (t)
input('Press ENTER to exit')
