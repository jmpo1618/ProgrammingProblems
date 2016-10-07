n = int(input())
result = set(input())
for i in range(n - 1):
    result = result.intersection(set(input()))
print(len(result))
