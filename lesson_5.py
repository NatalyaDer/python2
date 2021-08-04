# Задача 1
base = int(input('Вводите данные о количестве предприятий: '))
base_company = {}
sum_profit = 0

for i in range(base):
    name = input('Название предприятния')
    a = int(input('Доход первого года предприятния: '))
    b = int(input('Доход второго года предприятния: '))
    c = int(input('Доход третьего года предприятния: '))
    d = int(input('Доход четвертого года предприятния: '))
    year = a + b + c + d
    base_company[name] = year
    sum_profit += year


average_profit = sum_profit/base
print(average_profit)

# Задача 2
# разберу в уроке