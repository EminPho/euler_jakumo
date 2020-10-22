"""
Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-ое простое число - 13.
Какое число является 10001-ым простым числом?
"""

num = 2
list = [2]

while len(list) < 10001:
    i = 0
    while i < len(list):
        if num % list[i] == 0:
            i = len(list)
            break
        else:
            i = i + 1
            if i == len(list):
                list.append(num)
                i = len(list)
    num = num + 1
sum = list[len(list) - 1]

print (sum)
input('Press ENTER to exit')
