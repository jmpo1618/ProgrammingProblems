from collections import defaultdict
import sys

n = int(input())
pre_reqs = defaultdict(set)
for _ in range(n):
    line = [elem for elem in input().split()]
    for i in range(int(line[1])):
        pre_reqs[line[0]].add(line[2 + i])

visited = set()
for elem in input().split():
    visited.add(elem)
    for pr in pre_reqs[elem]:
        if pr not in visited:
            print('BOOM!')
            sys.exit(0)
print('SAFE!')
