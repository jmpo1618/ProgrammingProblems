from collections import defaultdict

n = int(input())

unique = defaultdict(int)
for _ in range(n):
    s = input().lower()
    abc = [0] * 26
    for c in s:
        abc[ord(c) - 97] += 1
    unique[tuple(abc)] += 1

count = 0
for k in unique.keys():
    if unique[k] > 1:
        count += unique[k]
print(count)
