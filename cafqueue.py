nums = [int(i) for i in input().split()]
queue = input()
for i in range(nums[1]):
    queue = queue.replace('BG', 'GB')
print(queue)

