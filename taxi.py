input()
groups = [int(n) for n in input().split()]
groups.sort(reverse=True)
result = 0
while groups:
    group = 0
    group += groups[0]
    groups.remove(group)
    full = False
    while not full:
        if not group == 4 and len(groups) > 0:
            if not group + groups[len(groups) - 1] > 4:
                group += groups.pop()
            else:
                full = True
        else:
            full = True
    result += 1
print(result)
