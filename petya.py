a = input()
b = input()
x = a[:].upper()
y = b[:].upper()
if x == y:
    print(0)
elif x > y:
    print(1)
else:
    print(-1)
