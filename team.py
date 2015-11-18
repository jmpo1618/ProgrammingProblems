n = int(input())
result = 0
for i in range(n):
    nums = [int(j) for j in input().split()]
    s = sum(nums)
    if s >= 2: result += 1
print(result)
