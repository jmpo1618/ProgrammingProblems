from collections import defaultdict, deque
from queue import PriorityQueue


for _ in range(int(input())):
    n, p, c = [int(i) for i in input().split()]
    graph = defaultdict(set)
    first = ''
    for _ in range(c):
        a, b = [i for i in input().split()]
        graph[a].add(b)
        graph[b].add(a)
        first = ''
    print(graph)

    pq = PriorityQueue()
    visited = set()
    for node in list(graph):
        stack = deque()
        stack.appendleft(first)
        count = 1
        while len(stack) > 0 and node not in visited:
            curr = stack.popleft()
            print(graph[curr])
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    stack.appendleft(neighbor)
                    count += 1
                    print(count)

    total = 0
    count = 0
    while not pq.empty:
        total += -(pq.get()[0])
        count += 1
        if total >= n:
            print(count)
    print('IMPOSSIBLE')
