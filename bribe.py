t = int(input())
for i in range(t):
    satisfied = []
    bags = []
    nums = [int(j) for j in input().split()]
    for j in range(nums[0]):
        bags.append([int(k) for k in input().split()])
    for j in range(nums[1]):
        l = input().split()
        name = l[0]
        needs = int(l[1])
        values = [int(l[k]) for k in range(2, 6)]
        for b in bags:
            s = sum([a * b for a,b in zip(b, values)])
            if s >= needs:
                satisfied.append(name)
                break
    satisfied.sort()
    print(" ".join(satisfied))
