# Задача 1
value = {'+': lambda a,b: a+b,
        '-': lambda a,b: a+b,
        '*': lambda a,b: a+b,
        '/': lambda a,b: a+b,
         }

while True:
    a = float(input('Введите число: '))
    b = float(input('Введите число: '))
    value_1 = input('Введите число или "0" для выхода: ')
    if value_1 == '/' and b == 0:
        print('На ноль делить нельзя')
        continue
    if value_1 in value:
        result = value[value_1](a,b)
        print(result)
    elif value_1 == '0':
        break
    else:
        print('Ошибка.Повторно введите число: ')

# Задача 2
a = int(input('Введите натуральное число: '))

count_1 = 0
count_2 = 0

while a > 0:
    if a % 10 % 2 == 0:
        count_1 += 1
    else:
        count_2 += 1
    a //= 10
print(f'четные - {count_1} и нечетные {count_2}')

# Задача 3
n = int(input('Введите число: '))
m = 0
while n > 0:
    m = m * 10 + n % 10
    n = n // 10
print(m)

# Задача 4
n = int(input('Введите число: '))

sum = 0
m = 1

for i in range(n):
    sum += m
    m /= -2
print(sum)

# Задача 5

# Задача 6

# Задача 7
# Задача 8
a = input('Введите последовательность чисел: ')
b = input('Введите искомое число: ')
count = 0
for i in a:
    if b == i:
        count += 1
print(count)

# Задача 9