for _ in range(int(input())):
    sigma = 0
    count = 0
    for _ in range(int(input())):
        s, d = [int(i) for i in input().split()]
        sigma += s * d
        count += d
    print(round(sigma / count))
