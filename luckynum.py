n = input()
ln = {7, 4, 47, 44, 74, 77, 444, 447, 474, 477, 777, 774, 744, 747}
lucky = True
for i in n:
    if not (i == '7' or i == '4'):
        lucky = False
        break
if lucky: print("YES")
else:
    n = int(n)
    for i in ln:
        if n % i == 0:
            lucky = True
            break
    if lucky: print("YES")
    else: print("NO")
