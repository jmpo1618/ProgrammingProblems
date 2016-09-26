from collections import defaultdict, deque
import heapq


for _ in range(int(input())):
    n, p, c = [int(i) for i in input().split()]
    graph = defaultdict(set)
    for _ in range(c):
        a, b = [i for i in input().split()]
        graph[a].add(b)
        graph[b].add(a)

    pq = []
    connected = set()
    for node in graph.keys():
        stack = deque()
        stack.appendleft(node)
        visited = {node}
        count = 1
        while len(stack) > 0 and node not in connected:
            curr = stack.popleft()
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.appendleft(neighbor)
                    count += 1
        if node not in connected:
            connected.update(visited)
            heapq.heappush(pq, (-count, node))

    total = 0
    count = 0
    done = False
    while len(pq) > 0 and not done:
        total += -(heapq.heappop(pq)[0])
        count += 1
        if total >= n:
            done = True
            print(count)
    if not done:
        print('IMPOSSIBLE')
