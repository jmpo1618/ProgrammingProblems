t = int(input())
for i in range(t):
    steps = 0
    l = [int(i) for i in input().split()]
    i = 0
    while i < 3:
        while l[i + 3] != l[i]:
            if l[i + 3] < l[i]:
                l[i + 3] += 1
                steps += 1
            elif l[i + 3] > l[i]:
                if l[i + 3] % 2 == 0:
                    l[i + 3] /= 2
                    steps += 1
                else:
                    l[i + 3] = (l[i + 3] + 1) / 2
                    steps += 2
        i += 1
    print(steps)
