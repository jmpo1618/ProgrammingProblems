for _ in range(int(input())):
    n, m = [int(i) for i in input().split()]
    l = [int(i) for i in input().split()]
    l.sort()
    print(sum(l[:n - m]))
