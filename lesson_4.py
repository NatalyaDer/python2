# Задача 1
import profile

year = int(input('Високосный ли год: '))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print('Год високосный')
else:
    print('Год не високосный')



year = int(input('Високосный ли год: '))
if year % 4 != 0:
    print("Год не високосный")
elif year % 100 != 0:
    if year % 400 == 0:
        print("Год високосный")
    else:
        print("Год не високосный")
else:
    print("Год високосный")

profile.run('main()')

# Задача 2
import profile


def test(num, n=10000):
    m = [i for i in range(n)]
    m[1] = 0
    for i in range(2, n):
        if m[i] != 0:
            j = i + i
            while j < n:
                m[j] = 0
                j += i
    result = [i for i in m if i != 0]
    print(f'Количество простых чисел в диапазоне до {n}: {len(result)}')
    assert num < len(result)
    return result[num - 1]

profile.run('main()')

