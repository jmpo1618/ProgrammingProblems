def answer(x):
    distinct = set()
    for s in x:
        if s not in distinct and s[::-1] not in distinct:
            distinct.add(s)
    return len(distinct)
