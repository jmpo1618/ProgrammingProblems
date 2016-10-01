s = input()
result = 0
for i in range(len(s)):
    if (i % 3 == 0 or i % 3 == 2) and not s[i] == 'S':
        result += 1
    elif i % 3 == 1 and not s[i] == 'O':
        result += 1
print(result)
