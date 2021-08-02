# Задача 1
dict = {}
n = 100
for i in range(2, 10):
    counter = 0
    for m in range(i, n +1, i):
        if m < n:
            counter += 1
            dict.update({i: counter})
print(dict)

# Задача 2

# Задача 3
list = [2, 5, 4, 4, 6, 8, 2, 7, 9]

max_value = 0
min_value = 0

for index in range(len(list)):
    if list[index] > list[max_value]:
        max_value = index
    elif list[index] < list[min_value]:
        min_value = index
list[max_value],list[min_value] = list[min_value], list[max_value]
print(list)

# Задача 4
# Задача 5
# Задача 6
# Задача 8
# Задача 8
# Задача 9
