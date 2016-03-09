s = [int(i) for i in input().replace("+", "")]
s.sort()
s = [str(i) for i in s]
print("+".join(s))
