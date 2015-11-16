nums = input().split()
n, k = int(nums[0]), int(nums[1])
scores = list(int(i) for i in input().split())
cutoff = scores[k - 1]
sum = 0
for i in range(n):
    if scores[i] >= cutoff and scores[i] > 0: sum += 1
    else: break
print(sum)
