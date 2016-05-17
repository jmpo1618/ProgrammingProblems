row = 1
for i in range(1, 6):
    r = input().split()
    if "1" in r:
        print(abs(3 - row) + abs(3 - (r.index("1") + 1)))
        break
    row += 1
