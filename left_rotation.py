def array_left_rotation(a, n, k):
    result = []
    for i in range(k, len(a)):
        result.append(a[i])
    for i in range(k):
        result.append(a[i])
    return result

n, k = [int(i) for i in input().strip().split(' ')]
a = [int(i) for i in input().strip().split(' ')]
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
