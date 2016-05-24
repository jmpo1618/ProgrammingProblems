import math
l = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
n = int(input())
group = 5
nums = 1
while n > group:
    n -= group
    group += group
    nums += nums
person = math.ceil(n / nums)
print(l[person - 1])
