t = int(input())
for i in range(t):
    l = input().split()
    st = l[0]
    s = int(l[1])
    result = ""
    for c in st:
        if ord(c) + s > 90:
            result += chr(64 + ord(c) + s - 90)
        else:
            result += chr(ord(c) + s)
    print(result)
