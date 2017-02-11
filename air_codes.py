for _ in range(int(input())):
    n = int(input())
    p = set(input() for _ in range(n))
    m = int(input())
    o = set(input() for _ in range(m))
    _p = sorted(p)
    _o = sorted(o)
    for elem in _p:
        if elem in o:
            print(elem)
    for elem in _o:
        if elem not in p:
            print(elem)
