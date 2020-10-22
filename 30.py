"""
Удивительно, но существует только три числа, которые могут быть записаны в виде суммы четвертых степеней их цифр:
1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
1 = 14 не считается, так как это - не сумма.
Сумма этих чисел равна 1634 + 8208 + 9474 = 19316.

Найдите сумму всех чисел, которые могут быть записаны в виде суммы пятых степеней их цифр.
"""

num = 2
end = 0

def sum5_func (num):
    i = 0
    sum = 0
    i_s = len(str(num))
    strnum = str(num)
    while i < i_s:
        sum += int(strnum[i])**5
        i += 1
    return sum
def sum9_func (num):
    i = 0
    sum = 0
    i_s = len(str(num))
    while i < i_s:
        sum += 9**5
        i += 1
    return sum

while True:
    num += 1
    if num > sum9_func (num): #Обозначил верхнюю границу
        break
    if sum5_func (num) == num:
        end += num

print (str(end))
input('Press ENTER to exit')
