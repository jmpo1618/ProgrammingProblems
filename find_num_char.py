s = input().strip()
n = int(input().strip())
mod = 0
for c in range(0, n % len(s)):
    if s[c] == 'a':
        mod += 1
count = mod
for c in range(n % len(s), len(s)):
    if s[c] == 'a':
        count += 1
count = count * (n // len(s)) + mod

print(count)
