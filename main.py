# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

'''Chisla = [2,6,45,21,2,14,48,21,6,14]
Itog = []

Uniq = dict.fromkeys(Chisla,0)
print(Uniq.keys())


#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = 20

i = 2

primfac = []

while i * i <= n:
    while n % i == 0:
        primfac.append(int (i))
        n = n / i
    i = i + 1
if n > 1:
    primfac.append(int(n))

print(primfac)

# Задача: Вычислить число пи c заданной точностью d
# Формула Лейбница: X = 4 - 4/3 + 4/5 - 4/7 + 4/9 - ....

print('Введите необходимое значение точности: ')
d = int (input())
z = 1
x = 0

for i in range(0,1000000):
    if i%2 == 0:
        x = x + 4/z

    else:
        x = x - 4/z

    z = z + 2
Pi = str(x)
print('Число Пи равно: ', Pi[:(d+2)])
'''

# Задана натуральная степень n. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
#  и записать в файл многочлен степени пример записи в файл при n=3 ==> 33x^3 + 8x^2 + 64x + 85 = 0 при n=2 ==> 27x^2 + 95x + 79 = 0

''' 
print('Введите значение степени: ')
n = int(input())
x = "x"
plus = " + "
import random

nakopitel = " "

for i in range(1, n+1):
    a = random.randint(1, 100)
    z = str(a) + x + "^" + str(i) + plus
    nakopitel = z + nakopitel

nakopitel = nakopitel + str(random.randint(1, 100)) + " = 0"
print(nakopitel)

f = open("first_file.txt", "w")
f.write (nakopitel)
f.close()




from numpy.polynomial import Polynomial as P
import random
n = 5 #степень
coef_list=[]
for i in range(1,n+2):
    coef_list.append(random.randint(1,100))
    print(coef_list)
p = P(coef_list)
#print(p," = 0")

n = 3 #степень
coef_list=[]
for i in range(1,n+2):
    coef_list.append(random.randint(1,100))
d = P(coef_list)
#print(d," = 0")

f = open("second_file.txt", "w")
f.write (str(p))
f.close()

f = open("third_file.txt", "w")
f.write (str(d))
f.close()

t = 'second_file.txt'
f = open(t,'r')
polinom1 = " "
for i in f:
    polinom1 = polinom1 + i
#print(polinom1)
f.close()

list1 = []

res = polinom1.split(" + ")
#print((res))
for i in res:
   poisk = i.find(" x")
   if poisk == -1:
       fc = i.replace(".0","")
       list1.append(int(fc.replace(" ","")))
   if poisk>0:
       #print(poisk)
       list1.insert(0,int(i[:poisk].replace(".0","")))

print(list1)




import numpy as np
new = np.poly1d(list1)
print((new))


k = 'third_file.txt'
f = open(k,'r')
polinom2 = " "
for i in f:
    polinom2 = polinom2 + i
#print(polinom2)
f.close()

list2 = []

res2 = polinom2.split(" + ")
print((res2))
for i in res2:
   poisk2 = i.find(" x")
   if poisk2 == -1:
       fc2 = i.replace(".0","")
       list2.append(int(fc2.replace(" ","")))
   if poisk2>0:
       #print(poisk2)
       list2.insert(0,int(i[:poisk2].replace(".0","")))

print(list2)


new2 = np.poly1d(list2)
print((new2))

itog = new + new2
print(itog)
z = open("itog_file.txt", "w")
z.write (str(itog))
f.close()


