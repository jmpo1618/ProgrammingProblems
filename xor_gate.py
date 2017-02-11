for _ in range(int(input())):
    count = 0
    input()
    for elem in input().split():
        s = "{0:b}".format(int(elem))
        i = int(s[0])
        for c in range(1, len(s)):
            i = i ^ int(s[c])
        if i == 1:
            count += 1
    print(count)
