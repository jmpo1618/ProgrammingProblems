n = int(input())
count = 0
for i in range(n):
    nums = [int(j) for j in input().split()]
    if nums[1] - nums[0] >= 2: count += 1
print(count)
