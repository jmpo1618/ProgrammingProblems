n = int(input())
found = False
while not found:
    n += 1
    if len(set(str(n))) == 4:
        print(n)
        found = True
