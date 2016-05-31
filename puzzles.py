nums = [int(i) for i in input().split()]
pieces = [int(i) for i in input().split()]
pieces.sort()
mini = 10001
for i in range(nums[1] - nums[0]):
    dif = pieces[i + nums[0] - 1] - pieces[i]
    if dif < mini:
        mini = dif
print(mini)
