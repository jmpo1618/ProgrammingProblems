s = input()
hello = "hello"
index = 0
for c in s:
    if c == hello[index]:
        index += 1
        if index == 5: break
if index == 5: print("YES")
else: print("NO")
