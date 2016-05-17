n = int(input())
l = [0 for i in range(n + 1)]
nums = [int(i) for i in input().split()]
for i in range(n):
    l[nums[i]] = i + 1
for i in range(1, n + 1):
    print(str(l[i]) + " ", end="")
