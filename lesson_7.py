# Задача 1
from random import randint

nums = [randint(-100, 99) for _ in range(5)]

for i in range(len(nums)):
    for n in range(len(nums)-i-1):
        if nums[n] < nums[n+1]:
            nums[n], nums[n+1] = nums[n+1], nums[n]
            print(nums)
print(nums)