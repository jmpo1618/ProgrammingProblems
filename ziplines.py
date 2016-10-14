def get_longest(hills, index, cur_len):
    m = cur_len
    for i in range(index - 2, index + 3):
        if i < len(hills) and i >= 0 and hills[i] < hills[index]:
            p = get_longest(hills, i, cur_len + 1)
            m = max(p, m)
    return m

n = int(input())
hills = []
for _ in range(n):
    hills.append(int(input()))

m = -1
for i in range(len(hills)):
    m = max(m, get_longest(hills, i, 0))
print(m)
