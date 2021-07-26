#Задача 1
import random

x = input('Введите трехзначное число')

if len(x) != 3:
    print(f'Введите трехзначное число')
else:
    summ = 0
    mult = 1
    for i in x:
        summ += int(i)
        mult *= int(i)

    print(summ)
    print(mult)


#Задача 2

x = 5
y = 6

print(f' {x} and {y} = {x and y}')
print(f' {x} or {y} = {x or y}')
print(f' {x} >> 2 = {x >> 2}')
print(f' {x} << 2 = {x << 2}')

#Задача 3
# не знаю как решать
#Задача 4

x = input('Верхняя граница')
у = input('Нижняя граница')
result = None

if x.isdigit() and у.isdigit():
    result = random.randint(int(x), int(y))
elif x.isalpha() and у.isalpha():
    result = chr((random.randint(ord(x), ord(y))))

#Задача 5
#Задача 6
#Задача 7
#Задача 8

year = int(input('Високосный ли год: '))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print('Год високосный')
else:
    print('Год не високосный')

#Задача 9