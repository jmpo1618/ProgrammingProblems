nums = list(int(i) for i in input().split())
result = 0
m2 = nums[0]
while nums[1] > 1:
    m1 = nums[0]
    while m1 > 0:
        result += 1
        m1 -= 1
    nums[1] -= 2
if nums[1] == 1:
    while m2 > 1:
        result += 1
        m2 -= 2
print(result)
