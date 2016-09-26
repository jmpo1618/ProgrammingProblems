x, y, z = 0, 0, 0
for _ in range(int(input())):
    xi, yi, zi = [int(i) for i in input().split()]
    x += xi
    y += yi
    z += zi
if x or y or z:
    print("NO")
else:
    print("YES")
