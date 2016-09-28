used = set()
for i in input():
    if not i == ' ':
        used.add(i.lower())
if len(used) == 26:
    print("pangram")
else:
    print("not pangram")
