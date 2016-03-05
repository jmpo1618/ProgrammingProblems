import math

t = int(input())
for i in range(t):
    s = int(input())
    pairs = []
    nums = [int(j) for j in input().split()]
    j = 0
    while j < s * 2:
        pairs.append((nums[j], nums[j + 1]))
        j += 2
    min = math.sqrt((pairs[0][0] - pairs[1][0])**2 + (pairs[0][1] - pairs[1][1])**2)
    for j in range(s):
        k = j + 1
        while k < s:
            dist = math.sqrt((pairs[j][0] - pairs[k][0])**2 + (pairs[j][1] - pairs[k][1])**2)
            if dist < min: min = dist
            k += 1
    print("%.4f" % round(min, 4))

